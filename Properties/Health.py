class Health:
    def __init__(self):
        self.hitpoints = 100
    
    def looseHealth(self, damage):
        self.hitpoints -= damage
        return self.hitpoints

    