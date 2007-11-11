# gambiarra/objects/balls.py
# este arquivo contem a bola basica, outras sao derivadas desta

from os.path import abspath

import pygame

from things import Thing

class BowlingBall(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(BowlingBall, self).__init__(
              pygame.image.load(abspath("../data/images/bolaBoliche.png")),
              editable, initialPosition, elasticity = 100, mobility = True,
              gravity = 10)

class BeachBall(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(BeachBall, self).__init__(
              pygame.image.load(abspath("../data/images/bola.png")),
              editable, initialPosition, elasticity = 100, mobility = True,
              gravity = 10)
