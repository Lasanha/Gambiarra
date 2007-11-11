# /gambiarra/objects/animals.py

# Peguin original art from:
# http://www.flickr.com/photos/katmere/62037353/
# Updated at November 10th, 2005.
# Published under Creative Commons Attribution 2.0 Generic.

import pygame

from objects.things import Thing

from os.path import abspath

class Penguin(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(Penguin, self).__init__(
              pygame.image.load(abspath("../data/penguin.png")),
              editable, initialPosition, elasticity = 100, mobility = True,
              gravity = 1)
