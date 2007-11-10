# /gambiarra/objects/things.py
# classe mais abstrata para "coisas" na tela

class Thing(object):
    img = None
    initialPosition = None
    mobility = None
    editable = None
    speed = None
    gravity = None
    elasticity = None # * 1%, from 0 up to 100
    
    def __init__(self, image, editable, initialPosition=None, elasticity = 100,
                 mobility = False, gravity = 10 ):
        self.img = image
        if initialPosition:
            self.initialPosition = initialPosition
        self.elasticity = elasticity
        self.editable = editable
        self.speed = [0,0]
        self.mobility = mobility
        self.gravity = gravity

    def draw(self, screen, pos ):
        # temos a imagem na variavel <img> e
        # o 'zero' (ponto onde deve ser desenhado <pos>
        screen.blit(self.img, (pos[0],pos[1]))

    def collision(self):
        """Verifies if the animal has hit the floor, the ceil or any wall"""
        
        #the floor
        centerBottom = self.centerPosition[1] + (self.heigth / 2)
        if centerBottom >= 700:
            # touched the floor, STOP!
            self.speed[0] = 0
            self.speed[1] = 0
            
            #self.speed[1] = - ( self.elasticity / 100 ) * self.speed[1]


        #the ceil
        centerTop = self.centerPosition[1] - (self.heigth / 2)
        if centerTop <= 0:
            # touched the ceil, STOP!
            self.speed[0] = 0
            self.speed[1] = 0
            
            #self.speed[1] = - ( self.elasticity / 100 ) * self.speed[1]
        
        #left wall
        centerLeft = self.centerPosition[0] - (self.heigth / 2)
        if centerLeft <= 0:
            #tocou a parede esquerda, para
            self.speed[0] = 0
            self.speed[1] = 0
            
            #self.speed[0] = - ( self.elasticity / 100 ) * self.speed[0]
            
            #right wall
        centerRight = self.centerPosition[0] + (heigth / 2)
        if centerRight >= 1200:
            #tocou a parede direita, para
            self.speed[0] = 0
            self.speed[1] = 0
                
            #self.speed[0] = - ( self.elasticity / 100 ) * self.speed[0]


