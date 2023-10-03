
class Game:
    def __init__(self, size):
        self.grid = [ [' ' for i in range (size[0])] * size[1] ]
        
    def affichage(self) :
        
    def PlaceUnit(self, unit, position):
        self.grid[position[0]][position[1]]=unit.name
        
    def MoveUnit(self, unit, position):
        ...