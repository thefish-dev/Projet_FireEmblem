from .Character import Character
from .Unit import Unit

class Player:
    def __init__(self, character):
        self.character = character
        self.units = self.character.units
        
    def CanPlay(self):
        return len(self.units) > 0

    def AddUnit(self, unit: Unit):
        self.units += [unit]