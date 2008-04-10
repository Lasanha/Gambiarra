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

from things import Thing

class Esteira(Thing):

    sentido = None

    def __init__(self, initialPosition = [0,0], editable=True):
        super(Esteira, self).__init__(
              pygame.image.load(abspath("data/images/esteira_dir.png")),
              editable, None,
              initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        self.sentido = 1
        self.image_dir = pygame.image.load(
                            abspath("data/images/esteira_dir.png"))
        self.image_esq = pygame.image.load(
                            abspath("data/images/esteira_esq.png"))

    def draw(self, screen, pos):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        if self.sentido == 1:
            screen.blit(self.image_dir, (pos[0],pos[1]))
        elif self.sentido == -1:
            screen.blit(self.image_esq, (pos[0],pos[1]))

    def collide(self, obj):
        if obj.rect.colliderect(self.rect):
            if (obj.rect.bottom >= self.rect.top and obj.speed[1] > 0):
                obj.rect.bottom = self.rect.top - 5
            obj.speed[0] = self.sentido*15
            obj.speed[1] *= -0.75*obj.elasticity/100
            return True
        return False

