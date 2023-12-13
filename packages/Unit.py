from .Attack import Attack
from .Ability import Ability

from random import randint

class Unit:
    def __init__(self, name: str, unitType: str, maxHealth: int, maxDistance: int, attacks: list, abilities: (list or None)):
        self.name = name
        self.type = unitType
        self.__maxHealth = maxHealth
        self.attacks = attacks
        self.abilities = abilities
        self.maxDistance = maxDistance

        self.team = 0
        self.health = self.__maxHealth
        self.shield = 0
        self.can_attack = 0

    def __str__(self):
        return self.name

    def set_team(self, team):
        self.team = team

    def modify_health(self, modification: int):
        self.health += round(modification)
        self.health = max(min(self.health, self.__maxHealth), 0) # Equivalent de clamp(valeur, min, max)
        print("New health", self.health)

    def is_alive(self):
        return self.health > 0
    
    def attack(self, target, attack: Attack):
        if not self.is_alive(): 
            return (0, "L'unité est morte")
        if target.shield > 0:
            target.shield -= 1
            return (0, f"Cette unité est protégée par un bouclier, votre attaque ne lui a rien fait. Son bouclier a désormait {target.shield} de résistance.")
        
        if self.can_attack > 0:
            self.can_attack -= 1
            return (0,"Votre unité n'est pas capable d'attaquer." + "Elle pourra attaquer de nouveau au prochain tour." if self.can_attack == 0 else "")
        
        damages = attack.damages
        if randint(0,1) <= attack.critic_damage_chance: 
            damages *= attack.critic_damage_multiplier # Application du multiplicateur en fonction de sa probabilité

        target.modify_health( -damages )

        score = 1
        if damages > attack.damages: score += 1
        if not target.is_alive(): score += 2

        return (score, f"{-damages} de dégats!" + f"Vous avez achevé {target.name}!" if target.is_alive() else "")

    def use_ability(self, target, ability: Ability):
        ability.Run(self, target) 
        
    def get_health(self):
        return int((self.health / self.__maxHealth) * 100)

    def get_power(self):
        power = 0
        medium = 0
        for attack in self.attacks:
            power += attack.damages
            medium += 1
        return power // medium
        