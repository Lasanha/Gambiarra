# gambiarra/objects/animals.py

import pygame

from things import Thing

from os.path import abspath

class Penguin(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(Penguin, self).__init__(
              pygame.image.load(abspath("../data/images/penguin.png")),
              editable, initialPosition, elasticity = 100, mobility = True,
              gravity = 1)
