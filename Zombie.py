from Actor import *
from Movement import *

class Zombie(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.movement = Movement()
        self.grfx = "rsz_ozzy.jpg"
    
    def move(self):
        self.position.x -= self.movement.move()[0]
        self.position.y -= self.movement.move()[1]
        return self.position.x,self.position.y