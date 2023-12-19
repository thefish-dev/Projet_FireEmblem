from .Attack import Attack
from .Ability import Ability

from random import randint

class Unit:
    def __init__(self, name: str, image: str, unitType: str, maxHealth: int, maxDistance: int, attacks: list, abilities: (list or None)):
        self.name = name
        self.image = image
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

    # Modifie la vie de l'unité (suite à une attaque ou une abilité de soin). 
    # Utilisation de clamp() pour être sûr que la vie ne soit ni supérieure à 100%, ni inférieure à 0.
    def modify_health(self, modification: int):
        self.health += round(modification)
        self.health = max(min(self.health, self.__maxHealth), 0) # Equivalent de clamp(valeur, min, max)
        print("New health", self.health)

    def is_alive(self):
        return self.health > 0
    
    # Attaque une unité et renvoie un tuple avec le score et un message à afficher
    def attack(self, target, attack: Attack):

        if not self.is_alive(): 
            return (0, "L'unité est morte")
        
        # Bouclier suite à une abilité appliquée sur cette cible
        if target.shield > 0:
            target.shield -= 1
            return (0, f"Cette unité est protégée par un bouclier, votre attaque ne lui a rien fait. Son bouclier a désormait {target.shield} de résistance.")
        
        # Abilité appliquée sur votre unité l'empêchant d'attaquer
        if self.can_attack > 0:
            self.can_attack -= 1
            return (0,"Votre unité n'est pas capable d'attaquer." + "Elle pourra attaquer de nouveau au prochain tour." if self.can_attack == 0 else "")
        
        # Attaque mortelle pour son utilisateur (notamment pour l'unité Minibombe)
        if attack.sacrifice == True:
            self.health = 0

        damages = attack.damages
        # Coup critique
        if randint(0,1) <= attack.critic_damage_chance: 
            damages *= attack.critic_damage_multiplier

        target.modify_health( -damages )

        # Calcul du score
        score = 1
        if damages > attack.damages: score += 1 # Coup critique
        if not target.is_alive(): score += 2

        # Message à afficher
        msg = f"{-damages} de dégats! "
        if not target.is_alive(): msg += f"Vous avez achevé {target.name}! "
        if attack.sacrifice == True: msg += "Vous y avez cependant laissé la vie."

        return (score, msg)

    def use_ability(self, target, ability: Ability):
        return ability.Run(self, target) # Résultat sous forme de str
        
    # Renvoie le pourcentage de santé restante
    def get_health(self):
        return int((self.health / self.__maxHealth) * 100)

    # Renvoir une moyenne de la puissance de toutes ses attaques
    def get_power(self):
        power = 0
        medium = 0
        for attack in self.attacks:
            power += attack.damages
            medium += 1
        return power // medium
        