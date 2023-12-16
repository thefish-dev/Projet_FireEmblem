from random import randint
from math import *
from pygame import *
import pygame

lst_perso_attack={"unit1":["bombe","mage"],"unit2":["dustin_poirier","singe"],"unit3":["stone","serpent"]}

#Fonction pour charger les images plus rapidement
def element(chemin,tall) :       
        var=pygame.image.load(chemin)
        var=var.convert_alpha()
        var=pygame.transform.scale(var,tall)
        return var

class Elem_Graphique(pygame.sprite.Sprite):
    def __init__(self,position_x,position_y,chemin):
        super().__init__()
        self.image= element(chemin,(60,60))
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

position_attaque=[(980,40),(870,100),(870,115),(870,200),(870,215)]

unit_chose="unit2"

def detecte_obstacle(choix_joueur,lst_obstacle,coordonnée : tuple) :
    pas_obstacle=True
    for i in range(len(choix_joueur["Joueur1"])) :
        if coordonnée== ((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)) :
            pas_obstacle=False
        elif coordonnée== ((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)) :
            pas_obstacle=False
    for i in range (len(lst_obstacle)) :
        if coordonnée==lst_obstacle[i] :
            pas_obstacle=False
    return pas_obstacle

def detecte_obstacle2(choix_joueur,coordonnée : tuple) :
    pas_obstacle=True
    for i in range(len(choix_joueur["Joueur1"])) :
        if coordonnée== ((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)) :
            pas_obstacle=False
        elif coordonnée== ((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)) :
            pas_obstacle=False
    return pas_obstacle


def create_obstacle(choix_joueur) :
    obstacle_aléatoire= [0,0]
    lst_coordonnée_possible_x=[(100+i*60) for i in range (10)]
    lst_coordonnée_possible_y=[(100+i*60) for i in range (10)]
    trouver_place_obstacle=True

    while trouver_place_obstacle :
        essaie=(lst_coordonnée_possible_x[randint(0,9)],lst_coordonnée_possible_x[randint(0,9)])
        if detecte_obstacle2(choix_joueur,essaie) :
            trouver_place_obstacle=False
    return essaie

def supprimer_élement(choix_joueur,joueur,coordonnée) : 
    for i in range (len(choix_joueur[joueur])) :
        if choix_joueur[joueur][i]==coordonnée :
            choix_joueur[joueur].pop(i)           
    return choix_joueur

def search_element(choix_joueur,coordonnée) :
    for i in range(len(choix_joueur["Joueur1"])) :
        if (choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)==coordonnée :
            return i,"Joueur1"
        elif (choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)==coordonnée :
            return i,"Joueur2"
    return None 

#verifie dans quele carré le joueur clique
def search_coordinate(coordonate) :
    possible_coordonate_x=[(100+i*60) for i in range (10)]
    possible_coordonate_y=[(100+i*60) for i in range (10)]
    if coordonate[0]<40 or coordonate[0]>700 or coordonate[1]<40 or coordonate[1]>700 :
        return None
    else :
        for i in range (len(possible_coordonate_x)) :
            for j in range (len(possible_coordonate_y)) :
                if (coordonate[0]>=possible_coordonate_x[j] and coordonate[0]< possible_coordonate_x[j]+60) and (coordonate[1]>=possible_coordonate_x[i] and coordonate[1]< possible_coordonate_x[i]+60) :
                    return (possible_coordonate_x[j],possible_coordonate_y[i])
                
def valeur_absolue(a : int) :
    return abs(a)

