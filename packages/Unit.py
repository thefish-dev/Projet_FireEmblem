from .Player import Player
from .Attack import Attack

class Unit:
    def __init__(self, name: str, unitType: str, maxHealth: int, attacks: list, maxDistance: int, abilities: (list or None), properties: (list or None)):
        self.name = name
        self.type = unitType
        self.__maxHealth = maxHealth
        self.attacks = attacks
        self.abilities = abilities
        self.properties = properties
        self.maxDistance = maxDistance

        self.health = self.maxHealth

    def SetParent(self, parent: Player):
        self.parent = parent

    def ModifyHealth(self, modification: int):
        if modification > self.__maxHealth:
            self.health = self.__maxHealth
        elif modification < 0:
            self.health = 0
        else:
            self.health += modification

    def IsAlive(self):
        return self.health > 0
    
    def Attack(self, unit, attack: Attack):
        unit.ModifyHealth(attack.damages)
        ans1 = f"{unit.name} has been attacked and received {attack.damages} damages."
        ans2 = f"{unit.name} has been killed."
        print(ans1 if unit.IsAlive() else ans2)        