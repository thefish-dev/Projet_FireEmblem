from random import randint
from math import *
from pygame import *
import pygame

#list des unité qui corresspond à leur perssonnage
lst_perso_attack={"unit1":["bombe","mage"],"unit2":["dustin_poirier","singe"],"unit3":["stone","serpent"]}

#Fonction pour charger les images plus rapidement
def element(chemin,tall) :       
        var=pygame.image.load(chemin)
        var=var.convert_alpha()
        var=pygame.transform.scale(var,tall)
        return var


#Classe élement graphique
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
    
    
#Position des text attaques et abillités pour les afficher au bonne endroit
position_attaque=[(980,40),(870,100),(870,115),(870,200),(870,215)]
position_abilities=[(870,200),(870,215),(870,270),(870,285)]
#variable test
unit_chose="unit2"
#Fonction qui detecte si le joueur essais de feinter le systéme, donc de se déplacer sur un obstacle
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
#fonction test : detecte obstacle
def detecte_obstacle2(choix_joueur,coordonnée : tuple) :
    pas_obstacle=True
    for i in range(len(choix_joueur["Joueur1"])) :
        if coordonnée== ((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)) :
            pas_obstacle=False
        elif coordonnée== ((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)) :
            pas_obstacle=False
    return pas_obstacle

#Fonction qui renvoie les coordonnée d'un possible obstacle
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
#fonction qui supprime un élement graphique, il le supprima alors de sa list d'affichage
def supprimer_element(choix_joueur,joueur,coordonnée) : 
    for i in range (len(choix_joueur[joueur])) :
        if (choix_joueur[joueur][i].rect.x,choix_joueur[joueur][i].rect.y)==coordonnée :
            choix_joueur[joueur].pop(i)           
    return choix_joueur
#Fonction qui prend en compte des coordonnées et renvoi sa place compléte dans le dictionnaire à condition que les coordonnées correspondent à une unité
def search_element(choix_joueur,coordonnée) :
    for i in range(len(choix_joueur["Joueur1"])) :
        if (choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)==coordonnée :
            return (i,"Joueur1")
        elif (choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)==coordonnée :
            return (i,"Joueur2")
    return None 

#Fonction correspondance, elle permettra l'affichage des bonnes attaque de l'unité pour la fonction affiche attaquz
#Elle prend en compte la place compléte d'une unité dans le dictionnaire choix_joueur grace a la fonction search element
def corespondance(choix_joueur,place_joueur) :
    if choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/bombe.png" :
        return ("unit1","bombe")
    elif choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/mage.png" :
        return ("unit1","mage")
    elif choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/singe.png" :
        return ("unit2","singe")
    elif choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/dustin_poirier.png" :
        return ("unit2","dustin_poirier")
    elif choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/serpent.png" :
        return ("unit3","serpent")
    elif choix_joueur[place_joueur[1]][place_joueur[0]].chemin=="./Images/stone.png" :
        return ("unit3","stone")
    
    
    

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
#fonction valeur absolue                
def valeur_absolue(a : int) :
    return abs(a)


