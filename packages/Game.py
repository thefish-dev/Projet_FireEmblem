from math import *
from packages import Unit

class Game:
    def __init__(self, size: int):
        self.size = size
        self.grid = [ [' ' for _ in range (size)] for _ in range (size) ]
        
    def Affichage(self) :
        print("")
        for line in self.grid:
            for e in line: line[line.index(e)] = str(e)
            print(line)

    def KnowPosition(self, unit: Unit) :
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == unit:
                    return (x,y)

    def Distance(self,position: tuple,position_voulue: tuple) :
        if position[0]==int(position[0]) and position[1]==int(position[1])  :
            return sqrt(((position_voulue[0]-position[0])**2)+((position_voulue[1]-position[1])**2))
        
    def PlaceUnit(self, unit: Unit, position: tuple):
        self.grid[position[0]][position[1]] = unit
        
    def MoveUnit(self, unit: Unit, position: tuple):
        if self.Distance(self.KnowPosition(),position) <= unit.maxDistance :
            self.grid[position[0]][position[1]] = unit 
        