# /gambiarra/objects/animals.py

# Peguin original art from:
# http://www.flickr.com/photos/katmere/62037353/
# Updated at November 10th, 2005.
# Published under Creative Commons Attribution 2.0 Generic.

class Animal():
    img = None
    width = 0
    heigth = 0
    centerPosition = [0,0]
    
    def __init__(self):
        pass
        
    def collision(self):
        """Verifies if the animal has hit the floor, the ceil or any wall"""
        
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
        pass
        
    def collision(self, obj):
        """Verifies collision with another object"""
        pass

    def draw(self,screen,position):
        screen.blit(self.img, position)
        pass
        
    def update(self,time):
        pass
        
class Penguin(Animal):
    def __init__(self):
        super(Animal,self).__init__(self)
