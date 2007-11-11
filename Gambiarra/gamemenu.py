# gambiarra/gamemenu.py

import pygame

from os.path import abspath

class GameMenu(object):
    screen = None
    background = None
    level = None
    start = None
    
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.background = pygame.image.load(abspath("./data/images/iniciar_normal.png"))
        # mudar o arquivo de logotipo
        self.level = LevelButton([0,0])
        self.start = StartButton([400,400])
        
    def run(self):
        pos = None
        self.screen = pygame.display.get_surface()
        self.screen.blit(background, (0,0))
        level.draw()
        start.draw()
        while (True):
            pos = pygame.mouse.get_pos()
            if (level.check_hover(pos) or start.check_hover(pos)):
                self.screen.blit(background, (0,0))
                level.draw()
                start.draw()
        pass

class LevelButton(object):
    img = None
    position = None
    level = None
    current_img = None
    
    def __init__(self, position):
        nonHover = pygame.image.load(abspath("./data/images/nivel_normal.png"))
        hover = pygame.image.load(abspath("./data/images/nivel_hover.png"))
        self.img = [nonHover,hover]
        self.position = position
        self.level = 0
        self.current_img = self.img[0]
    
    def check_hover(self, pos):
        hover = self.current_img.get_rect().collidepoint(pos)
        if (hover and self.current == 0) :
            self.current = 1
            self.current_img = self.img[self.current]
        if (not hover and self.current == 1) :
            self.current = 0
            self.current_img = self.img[self.current]
        return hover
    
    def draw(self, screen):
        screen.blit(self.current_img, self.position)
    
class StartButton(object):
    img = None
    position = None
    current = None
    current_img = None
    
    def __init__(self, position):
        nonHover=pygame.image.load(abspath("./data/images/iniciar_normal.png"))
        hover = pygame.image.load(abspath("./data/images/iniciar_hover.png"))
        self.img = [nonHover,hover]
        self.position = position
        self.current = 0
        self.current_img = self.img[self.current]
    
    def check_hover(self, pos):
        hover = self.current_img.get_rect().collidepoint(pos)
        if (hover and self.current == 0) :
            self.current = 1
            self.current_img = self.img[self.current]
        if (not hover and self.current == 1) :
            self.current = 0
            self.current_img = self.img[self.current]
        return hover
        
    def draw(self, screen):
        screen.blit(self.current_img, self.position)