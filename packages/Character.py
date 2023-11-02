from .Unit import Unit

class Character:
    def __init__(self, name: str, units: list):
        self.name = name
        self.units = units
        self.__score = 0

    def IncrementScore(self, value: int):
        self.__score += value

    def GetScore(self):
        return self.__score
        
    def CanPlay(self):
        return len(self.units) > 0