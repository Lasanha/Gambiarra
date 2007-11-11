# gambiarra/objects/things.py
# classe mais abstrata para "coisas" na tela

import pygame

class Thing(pygame.sprite.Sprite):

    img = None
    initialPosition = None
    mobility = None
    editable = None
    speed = None
    gravity = None
    elasticity = None # * 1%, from 0 up to 100
    
    def __init__(self, image, editable, initialPosition=None, elasticity = 100,
                 mobility = False, gravity = 10 ):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image = image
        self.rect = image.get_rect()
        
        if initialPosition:
            self.initialPosition = initialPosition
            self.rect.topleft = initialPosition[0], initialPosition[1]
        self.elasticity = elasticity
        self.editable = editable
        self.speed = [0,0]
        self.mobility = mobility
        self.gravity = gravity

    def draw(self, screen, pos ):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.image, (pos[0],pos[1]))

    def collision(self):
        pass