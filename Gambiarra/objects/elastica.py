# gambiarra/elastica.py

from os.path import abspath

import pygame

from things import Thing

class Elastica(Thing):

    def __init__(self, initialPosition = [0,0], editable=False):
        super(Elastica, self).__init__(
              pygame.image.load(abspath("../data/images/cama_elastica.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
