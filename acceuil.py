import pygame
import sys

# Initialisation de Pygame
pygame.init()

#Pour l'affichage du text
choix_joueur_1=True
choix_joueur_2=False

#Dictionnaire avec les unités choisit par les joueurs
choix_joueur= {
     "Joueur1" : "",
     "Joueur2" :""
}

#Création de la fenétre
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fire emblem")

#Dictionnaire avec les couleurs
colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0),
    "vert" :(0,255,0),
    "black" : (0,0,0)
}
#Fonction pour charger les images plus rapidement
def element(chemin,tall) :       
        var=pygame.image.load(chemin)
        var=var.convert_alpha()
        var=pygame.transform.scale(var,tall)
        return var


#Differente police utilisé 
description = pygame.font.SysFont("monospace",15)
affichage=pygame.font.SysFont("chemin_vers_ta_police_en_gras.ttf",50)
demande_perso = pygame.font.SysFont("monospace",30)

#Question de choix des joueurs
image_text = demande_perso.render('Joueur 1 :choisissez votre personnage ', True, colors["blue"])
image_text2 = demande_perso.render('Joueur 2 :choisissez votre personnage ', True, colors["blue"])



#Description des unités
Unit1_description = description.render('Equipe réflechi et methodique mais Bombe est suicidaire ce qui ne fait pas la  ', True, colors["vert"])
Unit1_p_2=description.render('fierté du puissant mage noir, un voleur capable de foudroyer ses énnemi',True, colors["vert"])
print_unit1=affichage.render('Unit 1',True,colors["black"])

Unit2_descripion= description.render('Equipe dotée d une force et d une puissance exeptionnel grace a leur éxperience', True, colors["red"])
Unit2_descripion_p_2= description.render('en MMA, cette unité n a pas d abilité, tout dans les muscles, rien dans la téte', True, colors["red"])
print_unit2=affichage.render('Unit 2',True,colors["black"])


Unit3_descripion= description.render('Equipe visieuse car le gros stone peut proteger  Serpent, car ce denier n a pas', True, colors["blue"])
Unit3_descripion_p_2= description.render('beaucoup de vie contrairement a ce gros tank de Stone,Serpent peut soigner',True, colors["blue"])
print_unit3=affichage.render('Unit 3',True,colors["black"])




#Chargement des images
fond_acceuil=element("./Images/fond_acceuil.jpg",(800,800))
bombe=element("./Images/bombe.png",(80,80))
mage=element("./Images/mage.png",(80,80))
serpent=element("./Images/serpent.png",(80,80))
stone=element("./Images/stone.png",(80,80))
dustin_poirier=element("./Images/dustin_poirier.png",(80,80))
singe=element("./Images/singe.png",(80,80))
wednesday=element("./Images/wednesday.png",(100,150))

#list des joueurs et de leurs coordonnées 
lst_perso=[bombe,mage,singe,dustin_poirier,stone,serpent]
perso_x_y=[(110,540),(200,540),(320,540),(420,540),(530,540),(630,540)]


# Boucle de jeu
running = True
while running:
    # Evénements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Detecte si la souris est sur le rectangle Unit1
        if event.type == pygame.MOUSEBUTTONDOWN:  
            mouse_pos = pygame.mouse.get_pos()  
            if 100 <= mouse_pos[0] <= 300 and \
               430 <= mouse_pos[1] <= 630 :
                
                #integre le choix du joueurs dans le dictionnaire correspondant
                if choix_joueur["Joueur1"]=='' :
                    choix_joueur["Joueur1"]='Unit1'
                else :
                    choix_joueur["Joueur2"]='Unit1'
                choix_joueur_1=False
                choix_joueur_2=True

            if 310 <= mouse_pos[0] <= 510 and \
               430 <= mouse_pos[1] <= 630 :
                if choix_joueur["Joueur1"]=='' :
                    choix_joueur["Joueur1"]='Unit2'
                else :
                    choix_joueur["Joueur2"]='Unit2'
                choix_joueur_1=False
                choix_joueur_2=True
            
            if 520 <= mouse_pos[0] <= 720 and \
               430 <= mouse_pos[1] <= 630 :
                if choix_joueur["Joueur1"]=='' :
                    choix_joueur["Joueur1"]='Unit3'
                else :
                    choix_joueur["Joueur2"]='Unit3'
                choix_joueur_1=False
                choix_joueur_2=True



   
    
    #Affichage de toute les images et création des rectangls pour l'estethisme 
    screen.blit(fond_acceuil,(0,0))
    screen.blit(wednesday,(100,650))

    pygame.draw.rect(screen, (0,100,0), (100, 430, 200, 100))
    screen.blit(print_unit1,(152,465))
    pygame.draw.rect(screen, (0,100,0), (100, 530, 200, 100),3)

    pygame.draw.rect(screen, (150,0,0), (310, 430, 200, 100))
    screen.blit(print_unit2,(355,465))
    pygame.draw.rect(screen, (150,0,0), (310, 530, 200, 100),3)  

    pygame.draw.rect(screen, (0,0,255), (520, 430, 200, 100))
    screen.blit(print_unit3,(570,465))
    pygame.draw.rect(screen, (0,0,255), (520, 530, 200, 100),3)

    if choix_joueur_1 :
        screen.blit(image_text,(50,100))
    if choix_joueur_2 :
        screen.blit(image_text2,(50,100))

    pygame.draw.rect(screen, (0,100,0), (10, 205, 70, 30))
    screen.blit(Unit1_description,(90,200))
    screen.blit(Unit1_p_2,(90,220))
    

    pygame.draw.rect(screen, (150,0,0), (10, 270, 70, 30))
    screen.blit(Unit2_descripion,(90,265))
    screen.blit(Unit2_descripion_p_2,(90,285))

    pygame.draw.rect(screen, (0,0,255), (10, 335, 70, 30))
    screen.blit(Unit3_descripion,(90,330))
    screen.blit(Unit3_descripion_p_2,(90,350))   

    for i in range (len(lst_perso)) :
         screen.blit(lst_perso[i],perso_x_y[i])
    #arret de la boucle quand les perssonnages sont choisis
    if choix_joueur['Joueur1'] != '' and choix_joueur['Joueur2'] != '' :
        running=False



    # Mettre à jour l'affichage
    pygame.display.flip()
    

# Quitter Pygame
pygame.quit()
sys.exit()