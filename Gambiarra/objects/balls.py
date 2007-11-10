# /gambiarra/objects/level.py
# este arquivo contem a bola basica, outras sao derivadas desta

class Ball(object):
    img = None
    
    def __init__(self):
        pass

class BowlingBall(Ball):
    def __init__(self):
        super.__init__(self)
        
class BeachBall(Ball):
    def __init__(self):
        super.__init__(self)

