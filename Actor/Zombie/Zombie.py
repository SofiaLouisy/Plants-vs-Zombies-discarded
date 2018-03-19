from Actor.Actor import *
import Properties

class Zombie(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.Movement = Properties.Movement()
        self.Attack = Properties.Attack()
        self.grfx = "Actor/Zombie/rsz_ozzy.jpg"
    
    def move(self):
        self.Position.x -= self.Movement.move()
        return self.Position.x,self.Position.y
    
    def attack(self,other):
        self.Attack.attack(other)
    
