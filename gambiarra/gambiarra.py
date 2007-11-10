# /gambiarra/gambiarra.py
#aqui fica o codigo do jogo em si

import pygame
from pygame.locals import *
import os

class Gambiarra(object):
    screen = None
    screenSize = None
    run = None
    background = None
    level = None

    def __init__(self):
        pygame.init()
        actors = {}
        self.screen = pygame.display.set_mode((1200,900)) #omitindo flags
        self.screenSize = self.screen.get_size()
        self.background = pygame.Surface(self.screenSize)
        self.background.fill([255,0,0,])
        self.screen.blit(self.background, (0,0))
        self.run = True
        self.level = -1
        pygame.display.set_caption("Gambiarra")

        #carregar imagens?
        #vai carregar tudo de uma vez ou on demand?
        
        #inicia o loop
        self.main_loop()

    def event_handler(self):
        #verificar o evento e tomar as acoes
        pass

    def update_actors(self):
        #update dos elementos da tela
        pass

    def actors_clear(self):
        #retira ator da tela
        pass
        
    def actors_draw(self):
        #desenha ator na tela
        pass

    def start_window(self):
        #desenha a tela inicial (abstrato -chama os outros metodos predefinidos)
        pass

    def main_loop(self):
        #loop principal
        
        while self.run:
            pass

def main():
    game = Gambiarra()

if __name__ == "__main__":
    main()
