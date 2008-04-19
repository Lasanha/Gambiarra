#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (C) 2007 by ULPM: Alexandre Yukio Harano
#                             Fábio Cassarotti Parronchi Navarro
#                             Gabriel Geraldo França Marcondes
#                             Luiz Carlos Irber Júnior
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys

import pygame

from Gambiarra.command import Play, Help, Quit
from Gambiarra.gamemenu import GameMenu
import Gambiarra.levels as Levels

from Gambiarra.objects import Esteira, check_collision

class Game(object):
    # controle do jogo
    fps = 30
    playing = None
    running = None
    clock = None
    level = 0
    levels = []
    selected_element = None
    _showed_help = None
    count = None
    play_sounds = None

    # elementos do jogo
    screen = None
    menu = None
    congrats = None
    congrats_snd = None

    def __init__(self, play_sounds=True):
        pygame.init()
        self.play_sounds = play_sounds
        if self.play_sounds:
            pygame.mixer.init()
        self.screen = pygame.display.set_mode((1200, 900)) #omitindo flags
        pygame.display.flip()
        self.running = True
        self.playing = False
        pygame.display.set_caption("Gambiarra")
        self.clock = pygame.time.Clock()
        self.levels = Levels.init_levels()
        self.menu = GameMenu()
        self.congrats = pygame.image.load("data/images/fim_fase.png")
        if self.play_sounds:
            snd_file = "data/snd/Congrats.wav"
            self.congrats_snd = pygame.mixer.Sound(snd_file)
        self._showed_help = False
        self.count = 0

    def run(self):
        #inicia o loop
        self.main_loop()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_event( pygame.mouse.get_pos() )

    def update_screen(self, fps):
        #update dos elementos da tela
        if self.playing:

            # executa a simulacao
            objs = check_collision(self.levels[self.level].simulator.objects,
                                self.levels[self.level].simulator.static_objs)
            self.levels[self.level].simulator.objects = objs
            for obj in self.levels[self.level].simulator.objects:
                obj.update()
        else:
            if self.selected_element:
                if self.selected_element.editable:
                    self.selected_element.rect.center = pygame.mouse.get_pos()

    def mouse_event(self, mouse_pos):
        if not self.selected_element:
            mouse_move = (0, 0)
            mouse_move = pygame.mouse.get_rel()

            for element in self.levels[self.level].simulator.objects:
                if element.rect.collidepoint(mouse_pos):
                    self.selected_element = element
                    break

            if not self.selected_element:
                for element in self.levels[self.level].simulator.static_objs:
                    if element.rect.collidepoint(mouse_pos):
                        self.selected_element = element

                        if isinstance(element, Esteira) and element.editable:
                            self.count += 1
                        if self.count == 1:
                            element.sentido = -element.sentido
                            self.count = 0
                        break

            if not self.selected_element: #se nao encontrou no for anterior
                for element in self.levels[self.level].objbar.objects:
                    if element.rect.collidepoint(mouse_pos):
                        element.remove(self.levels[self.level].objbar.objects)
                        self.levels[self.level].simulator.add(element)
                        self.selected_element = element
                        break

            if not self.selected_element: #se nao encontrou no for anterior
                for element in self.levels[self.level].cmdbar.commands:
                    if element.rect.collidepoint(mouse_pos):
                        if isinstance(element, Play):
                            element.image = pygame.transform.flip(element.image,
                                                                  True, False)
                            self.playing = not self.playing
                            if not self.playing:
                                objs = self.levels[self.level].simulator.objects
                                for obj in objs:
                                    obj.speed = [0, 0]
                                    obj.rect.topleft = obj.initial_pos
                        elif isinstance(element, Help):
                            self.levels[self.level].show_help(self.screen)
                        elif isinstance(element, Quit):
                            sys.exit()
                        break

        else:
            if self.selected_element.editable and not self.playing:
                mouse_move = pygame.mouse.get_rel()
                if mouse_move != (0, 0):
                    self.count -= 1
                self.selected_element.rect.center = pygame.mouse.get_pos()
                new_pos = self.selected_element.rect.topleft
                self.selected_element.initial_pos = new_pos
            self.selected_element = None

    def show_congratulations(self):
        if self.play_sounds:
            pygame.mixer.stop()
            self.congrats_snd.play()

        self.screen.blit(self.congrats, (600 - self.congrats.get_width()/2,
                                         450 - self.congrats.get_height()/2) )
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def main_loop(self):
        self.menu.run()
        while self.running and self.level < len(self.levels):
            while not self.levels[self.level].goal_reached():
                self.event_handler()
                self.clock.tick(self.fps)
                self.update_screen(self.fps)
                self.levels[self.level].draw()

                if not self._showed_help:
                    self.levels[self.level].show_help(self.screen)
                    self._showed_help = True

                pygame.display.flip()

            self.playing = False
            self._showed_help = False
            self.level += 1
            self.show_congratulations()
            if (len(self.levels) == self.level) :
                self.running = False

