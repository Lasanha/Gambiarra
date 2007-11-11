# /gambiarra/gambiarra.py
#aqui fica o codigo do jogo em si

import pygame
from pygame.locals import *
import os
from levels import levels as Levels
from objects.wall import *

def check_collision(sprite_list, wall_list):
    new_objects = pygame.sprite.RenderPlain()
    for obj in sprite_list:
        obj.remove(sprite_list)
        obj.add(new_objects)

        for s in sprite_list:
            #TODO: verifica colisao de objetos dinamicos
            pass

        for w in wall_list:
            if obj.rect.colliderect(w.rect):
                if isinstance(w, DownWall):
                    obj.speed[1] = -0.7*obj.speed[1]
                    if obj.rect.bottom > w.rect.top:
                        obj.rect.bottom = w.rect.top - 1

                if isinstance(w, UpWall):
                    obj.speed[1] = -0.7*obj.speed[1]
                    if obj.rect.top < w.rect.bottom:
                        obj.rect.top = w.rect.bottom + 1

                if isinstance(w, LeftWall):
                    obj.speed[0] = -0.9*obj.speed[0]
                    if obj.rect.left < w.rect.right:
                        obj.rect.left = w.rect.right + 1

                if isinstance(w, RightWall):
                    obj.speed[0] = -0.9*obj.speed[0]
                    if obj.rect.right > w.rect.left:
                        obj.rect.right = w.rect.left - 1

    return new_objects

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
        objs = check_collision(self.allLevels[self.level].simulator.objects,
                               self.allLevels[self.level].simulator._walls)
        self.allLevels[self.level].simulator.objects = objs
        for obj in self.allLevels[self.level].simulator.objects:
            #obj eh um objeto na tela
            if obj.mobility:
                newpos = obj.rect.move((obj.speed[0],obj.speed[1]))
                obj.rect = newpos
                if obj.speed[0]:
                    obj.speed[0] *= 0.9
                else:
                    obj.speed[0] = 20
                obj.speed[1] += obj.gravity

    def start_window(self):
        #desenha a tela inicial (abstrato -chama os outros metodos predefinidos)
        pass
        
    def next_level(self):
        pass
        
    def mouse_event(self, mousePos, mouseButtonsPressed ):
        if mouseButtonsPressed[0]:
            #verificar colisao com thing
            #colidiu = verificar Colisao!!!
            collided = False
            #Pegar o objeto
            obj = None
            mouseMove = python.mouse.get_rel() 
            if collided:
                while mouseButtonsPressed[0]:
                    pass
                
                mouseMove = python.mouse.get_rel()
                #comentado porque por enquanto obj eh None
                #obj.rect = obj.rect.move(mouseMove)

    def main_loop(self):
        #loop principal
        #-definir e desenhar o nivel
        #-esperar por eventos do mouse:
        #   -clique sobre um thing, arrasta
        #   -clique sobre um botao
        
        #quando clicar em play transformar o botao em stop        
        playPressed = True
        if playPressed:
            while self.run:
                self.clock.tick(self.fps)
                self.update_screen(self.fps)
                self.allLevels[self.level].draw()
            
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        self.mouse_event( pygame.mouse.get_pos(), 
                                          pygame.mouse.get_pressed() )

def main():
    game = Game()

if __name__ == "__main__":
    main()
