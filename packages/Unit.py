from .Attack import Attack
from .Ability import Ability

from random import randint

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

    def set_team(self, team):
        self.team = team

    def modify_health(self, modification: int):
        self.health += modification
        self.health = max(min(self.health, self.__maxHealth), 0) # Equivalent de clamp(valeur, min, max)
        print("New health", self.health)

    def is_alive(self):
        return self.health > 0
    
    def attack(self, target, attack: Attack):
        if not self.is_alive(): 
            return

        damages = attack.damages
        if randint(0,1) <= attack.critic_damage_chance: 
            damages *= attack.critic_damage_multiplier # Application du multiplicateur en fonction de sa probabilité

        target.modify_health( -damages )
        ans1 = f"{target.name} has been attacked and received {damages} damages."
        ans2 = f"{target.name} has been killed."
        print(ans1 if target.is_alive() else ans2) 

        score = 1
        if damages > attack.damages: score += 1
        if not target.is_alive(): score += 2
        return score

    def use_ability(self, unit, ability: Ability):
        
        ...  
        
    def get_health(self):
        return int((self.health / self.__maxHealth) * 100)

    def get_power(self):
        power = 0
        medium = 0
        for attack in self.attacks:
            power += attack.damages
            medium += 1
        return power // medium
        