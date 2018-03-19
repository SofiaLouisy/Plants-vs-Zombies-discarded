from Board.Board import Board
import Actor

class A1:
    def __init__(self):
        self.zombies = [Actor.Zombie()]
        self.plants = [Actor.Plant(),Actor.Plant()]
        self.Board = Board()
        #self.plants[0].Position.x = 200
        if self.Board.putPlant(0,1):
            self.plants[0].setPosition(self.Board.getPosition(0,1))
        if self.Board.putPlant(0,0):
            self.plants[1].setPosition(self.Board.getPosition(0,0))


    def getActors(self):
        return (self.zombies,self.plants)

    def run(self):
        for zombie in self.zombies:
            if self.plants:
                if(zombie.isBlocked(self.plants[0])):
                    zombie.attack(self.plants[0])
                    if self.plants[0].isDead():
                        self.plants.remove(self.plants[0])
                else:
                    zombie.move()
            else:
                zombie.move()