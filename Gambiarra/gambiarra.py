# /gambiarra/gambiarra.py
#aqui fica o codigo do jogo em si

import pygame
from pygame.locals import *
import os
from levels import levels as Levels
from objects.wall import *

class Game(object):
    fps = 30
    screen = None
    screenSize = None
    run = None
    background = None
    clock = None
    level = 0
    allLevels = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,900)) #omitindo flags
        self.screenSize = self.screen.get_size()
        pygame.display.flip()
        self.run = True
        pygame.display.set_caption("Gambiarra")
        self.clock = pygame.time.Clock()
        self.allLevels = Levels.init_levels()

        #inicia o loop
        self.main_loop()

    def event_handler(self):
        #verificar o evento e tomar as acoes
        pass

    def update_screen(self, fps):
        #update dos elementos da tela
        self.check_collision()
        for obj in self.allLevels[self.level].simulator.objects:
            #obj eh um objeto na tela
            if obj.mobility:
                newpos = obj.rect.move((obj.speed[0],obj.speed[1]))
                obj.rect = newpos
                obj.speed[0] *= 0.9
                obj.speed[1] += obj.gravity

    def check_collision(self):
        for obj in self.allLevels[self.level].simulator.objects:
            obj.remove(self.allLevels[self.level].simulator.objects)
            collision = pygame.sprite.spritecollide(obj, 
                               self.allLevels[self.level].simulator.objects, 0)
            obj.add(self.allLevels[self.level].simulator.objects)
            if collision != []:
                if isinstance(collision[0],DownWall):
                    obj.speed[1] =- obj.speed[1]

    def actors_clear(self):
        #retira ator da tela
        pass
        
    def actors_draw(self):
        #desenha ator na tela
        pass

    def start_window(self):
        #desenha a tela inicial (abstrato -chama os outros metodos predefinidos)
        pass
        
    def next_level(self):
        pass

    def main_loop(self):
        #loop principal
        
        while self.run:
            self.clock.tick(self.fps)
            self.update_screen(self.fps)
            self.allLevels[self.level].draw()
            
            pygame.display.flip()

def main():
    game = Game()

if __name__ == "__main__":
    main()
