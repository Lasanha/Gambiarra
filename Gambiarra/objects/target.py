# gambiarra/target.py

from os.path import abspath

import pygame

from things import Thing

class Target(Thing):
    def __init__(self, initialPosition = [0,0], editable=False):
        super(Target, self).__init__(
              pygame.image.load(abspath("../data/images/target.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)