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



#le nombre de fois que une unité peut utiliser une abillities
#adapt les fonctions a pygame si besoin genre par exemple, les text ne sont plus des chaines de charactére, mais des text graphique a afficher
#la fonction peut attaquer ce sera si une unité adverse est a une distance assez proche de l'unité jouer, tu pourra utiliser la 
#pour rappel toutes les unités de la map ainsi que leur position sont dans le dictionnaire choix_joueur dans acceuil

#En gros a la fin il me faudrait un code qui selectionne une unité, regarde si elle peut les attquer aux alentours en fonction de la portée
#  des attques, si oui alors propose ls attaques, propose d'en choisir une, propose au second joueur si une de ses abilité peut l'aider a detournez
#l'attaque si possible, si non modifie la vie de l'unité et tej la si elle a plus de vie(tu le supprime juste de cjoix_perso)