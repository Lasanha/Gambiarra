# /gambiarra/objects/balls.py
# este arquivo contem a bola basica, outras sao derivadas desta

from os.path import abspath

import pygame

from objects.things import Thing

class LeftWall(Thing):
    def __init__(self, initialPosition = [0,0], editable=False):
        super(LeftWall, self).__init__(
              pygame.image.load(abspath("../data/leftwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)
        
class RightWall(Thing):
    def __init__(self, initialPosition = [1185,0], editable=False):
        super(RightWall, self).__init__(
              pygame.image.load(abspath("../data/rightwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)

class UpWall(Thing):
    def __init__(self, initialPosition = [15,0], editable=False):
        super(UpWall, self).__init__(
              pygame.image.load(abspath("../data/upwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)

class DownWall(Thing):
    def __init__(self, initialPosition = [15,755], editable=False):
        super(DownWall, self).__init__(
              pygame.image.load(abspath("../data/downwall.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)