#utilisation des vecteurs pour savoir si l'unité est en mesure de se déplacer sur la case souhaitée : Xb - Xa)/60 pour l'abcisse 
# (Yb-Ya)/60 pour l'ordonnée, la somme de la valeur absolue des deux  sont le nombre totale de case déplacépour connaitre le nombre totale 
# de case déplacé, on divise par 60 car un carré fais, 60 pixels sur 60 pixels                   
def compte_case(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (valeur_absolue(x_total)+valeur_absolue(y_totlal))

def déplacemet_total(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (x_total,y_totlal)

def modificate_place(elem_graphique,deplacement) :
    if ((elem_graphique.rect.x + deplacement[0]*60) >=100) and ((elem_graphique.rect.x + deplacement[0]*60) <=640) and ((elem_graphique.rect.y + deplacement[0]*60) <=640) and ((elem_graphique.rect.x + deplacement[0]*60) >=100) : 
        elem_graphique.rect.x+=deplacement[0]*60 
        elem_graphique.rect.y+=deplacement[1]*60
    return elem_graphique

def search_coordinate2(coordonate) :
    possible_coordonate_x=[(i*60) for i in range (10)]
    possible_coordonate_y=[(i*60) for i in range (10)]
    if coordonate[0]<0 or coordonate[0]>540 or coordonate[1]<0 or coordonate[1]>540 :
        return None
    else :
        for i in range (len(possible_coordonate_x)) :
            for j in range (len(possible_coordonate_y)) :
                if (coordonate[0]>=possible_coordonate_x[j] and coordonate[0]< possible_coordonate_x[j]+60) and (coordonate[1]>=possible_coordonate_x[i] and coordonate[1]< possible_coordonate_x[i]+60) :
                    return (possible_coordonate_x[j],possible_coordonate_y[i])
                
def modificate_list_position(lst_position,coordonate_base,coordonate_want) :
    lst_modificate=[]
    for i in range (len(lst_position)) :
        if lst_position[i]==coordonate_base :
            lst_modificate.append(coordonate_want)
        else :
            lst_modificate.append(lst_position[i])
    return lst_modificate

def search_elem_in_choix_joueur_by_coordonate(choix_joueur,coordonate) :
    lst=["Joueur1","Joueur2"]
    for j in range (len(lst)) :
        for i in range (len(choix_joueur[j])) :
            if coordonate==(choix_joueur[lst[j]][i].rect.x,choix_joueur[lst[j]][i].rect.y) :
                return lst[j], i
    return None


def delete_elem_graphique(choix_joueur,place_delete) :
    delete=choix_joueur[search_elem_in_choix_joueur_by_coordonate(choix_joueur,place_delete)]
    choix_joueur=choix_joueur[delete[0]].pop(delete[1])
    return choix_joueur

def close_elem_of_unit(coordonate,autre_joueur,choix_joueur,case_max) :
    close_elem=[]
    for i in range (len(choix_joueur[autre_joueur])) :
        if compte_case(coordonate,(choix_joueur[autre_joueur][i].rect.x,choix_joueur[autre_joueur][i].rect.y)) <=case_max :
            close_elem.append(choix_joueur[autre_joueur][i])
    return close_elem

def affiche_attaque(perso,unit) :
    demande_perso = pygame.font.SysFont("monospace",14)
    colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0),
    "vert" :(0,255,0),
    "black" : (0,0,0),
    "white" : (255,255,255)
    }
    if perso == "unit1" and unit=="bombe" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["white"])
        image_text2 = demande_perso.render("Explosion Grotesque :Cette attaque est une attaque trés forte mais " , True, colors["blue"])
        image_text3=demande_perso.render(" l unité minibombe meurre lors de l attaque : 90 dégat" , True, colors["blue"])
        image_text4 = demande_perso.render("C4, Cette attaque peut s'utiliser à distance (de 3 cases max) car la minibombe  " , True, colors["blue"])
        image_text5 = demande_perso.render("lance un C4 sur son adversaire : 30 dégats" , True, colors["blue"])
    if perso== "unit1" and unit == "mage" :
         image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
         image_text2 = demande_perso.render("Coup de foudre Cette attaque electrocute une unité, vous pouvez l'utiliser" , True, colors["blue"])
         image_text3 = demande_perso.render(" à une distance de 2 case max : 20 dégats" , True, colors["blue"])
         image_text4 = demande_perso.render("",True,colors["blue"])
         image_text5 = demande_perso.render("",True,colors["blue"])
    if perso=="unit2" and unit=="dustin_poirier" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("étranglement en guillotine : ataque trés puisante , il ne faut pas" , True, colors["blue"])
        image_text3 = demande_perso.render("mettre en rage dustin Poirier : 60 dégat" , True, colors["blue"])
        image_text4 = demande_perso.render("Ground and pound, Cette attaque est agressive et puissante mais elle  ",True, colors["blue"])
        image_text5 = demande_perso.render("necessite d'étre proche pour étre utiliser (1 case) : 30 dégats",True, colors["blue"])
    if perso =='unit2' and unit=="singe" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("Coup de chico super chockbar,  le singe n'est pas content ,attaque plutot " , True, colors["blue"])
        image_text3 = demande_perso.render("proche (2cases): 30 dégats" , True, colors["blue"])
        image_text4 = demande_perso.render("Coup de pied retourné en highkick : une puissance de zinzin, attaque  ", True, colors["blue"])
        image_text5 = demande_perso.render("plutot proche (2 cases) : 60 dégat", True, colors["blue"])

    if perso=="unit3" and unit=="stone" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("Charge, une pierre te fonce dessus à une vitesse gargantuesque, peut attaquer" , True, colors["blue"])
        image_text3 = demande_perso.render("de loin (4 cases): 30 dégats" , True, colors["blue"])
        image_text4 = demande_perso.render("Tremblement de terre, ce gros bonhome tape des pied mais il fais le poid de ",True, colors["blue"])
        image_text5 = demande_perso.render("pantagruel, peut attaquer de loin (3 cases),: 20 dégats",True, colors["blue"])
    if perso=="unit3" and unit=="serpent" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("Etranglement en guillotine,le serpent t'attaque avec ses gros muscle de zinzin, ataque" , True, colors["blue"])
        image_text3 = demande_perso.render("proche(1 case): 30 dégats" , True, colors["blue"])
        image_text4 = demande_perso.render("Morsure, le serpent te mord car il a les crocs comme arthur attaque puissannte plutot",True, colors["blue"])
        image_text5 = demande_perso.render("proche : 70 dégats",True, colors["blue"])

    return [image_text,image_text2,image_text3,image_text4,image_text5]

