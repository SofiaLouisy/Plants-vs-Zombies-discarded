class Attack:
    def __init__(self):
        self.damage = 10
        self.chargeTime = 2
        self.charging = 0
    
    def attack(self, other):
        if(not self.charging):
            other.Health.looseHealth(self.damage)
            self.charging = self.chargeTime
            print("BANG")
        else:
            self.charging -= 1
            print("charging")