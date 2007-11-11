# gambiarra/esteira.py

from os.path import abspath

import pygame

from things import Thing

class Esteira(Thing):

    sentido = None

    def __init__(self, initialPosition = [0,0], editable=False):
        super(Esteira, self).__init__(
              pygame.image.load(abspath("../data/images/esteira_dir.png")),
              editable, initialPosition, elasticity = 100, mobility = False,
              gravity = 10)
        self.sentido = 1
        self.image_dir = pygame.image.load(
                                      abspath("../data/images/esteira_dir.png"))
        self.image_esq = pygame.image.load(
                                      abspath("../data/images/esteira_esq.png"))

    def draw(self, screen, pos):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        if self.sentido == 1:
            screen.blit(self.image_dir, (pos[0],pos[1]))
        elif self.sentido == -1:
            screen.blit(self.image_esq, (pos[0],pos[1]))
