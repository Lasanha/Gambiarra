# gambiarra/command.py

from os.path import abspath

import pygame

class Command(object):
    image = None
    
    def __init__(self, img):
        self.image = img

    def draw(self, screen, pos):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.image, (pos[0],pos[1]))

class Play(Command):
    def __init__(self):
        super(Play, self).__init__( pygame.image.load(
                                    abspath("../data/images/playButton.png") ) )

class Help(Command):
    def __init__(self):
        super(Help, self).__init__( pygame.image.load( 
                                    abspath("../data/images/helpButton.png") ) )

class Quit(Command):
    def __init__(self):
        super(Quit, self).__init__( pygame.image.load( 
                                    abspath("../data/images/quitButton.png") ) )
