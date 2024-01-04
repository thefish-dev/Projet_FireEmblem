import pygame
from pygame import *
from fonctions_pygame import *




choix_joueur={"Joueur1":[],"Joueur2":["jenna"]}

pygame.init()
if choix_joueur["Joueur1"]==[] :
    joueur="Joueur2"
elif choix_joueur["Joueur2"]==[] :
    joueur="Joueur1"



# Taille de la fenêtre
txt=pygame.font.SysFont("monospace",30)
txt_winner=txt.render("Et le gagnant par décision",True,(0,0,0))
txt_winner2=txt.render(("unanime est le joueur"),True,(0,0,0))

    
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




        
