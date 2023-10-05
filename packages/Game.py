from math import *
class Game:
    def __init__(self, size:int):
        self.grid = [ [' ' for i in range (size[0])] * size[1] ]
        
    def Affichage(self) :
        for i in range(len(self.grid)) :
            print(self.grid[i])


    def KnowPosition(self) :
        for i in range (len(self.grid)) :
            for j in range(len(self.grid[i])) :
                if self.grid([i][j])!=' ' :
                    return (i,j)

    def Distance(self,position:tuple,position_voulue:tuple) :
        return sqrt(((position_voulue[0]-position[0])**2)+((position_voulue[1]-position[1])**2))
        
    def PlaceUnit(self, unit, position):
        self.grid[position[0]][position[1]]=unit 
        
    def MoveUnit(self, unit,position:tuple, position_voulue :tuple):
        ...