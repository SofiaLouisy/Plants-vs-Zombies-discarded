from Actor.Actor import Actor

class Plant(Actor):
    def __init__(self):
        Actor.__init__(self)

        self.Position.x = 100
        #grfx
        self.grfx = "Actor/Plant/rsz_plant.gif"
        self.width = 36
    
    def setPosition(self,pos):
        self.Position.x = pos[0]
        self.Position.y = pos[1]