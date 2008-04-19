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

import os.path

import pygame

class GameMenu(object):
    screen = None
    background = None
#    level = None
    start = None

    def __init__(self):
#        pygame.init()
#        pygame.display.set_mode((1280,800))
        self.screen = pygame.display.get_surface()
        bg_file = os.path.join("data", "images", "background.png")
        self.background = pygame.image.load(bg_file)
        # mudar o arquivo de logotipo
#        self.level = LevelButton(350)
        self.start = StartButton(520)

    def run(self):
        self.screen.blit(self.background, (0, 0))
#        self.level.draw(self.screen)
        self.start.draw(self.screen)
        pygame.display.flip()
        while (True):
            event = self.event_handler()
            if ( event == pygame.MOUSEMOTION ):
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.background, (0, 0))
#                self.level.draw(self.screen)
                self.start.draw(self.screen)
                pygame.display.flip()
            if ( event == pygame.MOUSEBUTTONUP ) :
                if self.start.clicked:
                    return
#                if self.level.clicked:
#                    self.screen.fill((0,0,0))
#                    self.screen.blit(self.background, (0,0))
#                    self.level.draw(self.screen)
#                    self.start.draw(self.screen)
#                    pygame.display.flip()
#                    self.level.clicked = False

    def event_handler(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    img = self.start.current_img
                    rect = img.get_rect(topleft = self.start.position)
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        if self.start.current == 0 :
#                            if self.level.current == 1:
#                                self.level.current = 0
#                                self.level.current_img = self.level.img[0]
                            self.start.current = 1
                            self.start.current_img = self.start.img[1]
                            return pygame.MOUSEMOTION
#                    img = self.level.current_img
#                    rect = img.get_rect(topleft = self.level.position)
#                    elif rect.collidepoint(pygame.mouse.get_pos()):
#                        if self.level.current == 0 :
#                            if self.start.current == 1:
#                                self.start.current = 0
#                                self.start.current_img = self.start.img[0]
#                            self.level.current = 1
#                            self.level.current_img = self.level.img[1]
#                            return MOUSEMOTION
#                    elif self.level.current == 1 or self.start.current == 1 :
                    elif self.start.current == 1 :
                        if self.start.current == 1 :
                            self.start.current = 0
                            self.start.current_img = self.start.img[0]
#                        else:
#                            self.level.current = 0
#                            self.level.current_img = self.level.img[0]
                        return pygame.MOUSEMOTION
                if event.type == pygame.MOUSEBUTTONUP:
                    if (self.start.current_img.get_rect(
                            topleft = self.start.position).collidepoint(
                                                        pygame.mouse.get_pos())
                        and self.start.current == 1):
                        self.start.click()
                        return pygame.MOUSEBUTTONUP
#                    elif (self.level.current_img.get_rect(
#                            topleft = self.level.position).collidepoint(
#                                                        pygame.mouse.get_pos())
#                        and self.level.current == 1):
#                        self.level.click()
#                        return pygame.MOUSEBUTTONUP


class LevelButton(object):
    img = None
    position = None
    level = None
    current = None
    current_img = None
    levels_number = None
    current_level_img = None
    clicked = None

    def __init__(self, position, levels_number = 1):
        img = os.path.join("data", "images", "nivel_normal.png")
        non_hover = pygame.image.load(img)
        img = os.path.join("data", "images", "nivel_hover.png")
        hover = pygame.image.load(img)
        self.img = [non_hover, hover]
        self.position = [600 - non_hover.get_width()/2, position]
        self.level = 0
        self.current = 0
        self.current_img = self.img[self.current]
        self.levels_number = levels_number
        self.current_level_img = None # Precisa 'renderizar' o numero do nivel
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.current_img, self.position)

    def click(self):
        self.clicked = True
        self.level += 1
        if self.level == self.levels_number :
            self.level = 0

class StartButton(object):
    img = None
    position = None
    current = None
    current_img = None
    clicked = None

    def __init__(self, position):
        img = os.path.join("data", "images", "iniciar_normal.png")
        non_hover = pygame.image.load(img)
        img = os.path.join("data", "images", "iniciar_hover.png")
        hover = pygame.image.load(img)
        self.img = [non_hover, hover]
        self.position = [600 - non_hover.get_width()/2 - 50, position]
        self.current = 0
        self.current_img = self.img[self.current]
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.current_img, self.position)

    def click(self):
        self.clicked = True
