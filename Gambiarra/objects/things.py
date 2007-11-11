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

import pygame

class Thing(pygame.sprite.Sprite):

    img = None
    initialPosition = None
    mobility = None
    editable = None
    speed = None
    gravity = None
    elasticity = None # * 1%, from 0 up to 100
    
    def __init__(self, image, editable, initialPosition=None,
                 elasticity = 100, mobility = False, gravity = 10 ):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image = image
        self.rect = image.get_rect()
        
        if initialPosition:
            self.initialPosition = initialPosition
            self.rect.topleft = initialPosition[0], initialPosition[1]
        self.elasticity = elasticity
        self.editable = editable
        self.speed = [0,0]
        self.mobility = mobility
        self.gravity = gravity

    def draw(self, screen, pos ):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.image, (pos[0],pos[1]))

    def collision(self):
        pass