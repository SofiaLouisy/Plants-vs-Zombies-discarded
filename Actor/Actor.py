#from Properties.Health import *
#from Properties.Position import *
import Properties
from PIL import Image

class Actor:
    def __init__(self):
        self.Health = Properties.Health()
        self.Position = Properties.Position()

        #grfx
        self.grfx = "Actor/Zombie/ozzy.jpg"#"rsz_ozzy.jpg"
        self.width = 36
        #with Image.open(self.grfx) as img:
        #    self.width = img.size[0]
    
    def position(self):
        return self.Position.x,self.Position.y
    
    def isBlocked(self,other):
        return other.position()[0]+other.width//2 >= self.position()[0]-self.width//2

    def isDead(self):
        return self.Health.hitpoints <= 0
    
    def getGrfxFile(self):
        with Image.open(self.grfx,'r') as img:
            print(img)
            return img