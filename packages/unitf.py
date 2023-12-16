from .Attack import Attack
from .Ability import Ability
from pygame import *
import pygame

from random import randint

class Unit(pygame.sprite.Sprite) :
    def __init__(self,position_x,position_y,chemin):
        
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

        return (score, f"{-damages} de dégats!" + f"Vous avez achevé {target.name}!" if not target.is_alive() else "")

    def use_ability(self, target, ability: Ability):
        return ability.Run(self, target) 
        
    def get_health(self):
        return int((self.health / self.__maxHealth) * 100)

    def get_power(self):
        power = 0
        medium = 0
        for attack in self.attacks:
            power += attack.damages
            medium += 1
        return power // medium
    
def finish_unit(unit,name,type,maxHealth,attacks,abilities,max_distance,health) :
    unit.name=name
    unit.type=type
    unit.maxHealth=maxHealth
    unit.attacks=attacks
    unit.abilities=abilities
    unit.max_distance=max_distance
    unit.health=health
    return unit





{"bombe" :["bombe","feu",100,"tu peux mettre les attques correspondant a bombe stp","pareil pour les abillités","tu pourras crée un fonction pour enlever la vie, et la vie correspondra a sa"]}
#tu peut faire sa pour chaque perssonnage
#fonction a crée : si le joueur à toujours de la vie, le nombre de fois que une unité peut utiliser une abillities
#adapt les fonctions a pygame si besoin genre par exemple, les text ne sont plus des chaines de charactére, mais des text graphique a afficher
#tu pouuras regrder dans acceuil, il y a des exemples
#la fonction peut attquer ce sera si une unité adverse est a une distance assez proche de l'unité jouer, tu pourra utiliser la 
#pour rappel toute les unité de la map ainsi que leur position sont dans le dictionnaire choix_joueur dans acceuil

#En gros a la fin il me faudrait un code qui selectionne une unité, regarde si elle peut les attquer aux alentours en fonction de la portée
#  des attques, si oui alors propose ls attaques, propose d'en choisir une, propose au second joueur si une de ses abilité peut l'aider a detournez
#l'attaque si possible, si non modifie la vie de l'unité et tej la si elle a plus de vie(tu le supprime juste de cjoix_perso)
#

#FAIS LE JE T'EN SUPPLIE 


