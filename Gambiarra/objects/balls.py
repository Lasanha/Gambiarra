# /gambiarra/objects/level.py
# este arquivo contem a bola basica, outras sao derivadas desta

class Ball(object):
    img = None
    width = 0
    heigth = 0
    centerPosition = [0,0]
    
    def __init__(self):
        self.width = 0
        self.height = 0
        centerPosition = [0,0]
        pass
        
    def collision(self):
        """Verifies if the ball has hit the floor, the ceil or any wall"""
        
        #the floor
        centerBottom = centerPosition[1] + (heigth / 2)
        if centerBottom >= 700:
            #tocou o chao
            pass
        
        #the ceil
        centerTop = centerPosition[1] - (heigth / 2)
        if centerTop <= 0:
            #tocou o teto
            pass
        
        #left wall
        centerLeft = centerPosition[0] - (heigth / 2)
        if centerLeft <= 0:
            #tocou a parede esquerda
            pass
            
        #right wall
        centerRight = centerPosition[0] + (heigth / 2)
        if centerRight >= 1200:
            #tocou a parede direita
            pass
        
    def collision(self, obj):
        """Verifies collision with another object"""
        pass
        
        
    def draw(self,screen,position):
        screen.blit(self.img, position)

class BowlingBall(Ball):
    def __init__(self):
        super(BowlingBall, self).__init__()
        
        
class BeachBall(Ball):
    def __init__(self):
        super(BeachBall, self).__init__()

