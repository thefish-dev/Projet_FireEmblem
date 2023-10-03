
class Game:
    def __init__(self, size:int):
        self.grid = [ [' ' for i in range (size[0])] * size[1] ]
        
    def affichage(self) :
        for i in range(len(self.grid)) :
            print(self.grid[i])
        
    def PlaceUnit(self, unit, position):
        self.grid[position[0]][position[1]]=unit.name
        
    def MoveUnit(self, unit, position):
        