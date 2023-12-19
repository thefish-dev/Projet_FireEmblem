from .Unit import Unit
from pygame import *
import pygame

from random import randint

class Sprite(pygame.sprite.Sprite) :
    def __init__(self, unit: Unit, position_x, position_y, chemin):
        self.unit = unit
        self.name = ""
        self.type = ""
        self.maxHealth = 0
        self.attacks = ""
        self.abilities = ""
        self.maxDistance = ""

        self.health = ""
        super().__init__()
        self.image= self.element(chemin,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = position_x # Position initiale x
        self.rect.y = position_y  # Position initiale y
    
    def droite (self) :
        if self.rect.x<640 :
            self.rect.x += 60
    def gauche(self) :
        if self.rect.x>100 :
            self.rect.x-=60
    def monter (self) :
        if self.rect.y>100 :
            self.rect.y-=60
    def descendre (self) : 
        if self.rect.y <640 :
            self.rect.y+=60


    def element(self,chemin,tall) :
        var=image.load(chemin)
        var=var.convert_alpha()
        var=transform.scale(var,tall)
        return var
    
    def __str__(self) -> str:
        return super().__str__()


#adapt les fonctions a pygame si besoin genre par exemple, les text ne sont plus des chaines de charactére, mais des text graphique a afficher

#la fonction peut attaquer ce sera si une unité adverse est a une distance assez proche de l'unité jouer, tu pourra utiliser la 
#pour rappel toutes les unités de la map ainsi que leur position sont dans le dictionnaire choix_joueur dans acceuil

#En gros a la fin il me faudrait un code qui selectionne une unité, regarde si elle peut les attquer aux alentours en fonction de la portée
#  des attques, si oui alors propose ls attaques, propose d'en choisir une, propose au second joueur si une de ses abilité peut l'aider a detournez
#l'attaque si possible, si non modifie la vie de l'unité et tej la si elle a plus de vie(tu le supprime juste de cjoix_perso)


"""
    Liste des fonctions:

    unit.modify_health(int) => None

    unit.is_alive() => Booléen
    
    unit.attack(cible, attaque) => tuple(Score, message)

    unit.use_ability(cible, abilité) => message

    unit.get_health() => Renvoie la vie en pourcentage

    unit.get_power() => Renvoie une moyenne de la puissance de toutes ses attaques


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

    # Renvoie une moyenne de la puissance de toutes ses attaques
    def get_power(self):
        power = 0
        medium = 0
        for attack in self.attacks:
            power += attack.damages
            medium += 1
        return power // medium
"""