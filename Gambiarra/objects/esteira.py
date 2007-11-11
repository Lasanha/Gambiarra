# gambiarra/esteira.py

from os.path import abspath

import pygame

from things import Thing

class Esteira(Thing):
    def __init__(self, initialPosition = [0,0], editable=False):
        super(Esteira, self).__init__(
              pygame.image.load(abspath("../data/images/esteira.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)