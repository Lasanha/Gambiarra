# gambiarra/objects/wall.py
# este arquivo contem a bola basica, outras sao derivadas desta

from os.path import abspath

import pygame

from things import Thing

class LeftWall(Thing):
    def __init__(self, initialPosition = [0,0], editable=False):
        super(LeftWall, self).__init__(
              pygame.image.load(abspath("../data/images/leftwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        
class RightWall(Thing):
    def __init__(self, initialPosition = [1185,0], editable=False):
        super(RightWall, self).__init__(
              pygame.image.load(abspath("../data/images/rightwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)

class UpWall(Thing):
    def __init__(self, initialPosition = [15,0], editable=False):
        super(UpWall, self).__init__(
              pygame.image.load(abspath("../data/images/upwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)

class DownWall(Thing):
    def __init__(self, initialPosition = [15,755], editable=False):
        super(DownWall, self).__init__(
              pygame.image.load(abspath("../data/images/downwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
