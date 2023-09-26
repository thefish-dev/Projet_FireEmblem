from .Player import Player

class Unit:
    def __init__(self, name: str, unitType: str, maxHealth: int, attacks: list, abilities: (list or None), properties: (list or None)):
        self.name = name
        self.type = unitType
        self.__maxHealth = maxHealth
        self.attacks = attacks
        self.abilities = abilities
        self.properties = properties

        self.health = self.maxHealth

    def setParent(self, parent: Player):
        self.parent = parent

    def ModifyHealth(self, modification: int):
        if modification > self.__maxHealth:
            self.health = self.__maxHealth
        elif modification < 0:
            self.health = 0
        else:
            self.health += modification