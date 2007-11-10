# /gambiarra/objects/balls.py
# este arquivo contem a bola basica, outras sao derivadas desta

from os.path import abspath

import pygame

from objects.things import Thing

class BowlingBall(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(BowlingBall, self).__init__(
              pygame.image.load(abspath("../data/bolaBoliche.png")),
              editable, initialPosition, elasticity = 100, mobility = True,
              gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)
        
class BeachBall(Thing):
    def __init__(self, initialPosition=None, editable=True):
        super(BeachBall, self).__init__(
              pygame.image.load(abspath("../data/bola.png")), editable,
              initialPosition, elasticity = 100, mobility = True, gravity = 10)
        # TODO: substituir pela imagem correta
        #self.img = pygame.Surface((170, 170))
        #pygame.draw.circle(self.img, [0,10,0], (85, 85), 80)
