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

from things import Thing

class Elastica(Thing):

    def __init__(self, initial_pos = None, editable=True):
        if pygame.mixer.get_init():
            snd = pygame.mixer.Sound("data/snd/cama_elastica.wav")
        else:
            snd = None
        Thing.__init__(self,
              pygame.image.load("data/images/cama_elastica.png"),
              editable, snd,
              initial_pos, elasticity = 100, mobility = False,
              gravity = 10)

    def collide(self, obj):
        if obj.rect.colliderect(self.rect):
            if (obj.rect.bottom >= self.rect.top and obj.speed[1] > 0):
                obj.rect.bottom = self.rect.top - 1
            elif (obj.rect.top <= self.rect.bottom):
                obj.rect.top = self.rect.bottom + 1
            obj.speed[1] *= -0.99
            return True
        return False

