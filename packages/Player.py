
class Player:
    def __init__(self, units, character):
        self.units = units
        self.character = character
        
    def CanPlay(self):
        return len(self.units) > 0