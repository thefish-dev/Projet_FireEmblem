from .Character import Character

class Player:
    def __init__(self, character):
        self.character = character
        self.units = self.character.units
        
    def CanPlay(self):
        return len(self.units) > 0