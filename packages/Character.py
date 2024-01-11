from .Unit import Unit

class Character:
    def __init__(self, name: str, desc: str, units: list):
        self.name = name
        self.desc = desc
        self.units = units
        self.__score = 0

    def increment_score(self, value: int):
        self.__score += value

    def get_score(self):
        return self.__score
        
    def can_play(self):
        return len(self.units) > 0