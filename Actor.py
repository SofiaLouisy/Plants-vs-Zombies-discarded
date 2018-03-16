from Health import Health
from Position import Position

class Actor:
    def __init__(self):
        self.health = Health()
        self.position = Position()

        #grfx
        self.grfx = "rsz_ozzy.jpg"
        self.width = 36
    
    def pos(self):
        return self.position.x,self.position.y
    
    def isBlocking(self,other):
        return other.pos()[0]-other.width//2 <= self.pos()[0]+self.width//2