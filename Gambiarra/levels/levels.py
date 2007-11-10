# /gambiarra/level.py
#arquivo que contem a lista de fases

import pygame

class ObjectBar(object):
    """ This widget contains the objects available for the problem. """

    def __init__(self):
        self.background = pygame.Surface((1000, 200))
        self.background.fill([0,255,0])   #TODO: achar uma cor melhor =D

    def draw(self, pos=None):
        screen = pygame.display.get_surface()
        if pos:
            screen.blit(self.background, (pos[0], 700 + pos[1]), pos)
        else:
            screen.blit(self.background, (0, 700))

    def update(self):
        pass

class CommandBar(object):
    """ This widget contains the commands: play, help, and quit. KISS! =D """

    def __init__(self):
        self.background = pygame.Surface((200, 200))
        self.width, self.height = self.background.get_size()
        self.background.fill([0,0,255])   #TODO: achar uma cor melhor =D
        
    def draw(self, pos=None):
        screen = pygame.display.get_surface()    
        if pos:
            screen.blit(self.background, (1000 + pos[0], 700 + pos[1]), pos)
        else:
            screen.blit(self.background, (1000, 700))

    def update(self):
        pass

class Level(object):
    """This widget contains the objects in the scenario and their positions
    on the screen"""
    objects = None

    def __init__(self, objectList):
        self.objects = objectList
        self.objbar = ObjectBar()
        self.cmdbar = CommandBar()

    def draw(self):
        self.objbar.draw()
        self.cmdbar.draw()


#Sample levels
level1Objects = [ ("BowlingBall", 200, 300), ("BeachBall", 400, 800)]
level2Objects = [ ("Penguin", 300, 600)]
level3Objects = [ ("BowlingBall", 200, 700), ("Penguin", 500, 800)]

level1 = Level( level1Objects )
level2 = Level( level2Objects )
level3 = Level( level3Objects )