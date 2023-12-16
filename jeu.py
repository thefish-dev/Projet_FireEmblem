import pygame
from pygame import *
import sys
from random import randint
from fonctions_pygame import *


def MAIN(choix_joueur):
    playing=True 

    pygame.init()

    # Définition de la taille de la fenêtre

    background = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("Fire emblem")

    carre=element("./Images/carre.JPG",(60,60))
    contour=element("./Images/contour.png",(700,700))
    fond = element("./Images/fond.png",(800,800))



    lst_obstacle=["./Images/rocher.png","./Images/sapin.png","./Images/arbre.png","./Images/circulation.png","./Images/chien_arthur.png"]
    for i in range (len(lst_obstacle)) :
        lst_obstacle[i]=element(lst_obstacle[i],(60,60))

    lst_position_obstacle=[]

    while len(lst_position_obstacle) <5 :
        essaie=create_obstacle(choix_joueur)
        if essaie  not in lst_position_obstacle :
            lst_position_obstacle.append(essaie)
    print(lst_position_obstacle)
    lst_position_joueur_1=[]
    lst_position_joueur_2=[]
    for i in range (len(choix_joueur["Joueur1"])) :
        lst_position_joueur_1.append((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y))
    for i in range (len(choix_joueur["Joueur2"])) :
        lst_position_joueur_2.append((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y))


    print(lst_position_joueur_1)
    clique_droit=0
    case_maxi=4
    choix_tour_joueur="Joueur1"
    fond_attaque=element("./Images/fond_attaque.png",(700,800))
    wednesday_attack=element("./Images/mercredi.png",(120,200))
    thing=element("./Images/the_thing.png",(40,40))
    bulle=element("./Images/bulle.png",(170,135))
    text_bulle=element("./Images/text_bulle.png",(120,60))

    # Musique du jeu
    pygame.mixer.music.load("sounds/fight_music.mp3")
    pygame.mixer.music.play(-1)
    attaque=0
    # Boucle de jeu
    running = True
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
                    coordonate_base=search_coordinate((mouse_pos_unit[0],mouse_pos_unit[1]))              
                    coordonate_want=search_coordinate((mouse_pose_want[0],mouse_pose_want[1]))
                    elem_move=search_element(choix_joueur,coordonate_base)
                    if elem_move is not None :       
                        if coordonate_want is not None :        
                            case_max=compte_case(coordonate_base,coordonate_want)
                            deplacement=déplacemet_total(coordonate_base,coordonate_want)
                            if case_max<=case_maxi :

                                if detecte_obstacle(choix_joueur,lst_position_obstacle,coordonate_want)  :
                                    if choix_tour_joueur=="Joueur1" :
                                        if coordonate_base in lst_position_joueur_1 :
                                            choix_tour_joueur="Joueur2"
                                            lst_position_joueur_1=modificate_list_position(lst_position_joueur_1,coordonate_base,coordonate_want)


                                            choix_joueur[elem_move[1]][elem_move[0]]=modificate_place(choix_joueur[elem_move[1]][elem_move[0]],deplacement)
                                            if close_elem_of_unit(coordonate_want,"Joueur2",choix_joueur,1) != [] :

                                                attaque=1
                                    elif choix_tour_joueur=="Joueur2" :
                                        if coordonate_base in lst_position_joueur_2 :
                                            choix_tour_joueur="Joueur1"
                                            lst_position_joueur_2=modificate_list_position(lst_position_joueur_2,coordonate_base,coordonate_want)

                                            choix_joueur[elem_move[1]][elem_move[0]]=modificate_place(choix_joueur[elem_move[1]][elem_move[0]],deplacement)
                                            if close_elem_of_unit(coordonate_want,"Joueur1",choix_joueur,1) != [] :                                   
                                                attaque=1




        background.fill((0,0,0))  # Remplir l'écran avec une couleur de fond
        background.blit(fond,(0,0))
        background.blit(contour,(50,50))

        for i in range(10) :
            for j in range(10) :
                background.blit(carre,((100+j*60),(100+i*60)))
        for i in range (len(choix_joueur["Joueur1"])) :
            background.blit(choix_joueur["Joueur1"][i].image,(choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y))
        for i in range (len(choix_joueur["Joueur2"])) :
            background.blit(choix_joueur["Joueur2"][i].image,(choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y))
        for i in range (len(lst_obstacle)) :
            background.blit(lst_obstacle[i],(lst_position_obstacle[i][0],lst_position_obstacle[i][1]))
        if attaque==1 :
            print(unit_chose)
            pygame.draw.rect(background, (0,0,0), (800, 0, 700, 800))
            background.blit(fond_attaque,(800,0))
            background.blit(wednesday_attack,(900,600))
            background.blit(thing,(1150,560))
            background.blit(bulle,(970,480))
            background.blit(text_bulle,(1000,510))
            pygame.draw.rect(background, (255,0,0), (810, 100, 60, 30))
            pygame.draw.rect(background, (0,255,0), (810, 200, 60, 30)) 
            for i in range (5) :
                background.blit(affiche_attaque(unit_chose,lst_perso_attack[unit_chose][1])[i],position_attaque[i])






        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()

    sys.exit()
