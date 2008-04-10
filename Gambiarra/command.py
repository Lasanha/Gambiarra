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

from os.path import abspath

import pygame

class Command(pygame.sprite.Sprite):
    image = None

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()

    def draw(self, screen, pos):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.image, (pos[0],pos[1]))

class Play(Command):
    def __init__(self):
        super(Play, self).__init__( pygame.image.load(
                          abspath("data/images/playButton.png") ) )

class Help(Command):
    def __init__(self):
        super(Help, self).__init__( pygame.image.load(
                          abspath("data/images/helpButton.png") ) )

class Quit(Command):
    def __init__(self):
        super(Quit, self).__init__( pygame.image.load(
                          abspath("data/images/quitButton.png") ) )
