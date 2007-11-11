# /gambiarra/level.py
#arquivo que contem a lista de fases

import pygame
from objects.balls import *
from objects.animals import *
from objects.wall import *

class SimulationView(object):
    """ This widget holds the objects being simulated. """
    running = None
    background = None
    objects = None
    
    def __init__(self, objects):
        self.running = False
        self.background = pygame.Surface((1200, 700))
        self.background.fill([0,0,150])
        self.objects = pygame.sprite.RenderPlain(objects)
        LeftWall().add(self.objects)
        RightWall().add(self.objects)
        UpWall().add(self.objects)
        DownWall().add(self.objects)

    def draw(self, pos = None):
        screen = pygame.display.get_surface()
        if pos:
            screen.blit(self.background, (pos[0], pos[1]), pos)
        else:
            screen.blit(self.background, (0, 0))

        for item in self.objects:
            item.draw(screen, item.rect.topleft)

class ObjectBar(object):
    """ This widget contains the objects available for the problem. """

    def __init__(self, objects):
        self.background = pygame.Surface((1000, 200))
        self.background.fill([0,255,0])   #TODO: achar uma cor melhor =D
        self.objects = pygame.sprite.RenderPlain(objects)

    def draw(self, pos = None):
        screen = pygame.display.get_surface()
        if pos:
            screen.blit(self.background, (pos[0], 700 + pos[1]), pos)
        else:
            screen.blit(self.background, (0, 700))

        objpos = [0,715]
        for item in self.objects:
            item.draw(screen, objpos)
            objpos[0] += item.image.get_width() + 15

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

    def __init__(self, objInPlace, objToAdd):
        self.simulator = SimulationView(objInPlace)
        self.objbar = ObjectBar(objToAdd)
        self.cmdbar = CommandBar()

    def draw(self):
        self.simulator.draw()
        self.objbar.draw()
        self.cmdbar.draw()


def init_levels():
    #FIXME: fazer de um jeito menos lusitano
    #Sample levels
    level1ObjInPlace = [ BowlingBall((200,300)), BeachBall((400,800))]
    level1ObjToAdd = [ Penguin(), BeachBall() ]

    level2ObjInPlace = [ Penguin((300,600))]
    level2ObjToAdd = [ BeachBall(), Penguin(), BowlingBall() ]

    level3ObjInPlace = [ BowlingBall((200,700)), Penguin((500, 800))]
    level3ObjToAdd = [ Penguin(), BeachBall() ]

    level1 = Level( level1ObjInPlace, level1ObjToAdd )
    level2 = Level( level2ObjInPlace, level2ObjToAdd )
    level3 = Level( level3ObjInPlace, level3ObjToAdd )

    return [level1, level2, level3]