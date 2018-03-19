class Board:
    grfx = "Board/grass.bmp"
    size = width,height = (1027,770) #image size

    def __init__(self):
        self.lanes = 1
        self.grid = []
        self.sections = 3
        self.constructGrid()
    
    def setLanes(self,nr):
        self.lanes = nr
        self.constructGrid()

    def constructGrid(self):
        self.grid = []
        for i in range(self.lanes):
            self.grid.append([True for i in range(self.sections)])
    
    def getPosition(self,r,c):
        x = Board.width*(c+1)//(self.sections*2)
        #x = Board.width*(1)//(self.sections*2)
        y = Board.height*(r+1)//(self.lanes*2)
        return x,y
    
    def putPlant(self,r,c):
        if self.grid[r][c]:
            self.grid[r][c] = False
            return True
        else:
            return False