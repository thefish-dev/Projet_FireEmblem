from math import *
from packages import Unit
import random

def clamp(valeur, min, max):
    return max(min(valeur, max), min)

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
        obstacles = [1,2,3]
        for _ in range(amount):
            obstacle = random.choice(obstacles)

            def random_loc():
                loc = (random.randint(2,self.size - 4), random.randint(0,self.size-1))
                if self.is_there_something(loc):
                    return random_loc()
                else:
                    return loc
            
            x,y = random_loc()
            self.grid[x][y] = obstacle


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
        x,y = position
        return self.grid[x][y] != None
        