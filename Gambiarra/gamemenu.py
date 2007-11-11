# gambiarra/gamemenu.py

import pygame
from pygame.locals import *

from os.path import abspath

class GameMenu(object):
    screen = None
    background = None
    level = None
    start = None
    
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280,800))
        self.screen = pygame.display.get_surface()
        self.background = pygame.image.load(abspath("../data/images/iniciar_normal.png"))
        # mudar o arquivo de logotipo
        self.level = LevelButton([400,350])
        self.start = StartButton([400,600])

    def run(self):
        self.screen.blit(self.background, (0,0))
        self.level.draw(self.screen)
        self.start.draw(self.screen)
        pygame.display.flip()
        while (True):
            pos = pygame.mouse.get_pos()
            print pos
            event = self.event_handler()
            if ( event == MOUSEMOTION ):
                self.screen.fill((0,0,0))
                self.screen.blit(self.background, (0,0))
                self.level.draw(self.screen)
                self.start.draw(self.screen)
                pygame.display.flip()

    def event_handler(self):
        validEventFound = False
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    if self.level.current_img.get_rect(topleft = self.level.position).collidepoint(pygame.mouse.get_pos()):
                        if self.level.current == 0 :
                            if self.start.current == 1:
                                self.start.current = 0
                                self.start.current_img = self.start.img[self.start.current]
                            self.level.current = 1
                            self.level.current_img = self.level.img[self.level.current]
                            return MOUSEMOTION
                    elif self.start.current_img.get_rect(topleft = self.start.position).collidepoint(pygame.mouse.get_pos()):
                        if self.start.current == 0 :
                            if self.level.current == 1:
                                self.level.current = 0
                                self.level.current_img = self.level.img[self.level.current]
                            self.start.current = 1
                            self.start.current_img = self.start.img[self.start.current]
                            return MOUSEMOTION
                    elif self.level.current == 1 or self.start.current == 1 :
                        if self.level.current == 1 :
                            self.level.current = 0
                            self.level.current_img = self.level.img[self.level.current]
                        else:
                            self.start.current = 0
                            self.start.current_img = self.start.img[self.start.current]
                        return MOUSEMOTION

class LevelButton(object):
    img = None
    position = None
    level = None
    current = None
    current_img = None
    
    def __init__(self, position):
        nonHover = pygame.image.load(abspath("../data/images/nivel_normal.png"))
        hover = pygame.image.load(abspath("../data/images/nivel_hover.png"))
        self.img = [nonHover,hover]
        self.position = position
        self.level = 0
        self.current = 0
        self.current_img = self.img[self.current]
    
    def draw(self, screen):
        screen.blit(self.current_img, self.position)
        
    def click(self):
        pass
    
class StartButton(object):
    img = None
    position = None
    current = None
    current_img = None
    
    def __init__(self, position):
        nonHover=pygame.image.load(abspath("../data/images/iniciar_normal.png"))
        hover = pygame.image.load(abspath("../data/images/iniciar_hover.png"))
        self.img = [nonHover,hover]
        self.position = position
        self.current = 0
        self.current_img = self.img[self.current]
        
    def draw(self, screen):
        screen.blit(self.current_img, self.position)
    
    def click(self):
        pass