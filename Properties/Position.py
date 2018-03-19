from Board.Board import *

class Position:
    def __init__(self):
        self.x = Board.width
        self.y = Board.height//2
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    #def setLane(self, y):
    #    self.y = Board.height//(2*y*Board.lanes)