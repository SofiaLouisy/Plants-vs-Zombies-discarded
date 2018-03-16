from Actor import *

class Plant(Actor):
    def __init__(self):
        Actor.__init__(self)

        self.position.x = 30
        #grfx
        self.grfx = "rsz_plant.gif"
        self.width = 36
        