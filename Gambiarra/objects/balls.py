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

from things import Thing

class BowlingBall(Thing):
    def __init__(self, initial_pos=None, editable=True):
        if pygame.mixer.get_init():
            snd = pygame.mixer.Sound(os.path.join("data", "snd",
                                                  "BowlingBall.wav"))
        else:
            snd = None
        Thing.__init__(self,
              pygame.image.load(os.path.join("data", "images",
                                             "bolaBoliche.png")),
              editable, snd,
              initial_pos, elasticity = 60, mobility = True, gravity = 5)

class BeachBall(Thing):
    def __init__(self, initial_pos=None, editable=True):
        if pygame.mixer.get_init():
            snd = pygame.mixer.Sound(os.path.join("data", "snd",
                                                  "BowlingBall.wav"))
        else:
            snd = None
        Thing.__init__(self,
              pygame.image.load(os.path.join("data", "images", "bola.png")),
              editable, snd,
              initial_pos, elasticity = 90, mobility = True, gravity = 5)

class SoccerBall(Thing):
    def __init__(self, initial_pos=None, editable=True):
        if pygame.mixer.get_init():
            snd = pygame.mixer.Sound(os.path.join("data", "snd",
                                                  "BowlingBall.wav"))
        else:
            snd = None
        Thing.__init__(self,
              pygame.image.load(os.path.join("data", "images", "futebol.png")),
              editable, snd,
              initial_pos, elasticity = 70, mobility = True,
              gravity = 5)
