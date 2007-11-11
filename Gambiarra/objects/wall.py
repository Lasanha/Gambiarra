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

from things import Thing, NoSound

class LeftWall(Thing):
    def __init__(self, initialPosition = [0,0], editable=False):
        super(LeftWall, self).__init__(
           pygame.image.load(abspath("../data/images/leftwall.png")),
           editable, NoSound(),
           initialPosition, elasticity = 100, mobility = False, gravity = 10)
        
class RightWall(Thing):
    def __init__(self, initialPosition = [1185,0], editable=False):
        super(RightWall, self).__init__(
           pygame.image.load(abspath("../data/images/rightwall.png")),
           editable, NoSound(),
           initialPosition, elasticity = 100, mobility = False, gravity = 10)

class UpWall(Thing):
    def __init__(self, initialPosition = [15,0], editable=False):
        super(UpWall, self).__init__(
            pygame.image.load(abspath("../data/images/upwall.png")),
            editable, NoSound(),
            initialPosition, elasticity = 100, mobility = False,
            gravity = 10)

class DownWall(Thing):
    def __init__(self, initialPosition = [15,755], editable=False):
        super(DownWall, self).__init__(
            pygame.image.load(abspath("../data/images/downwall.png")),
            editable, NoSound(),
            initialPosition, elasticity = 100, mobility = False,
            gravity = 10)
