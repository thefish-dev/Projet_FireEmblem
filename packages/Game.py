from math import *
from packages import Unit

class Game:
    def __init__(self, size: int):
        self.size = size
        self.grid = [ [None for _ in range (size)] for _ in range (size) ]
        
    def affichage(self) :
        print("")
        clone = self.grid.copy()
        for line in clone:
            for e in line: 
                line[line.index(e)] = str(e)
                
            print(" | ".join(line))

    def get_position(self, unit: Unit) :
        for x in range(self.size):
            for y in range(self.size):
                print(self.grid[x][y])
                if self.grid[x][y] == unit or self.grid[x][y] == unit.name:
                    return (x,y)

    def geenerate_obstacles(self, amount):
        ...

    def distance(self,position: tuple,position_voulue: tuple) :
        if position[0]==int(position[0]) and position[1]==int(position[1])  :
            return sqrt(((position_voulue[0]-position[0])**2)+((position_voulue[1]-position[1])**2))
        
    def place_unit(self, unit: Unit, position: tuple):
        self.grid[position[0]][position[1]] = unit
        
    def move_unit(self, unit: Unit, position: tuple):
        currentPos = self.get_position(unit)
        if self.distance(currentPos, position) <= unit.maxDistance :
            self.grid[currentPos[0]][currentPos[1]] = None
            self.grid[position[0]][position[1]] = unit 
            return True
        else:
            return False
        
    def is_there_something(self, position: tuple):
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] != None and (x,y) == position:
                    return True
        return False
        