# gambiarra/gamemenu.py

import pygame

from os.path import abspath

class GameMenu(object):
    background = None
    screen = None
    logo = None
    iniciar = None
    
    def __init__(self):
        self.background = pygame.Surface((1200,900))
        self.background.fill((255,0,255))
        self.screen = pygame.display.get_surface()
        self.logo = pygame.image.load(abspath("../data/images/penguin.png"))
        # mudar o arquivo de logotipo
        self.iniciar = pygame.image.load(abspath("../data/images/iniciar_normal.png"))