def affiche_abillities (perso,unit) :
    demande_perso = pygame.font.SysFont("monospace",12)
    colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0),
    "vert" :(0,255,0),
    "black" : (0,0,0),
    "white" : (255,255,255)
    }
    if perso=="unit1" and unit=="bombe" :
        image_text=demande_perso.render("Vous pouvez soignez un d vos compatriote, cliquer sur lui",True,colors["blue"])
        image_text2=demande_perso.render("Vous ne pouurez pas le faire indefiniment",True,colors["blue"])
    if perso=="unit1" and unit=="mage" :
        image_text=demande_perso.render("Au prochain tour vous attaqerez avec une attaque aléatoire",True,colors["blue"])
        image_text2=demande_perso.render("que vous volez à une unité",True,colors["blue"])
    if perso =="uit2" and unit == "dustin_poirier" :
        image_text=None
        image_text2=None
    if perso == "unit2"  and unit == "singe" :
        image_text=None
        image_text2=None
    if perso == "unit3" and unit== "stone" :
        image_text=demande_perso.render("Stone est capale de protéger l'une de vos unité pour la ",True,colors["blue"])
        image_text2=demande_perso.render("prochaine fois que cette derniere ce fera attaquer",True,colors["blue"])
    if perso== "unit3" and unit == "serpent" :
        image_text=demande_perso.render("Serpent est doté d'une agilité deconsertante, il peut")
        image_text2=demande_perso.render("alors esquiver des attaques, mais pas tout le TEMPS !",True,colors["blue"])
    return [image_text,image_text2]

def health_bar(surface,choix_joueur,joueur) :
    position_health=[[(810,270),(900,290)],[(1010,270),(1100,290)],[(1210,270),(1300,290)],[(810,350),(900,370)],[(1010,350),(1100,370)],[(1210,350),(1300,370)],[(810,430),(900,450)]]
    for i in range (len(choix_joueur[joueur])) :
        surface.blit(choix_joueur[joueur][i].image,(position_health[i][0]))
        pygame.draw.rect(surface, (0,100,0), (position_health[i][1][0], position_health[i][1][1], 100, 30))


    



