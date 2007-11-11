# gambiarra/gambiarra.py
#aqui fica o codigo do jogo em si

import pygame
from pygame.locals import *
import os
import levels as Levels
from objects.elastica import Elastica
from objects.esteira import Esteira
from objects.target import Target
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
            hitbox = obj.rect.inflate(5,5)
            if hitbox.colliderect(w.rect):
                if isinstance(w, DownWall):
                    if obj.rect.bottom > w.rect.top:
                       obj.rect.bottom = w.rect.top - 1
                       obj.speed[1] = -0.7*obj.speed[1]

                if isinstance(w, UpWall):
                    if obj.rect.top < w.rect.bottom:
                        obj.rect.top = w.rect.bottom + 1
                        obj.speed[1] = -0.7*obj.speed[1]

                if isinstance(w, LeftWall):
                    if obj.rect.left < w.rect.right:
                        obj.rect.left = w.rect.right + 1
                        obj.speed[0] = -0.9*obj.speed[1]

                if isinstance(w, RightWall):
                    if obj.rect.right > w.rect.left:
                        obj.rect.right = w.rect.left - 1
                        obj.speed[0] = -0.9*obj.speed[1]

                if isinstance(w, Esteira):
                     if (obj.rect.midbottom > w.rect.top and
                          obj.rect.bottom < w.rect.bottom):
                        obj.rect.bottom = w.rect.top
                        obj.speed[0] += w.sentido*3
                        obj.speed[1] = 0
                        
                if isinstance(w, Elastica):
                     if (obj.rect.midbottom > w.rect.top and
                          obj.rect.bottom < w.rect.bottom):
                        obj.rect.bottom = w.rect.top
                     obj.speed[1] *= -1.07

                if isinstance(w, Target):
                    pass 

    return new_objects


class Game(object):
    fps = 5
    screen = None
    screenSize = None
    playing = None
    run = None
    background = None
    clock = None
    level = 0
    levels = []
    action = []
    selected_element = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,900)) #omitindo flags
        self.screenSize = self.screen.get_size()
        pygame.display.flip()
        self.run = True
        self.playing = False
        pygame.display.set_caption("Gambiarra")
        self.clock = pygame.time.Clock()
        self.levels = Levels.init_levels()

        #inicia o loop
        self.main_loop()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                self.mouse_event( pygame.mouse.get_pos() )

    def update_screen(self, fps):
        #update dos elementos da tela
        if self.playing:
            # executa a simulacao
            objs = check_collision(self.levels[self.level].simulator.objects,
                                self.levels[self.level].simulator.staticObjs)
            self.levels[self.level].simulator.objects = objs
            for obj in self.levels[self.level].simulator.objects:
                #obj eh um objeto na tela
                if obj.mobility:
                    newpos = obj.rect.move((obj.speed[0],obj.speed[1]))
                    obj.rect = newpos
                    if obj.speed[0]:
                        obj.speed[0] *= 0.99
                    else:
                        obj.speed[0] = 20
                    obj.speed[1] += obj.gravity
        elif self.action:
            action = None

    def start_window(self):
        #desenha a tela inicial (abstrato -chama os outros metodos predefinidos)
        pass
        
    def next_level(self):
        pass
        
    def mouse_event(self, mousePos):
        if not self.selected_element:
            collided = False
            mouseMove = (0,0)
            mouseMove = pygame.mouse.get_rel()
            
            for element in self.levels[self.level].simulator.objects:
                if element.rect.collidepoint(mousePos):
                    print "COLIDIU PORRA", element
                    collided = True
                    self.selected_element = element
                    break
                    
            if not self.selected_element: #se nao encontrou no for anterior
                print "nao colidiu no simulador"
                for element in self.levels[self.level].objbar.objects:
                    if element.rect.collidepoint(mousePos):
                        print "COLIDIU PORRA", element
                        collided = True
                        self.selected_element = element
                        break
                        
            """if not self.selected_element: #se nao encontrou no for anterior
                for element in self.levels[self.level].cmdbar.commands:
                    if element.rect.collidepoint(mousePos):
                        print "COLIDIU PORRA", element
                        collided = True
                        self.selected_element = element
                        break"""
                
        else:
            mouseMove = pygame.mouse.get_rel()
            self.selected_element.rect = self.selected_element.rect.move(mouseMove)
            self.selected_element = None


    def main_loop(self):
        #quando clicar em play transformar o botao em stop
        while self.run:
            self.event_handler()
            self.clock.tick(self.fps)
            self.update_screen(self.fps)
            self.levels[self.level].draw()

            pygame.display.flip()


def main():
    game = Game()

if __name__ == "__main__":
    main()
