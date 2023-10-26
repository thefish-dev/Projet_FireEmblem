from .Player import Player
from .Attack import Attack
from .Ability import Ability

class Unit:
    def __init__(self, name: str, unitType: str, maxHealth: int, maxDistance: int, attacks: list, abilities: (list or None), properties: (list or None)):
        self.name = name
        self.type = unitType
        self.__maxHealth = maxHealth
        self.attacks = attacks
        self.abilities = abilities
        self.properties = properties
        self.maxDistance = maxDistance

        self.health = self.__maxHealth

    def __str__(self):
        return self.name

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
    
    def Attack(self, target, attack: Attack):
        target.ModifyHealth(attack.damages)
        ans1 = f"{target.name} has been attacked and received {attack.damages} damages."
        ans2 = f"{target.name} has been killed."
        print(ans1 if target.IsAlive() else ans2)   

    def UseAbility(self, unit, ability: Ability):
        
        ...  
        
    def GetHealthPercent(self):
        return (self.health / self.__maxHealth).__round__()

    def GetPower(self):
        power = 0
        medium = 0
        for attack in self.attacks:
               power += attack.damages
               medium += 1
        return power // medium
        