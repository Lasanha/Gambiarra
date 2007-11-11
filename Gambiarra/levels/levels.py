# /gambiarra/level.py
#arquivo que contem a lista de fases

import pygame
from objects.balls import *
from objects.animals import *
from objects.wall import *
from objects.esteira import *

class SimulationView(object):
    """ This widget holds the objects being simulated. """
    running = None
    background = None
    objects = None
    
    def __init__(self, objects):
        self.running = False
        self.background = pygame.Surface((1200, 770))
        self.background.fill([0,0,150])
        self.objects = pygame.sprite.RenderPlain(objects)
        self._walls = []
        self._walls.append(LeftWall())
        self._walls.append(RightWall())
        self._walls.append(UpWall())
        self._walls.append(DownWall())

    def draw(self, pos = None):
        screen = pygame.display.get_surface()
        if pos:
            screen.blit(self.background, (pos[0], pos[1]), pos)
        else:
            screen.blit(self.background, (0, 0))

        for wall in self._walls:
            wall.draw(screen, wall.rect)

        for item in self.objects:
            item.draw(screen, item.rect.topleft)

class ObjectBar(object):
    """ This widget contains the objects available for the problem. """

    def __init__(self, objects):
        self.background = pygame.Surface((1000, 130))
        self.background.fill([0,255,0])   #TODO: achar uma cor melhor =D
        self.objects = pygame.sprite.RenderPlain(objects)

    def draw(self, pos = None):
        screen = pygame.display.get_surface()
        if pos:
            screen.blit(self.background, (pos[0], 770 + pos[1]), pos)
        else:
            screen.blit(self.background, (0, 770))

        objpos = [0, 785]
        for item in self.objects:
            item.draw(screen, objpos)
            objpos[0] += item.image.get_width() + 15

    def update(self):
        pass

class CommandBar(object):
    """ This widget contains the commands: play, help, and quit. KISS! =D """

    def __init__(self):
        self.background = pygame.Surface((200, 130))
        self.width, self.height = self.background.get_size()
        self.background.fill([0,0,255])   #TODO: achar uma cor melhor =D
        
    def draw(self, pos=None):
        screen = pygame.display.get_surface()    
        if pos:
            screen.blit(self.background, (1000 + pos[0], 770 + pos[1]), pos)
        else:
            screen.blit(self.background, (1000, 770))

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
    level1ObjInPlace = [ BowlingBall((200,300)), BeachBall((100,100))]
    level1ObjToAdd = [ Penguin(), BeachBall() ]

    level2ObjInPlace = [ Penguin((300,600)), Esteira((20,650))]
    level2ObjToAdd = [ BeachBall(), Penguin(), BowlingBall() ]

    level3ObjInPlace = [ BowlingBall((200,700)), Penguin((500, 800))]
    level3ObjToAdd = [ Penguin(), BeachBall() ]

    level1 = Level( level1ObjInPlace, level1ObjToAdd )
    level2 = Level( level2ObjInPlace, level2ObjToAdd )
    level3 = Level( level3ObjInPlace, level3ObjToAdd )

    return [level1, level2, level3]