#Fonction qui compte le déplacement grace a des vecteurs, si l'unité monte de 3 et descent de 2, la fonction va renvoyer (3,-2)
def deplacemet_total(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (x_total,y_totlal)
#utilisation des vecteurs pour savoir si l'unité est en mesure de se déplacer sur la case souhaitée : Xb - Xa)/60 pour l'abcisse 
# (Yb-Ya)/60 pour l'ordonnée, la somme de la valeur absolue des deux  sont le nombre totale de case déplacépour connaitre le nombre totale 
# de case déplacé, on divise par 60 car un carré fais, 60 pixels sur 60 pixels                   
def compte_case(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (valeur_absolue(x_total)+valeur_absolue(y_totlal))

#Fonction qui modifie l'emplacement d'une unité grace a la fonction deplacement total
def modificate_place(elem_graphique,deplacement) :
    if ((elem_graphique.rect.x + deplacement[0]*60) >=100) and ((elem_graphique.rect.x + deplacement[0]*60) <=640) and ((elem_graphique.rect.y + deplacement[0]*60) <=640) and ((elem_graphique.rect.x + deplacement[0]*60) >=100) : 
        elem_graphique.rect.x+=deplacement[0]*60 
        elem_graphique.rect.y+=deplacement[1]*60
    return elem_graphique
#Fonction test dans mes souvenirs
def search_coordinate2(coordonate) :
    possible_coordonate_x=[(i*60) for i in range (10)]
    possible_coordonate_y=[(i*60) for i in range (10)]
    if coordonate[0]<0 or coordonate[0]>540 or coordonate[1]<0 or coordonate[1]>540 :
        return None
    else :
        for i in range (len(possible_coordonate_x)) :
            for j in range (len(possible_coordonate_y)) :
                if (coordonate[0]>=possible_coordonate_x[j] and coordonate[0]<=possible_coordonate_x[j]+60) and (coordonate[1]<=possible_coordonate_x[i] and coordonate[1]>= possible_coordonate_x[i]+60) :
                    return (possible_coordonate_x[j],possible_coordonate_y[i])

#Fonction qui modifie dans la list d'affichage des unités, les changement de coordonnées des differentes unités                
def modificate_list_position(lst_position,coordonate_base,coordonate_want) :
    lst_modificate=[]
    for i in range (len(lst_position)) :
        if lst_position[i]==coordonate_base :
            lst_modificate.append(coordonate_want)
        else :
            lst_modificate.append(lst_position[i])
    return lst_modificate
#Fonction qui renvoie la place d'une unité dans le dictionnaire
def search_elem_in_choix_joueur_by_coordonate(choix_joueur,coordonate) :
    lst=["Joueur1","Joueur2"]
    for j in range (len(lst)) :
        for i in range (len(choix_joueur[j])) :
            if coordonate==(choix_joueur[lst[j]][i].rect.x,choix_joueur[lst[j]][i].rect.y) :
                return lst[j], i
    return None

#Fonction qui supprime un élement de la list d'affichage des différent joueurs
def delete_elem_graphique(choix_joueur,place_delete) :
    delete=choix_joueur[search_elem_in_choix_joueur_by_coordonate(choix_joueur,place_delete)]
    choix_joueur=choix_joueur[delete[0]].pop(delete[1])
    return choix_joueur
#Fonction qui vérifie si une unité adverse est proche
def close_elem_of_unit(coordonate,autre_joueur,choix_joueur,case_max) :
    close_elem=[]
    for i in range (len(choix_joueur[autre_joueur])) :
        if compte_case(coordonate,(choix_joueur[autre_joueur][i].rect.x,choix_joueur[autre_joueur][i].rect.y)) <=case_max :
            close_elem.append(choix_joueur[autre_joueur][i])
    return close_elem
#Fonction qui affiche les attaques d'une certaine unité
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


#Fonction qui affiche les abilités d'une certaine unité
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
    if perso =="unit2" and unit == "dustin_poirier" :
        image_text=demande_perso.render("Dustin Poirier n'a aucune abilité, c'est un combattant orpére, ",True,colors["blue"])
        image_text2=demande_perso.render("Mais il n'a pas de pouvoir magique",True,colors["blue"])
    if perso == "unit2"  and unit == "singe" :
        image_text=demande_perso.render("Ce gros singe aves ses chicos n'a aucune abilité, ET OUAIS",True,colors["blue"])
        image_text2=demande_perso.render("",True,colors["blue"])
    if perso == "unit3" and unit== "stone" :
        image_text=demande_perso.render("Stone est capale de protéger l'une de vos unité pour la ",True,colors["blue"])
        image_text2=demande_perso.render("prochaine fois que cette derniere ce fera attaquer",True,colors["blue"])
    if perso== "unit3" and unit == "serpent" :
        image_text=demande_perso.render("Serpent est doté d'une agilité deconsertante, il peut",True,colors["blue"])
        image_text2=demande_perso.render("alors esquiver des attaques, mais pas tout le TEMPS !",True,colors["blue"])
    image_text3=demande_perso.render("Vous n'utiliser aucune abbilités, c'est un choix qui peut",True,colors["blue"])
    image_text4=demande_perso.render("étre judicieux mais bon je suis perssone pour juger",True,colors["blue"])
    return [image_text,image_text2,image_text3,image_text4]
#Fonction qui affiche la barre de vie de toutes les unités d'un joueur
def health_bar(surface,choix_joueur,joueur) :
    position_health=[[(810,270),(900,290)],[(1010,270),(1100,290)],[(1210,270),(1300,290)],[(810,350),(900,370)],[(1010,350),(1100,370)],[(1210,350),(1300,370)],[(810,430),(900,450)]]
    for i in range (len(choix_joueur[joueur])) :
        surface.blit(choix_joueur[joueur][i].image,(position_health[i][0]))
        pygame.draw.rect(surface, (0,100,0), (position_health[i][1][0], position_health[i][1][1], 100, 30))

def winner_by_decision(surface,choix_joueur) :
    pygame.init()
    if choix_joueur["Joueur1"]==[] :
        joueur="Joueur2"
    elif choix_joueur["Joueur2"]==[] :
        joueur="Joueur1"


# Taille de la fenêtre
    txt=pygame.font.SysFont("monospace",30)
    txt_winner=txt.render("Et le gagnant par décision",True,(0,0,0))
    txt_winner2=txt.render(("unanime est le joueur",joueur),True,(0,0,0))

    
    end_wednesday =element("./Images/mercredi_finish.png",(300,150))
    bull=element("./Images/bulle.png",(200,120))
    end_background=element("./Images/end_fond.png",(800,800))

    # Création de la fenêtre
    winner = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Winner")
    



    # Boucle principale
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Dessiner ici

        # Actualisation de l'écran
        winner.fill((0,0,0))  # Remplir l'écran en blanc par exemple
        # Dessiner d'autres éléments ici
        winner.blit(end_background,(0,0))
        winner.blit(end_wednesday,(200,500))
        winner.blit(bull,(350,350))
        winner.blit(txt_winner,(360,375))
        winner.blit(txt_winner,(360,390))




        pygame.display.flip()




        



