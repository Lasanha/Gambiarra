# gambiarra/gambiarra.py
#aqui fica o codigo do jogo em si

import pygame
from pygame.locals import *
import os
import levels as Levels
from objects.wall import *
from objects.target import Target
from objects.esteira import Esteira

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
                        obj.speed[1] = -0.9*obj.speed[1]

                if isinstance(w, RightWall):
                    if obj.rect.right > w.rect.left:
                        obj.rect.right = w.rect.left - 1
                        obj.speed[1] = -0.9*obj.speed[1]

                if isinstance(w, Esteira):
                     if (obj.rect.midbottom > w.rect.top and
                          obj.rect.bottom < w.rect.bottom):
                        obj.rect.bottom = w.rect.top
                        obj.speed[0] += w.sentido*3
                        obj.speed[1] = 0

                if isinstance(w, Target):
                    pass 

    return new_objects


class Game(object):
    fps = 30
    screen = None
    screenSize = None
    playing = None
    run = None
    background = None
    clock = None
    level = 0
    levels = []
    action = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,900)) #omitindo flags
        self.screenSize = self.screen.get_size()
        pygame.display.flip()
        self.run = True
        self.playing = True
        pygame.display.set_caption("Gambiarra")
        self.clock = pygame.time.Clock()
        self.levels = Levels.init_levels()

        #inicia o loop
        self.main_loop()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                self.mouse_event( pygame.mouse.get_pos(), 
                                  pygame.mouse.get_pressed() )

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
                        obj.speed[0] *= 0.9
                    else:
                        obj.speed[0] = 20
                    obj.speed[1] += obj.gravity
        elif self.action:
            # movimenta elementos na tela
            if self.action[0] == "nothing":
                self.action = []
            elif self.action[0] == "move thing":
                print "vai mover..."
                self.action[1].rect = self.action[1].rect.move(self.action[2])
                self.action = []
            elif self.action[0] == "command":
                self.action = []


    def start_window(self):
        #desenha a tela inicial (abstrato -chama os outros metodos predefinidos)
        pass
        
    def next_level(self):
        pass
        
    def mouse_event(self, mousePos, mouseButtonsPressed ):
        if mouseButtonsPressed[0]:
            collidedThing = False
            collidedCommand = False
            dragging = None
            mouseMove = pygame.mouse.get_rel()
            print "botao esquerdo pressionado"
            
            for obj in self.levels[self.level].simulator.objects:
                if obj.rect.collidepoint(mousePos):
                    if obj.editable:
                        collidedThing = True
                    break

            for obj in self.levels[self.level].objbar.objects:
                if obj.rect.collidepoint(mousePos):
                    print "colidiu barra"
                    collidedThing = True
                    break

            for obj in self.levels[self.level].objbar.objects:
                if obj.rect.collidepoint(mousePos):
                    print "colidiu comando"
                    collidedCommand = True
                    break
            
            if collidedThing:
                #esperar outro clique
                destiny = False
                while not destiny:
                    for evt in pygame.event.get():
                        if evt.type == MOUSEBUTTONDOWN:
                            print "destino clicado"
                            destiny = True
                
                mouseMove = pygame.mouse.get_rel()
                if obj:
                    self.action = [ "move thing", obj, mouseMove ]
             
            elif collidedCommand:
                if obj:
                    self.action = [ "command", obj ]
                    
            else:
                self.action = [ "nothing" ]

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
