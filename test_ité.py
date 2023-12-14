import pygame
import sys
from fonctions_pygame import *
from pygame import*

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre et des carrés
largeur_fenetre = 1200
hauteur_fenetre = 800
taille_carré = 60
nb_colonnes = 10
nb_lignes = 10

def affiche_attaque(perso,unit) :
    demande_perso = pygame.font.SysFont("monospace",30)
    colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0),
    "vert" :(0,255,0),
    "black" : (0,0,0),
    "white" : (255,255,255)
    }
    if perso == "unit1" and unit=="bombe" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("Explosion Grotesque :Cette attaque est une attaque trés forte mais l unité minibombe meurre lors de l attaque : 90 dégat" , True, colors["blue"])
        image_text3 = demande_perso.render("C4, Cette attaque peut s'utiliser à distance (de 3 cases max) car la minibombe lance un C4 sur son adversaire : 30 dégats" , True, colors["blue"])
    if perso== "unit1" and unit == "mage" :
         image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
         image_text2 = demande_perso.render("Coup de foudre Cette attaque electrocute une unité, vous pouvez l'utiliser à une distance de 2 case max : 20 dégats" , True, colors["blue"])
         image_text3 = demande_perso.render()
    if perso=="unit2" and unit=="dustin_poirier" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"])
        image_text2 = demande_perso.render("étranglement en guillotine : ataque trés puisante , il ne faut pas mettre en rage dustin Poirier : 60 dégat" , True, colors["blue"])
        image_text3 = demande_perso.render("Ground and pound, Cette attaque est agressive et puissante mais elle necessite d'étre proche pour étre utiliser (1 case) : 30d dégats",True, colors["blue"])
    if perso =='unit2' and unit=="singe" :
        image_text = demande_perso.render('Vous pouvez attaquez votre adversaire : ', True, colors["blue"]) 
        pass




 
        

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tableau de Carrés")

# Couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
def element(chemin,tall) :       
        var=pygame.image.load(chemin)
        var=var.convert_alpha()
        var=pygame.transform.scale(var,tall)
        return var


# Fonction pour dessiner la grille de carrés
def dessiner_grille():
    for x in range(nb_colonnes):
        for y in range(nb_lignes):
            rect = pygame.Rect(x * taille_carré, y * taille_carré, taille_carré, taille_carré)
            pygame.draw.rect(fenetre, NOIR, rect, 1)
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
elem=[Elem_Graphique(120,120,"./Images/bombe.png")]

case_maxi=3

# Boucle de jeu
running = True
clique_droit=0
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  
            clique_droit+=1
            if clique_droit==1 :
                mouse_pos_unit = pygame.mouse.get_pos()
            elif clique_droit==2 :
                clique_droit=0
                mouse_pose_want=pygame.mouse.get_pos()
                coordonate_base=search_coordinate2((mouse_pos_unit[0],mouse_pos_unit[1]))
                print(elem[0].rect.x,elem[0].rect.y)
                print(coordonate_base)
                coordonate_want=search_coordinate2((mouse_pose_want[0],mouse_pose_want[1]))
                if coordonate_base==((elem[0].rect.x,elem[0].rect.y)) :               
                    case_max=compte_case(coordonate_base,coordonate_want)
                    deplacement=déplacemet_total(coordonate_base,coordonate_want)
                    if case_max<=case_maxi :
                        elem[0]=modificate_place(elem[0],deplacement) 




            
           
            

             

                
                
    
    # Dessin sur l'écran
    fenetre.fill(BLANC)  # Remplir l'écran avec une couleur de fond
    dessiner_grille()  # Dessiner la grille de carrés
    fenetre.blit(elem[0].image,(elem[0].rect.x,elem[0].rect.y))

    # Mettre à jour l'affichage
    pygame.display.flip()
    
# Quitter Pygame
pygame.quit()
sys.exit()