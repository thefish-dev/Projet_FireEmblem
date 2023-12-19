import pygame
from pygame import *
import sys
from random import randint
from fonctions_pygame import *
from packages.Unit import *





# Initialisation de Pygame
pygame.init()

#Class pour les élements interactif homme machine
class Elem_Graphique(pygame.sprite.Sprite):
    def __init__(self,position_x,position_y,chemin):
        super().__init__()
        self.image= element(chemin,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = position_x # Position initiale x
        self.rect.y = position_y  # Position initiale y
        self.position_elem=(self.rect.x,self.rect.y)
        self.chemin=chemin
       
    
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
 

#Pour l'affichage du text
choix_joueur_1=True
choix_joueur_2=False

#Dictionnaire avec les unités choisit par les joueurs
choix_joueur= {
     "Joueur1" : None,
     "Joueur2" :None
}

#Création de la fenétre
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fire emblem")

#Dictionnaire avec les couleurs
colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0),
    "vert" :(0,255,0),
    "black" : (0,0,0),
    "white" : (255,255,255)
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
affichage_erreur=pygame.font.SysFont("chemin_vers_ta_police_en_gras.ttf",30)
demande_perso = pygame.font.SysFont("monospace",30)
text=pygame.font.SysFont("monospace",25)

#Question de choix des joueurs
image_text = demande_perso.render('Joueur 1 :choisissez votre personnage ', True, colors["blue"])
image_text2 = demande_perso.render('Joueur 2 :choisissez votre personnage ', True, colors["blue"])


#Text qui affiche quelle joueur doit jouer
tour_joueur1=text.render("Joueur 1 :c est a vous de jouer CHEF", True, colors["blue"])
tour_joueur2=text.render("Joueur 2 :c est a vous de jouer CHEF", True, colors["blue"])





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



text_erreur_joueur=affichage_erreur.render('Equipe déja choisit par le joueur 1',True, colors["white"])
text_erreur='Equipe déja choisit par le joueur 1'
text_erreur_f=''
affichage_text_erreur_joueur=False

text_abilities=description.render("Votre joueur adverse peut utiliser une de ses abillités pour se défendre :",True,colors["white"])




#Chargement des images
fond_acceuil=element("./Images/fond_acceuil.jpg",(800,800))
bombe=element("./Images/bombe.png",(80,80))
mage=element("./Images/mage.png",(80,80))
serpent=element("./Images/serpent.png",(80,80))
stone=element("./Images/stone.png",(80,80))
dustin_poirier=element("./Images/dustin_poirier.png",(80,80))
singe=element("./Images/singe.png",(80,80))
wednesday=element("./Images/wednesday.png",(100,150))
can_attack=False

#Position des unités à l'initialisation
unit1_position=[(100,100),(160,100),(400,100),(580,100),(640,100),(340,160),(400,160)]
unit_position2=[(100,640),(160,640),(400,640),(580,640),(640,640),(340,580),(400,580)]


#List de unités en fonctions du perssonnage choisit
joueur1_unit1=[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/bombe.png") for i in range (5)]+[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/mage.png") for i in range (5,7)]

joueur1_unit2=[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/singe.png") for i in range (4)]+[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/dustin_poirier.png") for i in range (4,7)]

joueur1_unit3=[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/stone.png") for i in range (2)]+[Elem_Graphique(unit1_position[i][0],unit1_position[i][1],"./Images/serpent.png") for i in range (2,7)]

joueur2_unit1=[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/bombe.png") for i in range (5)]+[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/mage.png") for i in range (5,7)]

joueur2_unit2=[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/singe.png") for i in range (4)]+[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/dustin_poirier.png") for i in range (4,7)]

joueur2_unit3=[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/stone.png") for i in range (2)]+[Elem_Graphique(unit_position2[i][0],unit_position2[i][1],"./Images/serpent.png") for i in range (2,7)]

#Variabe qui permettront d'afficher un text pdt un certain temps
temp_final=0
temp_actuel=0


#list des joueurs et de leurs coordonnées 
lst_perso=[bombe,mage,singe,dustin_poirier,stone,serpent]
perso_x_y=[(110,540),(200,540),(320,540),(420,540),(530,540),(630,540)]

# Musique du menu
pygame.mixer.music.load ("sounds/menu.mp3") 
pygame.mixer.music.play(-1)

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
                if choix_joueur["Joueur1"]==None :
                    choix_joueur["Joueur1"]=joueur1_unit1
                else :
                    if choix_joueur["Joueur1"]!= joueur1_unit1 :
                        choix_joueur["Joueur2"]=joueur2_unit1
                    else : 
                        temp_final= 3000
                choix_joueur_1=False
                choix_joueur_2=True
            

            
            if 310 <= mouse_pos[0] <= 510 and \
               430 <= mouse_pos[1] <= 630 :
                if choix_joueur["Joueur1"]==None :
                    choix_joueur["Joueur1"]=joueur1_unit2
                else :
                    if choix_joueur["Joueur1"]!= joueur1_unit2 :
                        choix_joueur["Joueur2"]=joueur2_unit2
                    else : 
                        temp_final= 3000
                choix_joueur_1=False
                choix_joueur_2=True
            if 520 <= mouse_pos[0] <= 720 and \
               430 <= mouse_pos[1] <= 630 :
                if choix_joueur["Joueur1"]==None :
                    choix_joueur["Joueur1"]=joueur1_unit3
                else :
                    if choix_joueur["Joueur1"]!= joueur1_unit3 :
                        choix_joueur["Joueur2"]=joueur2_unit3
                    else : 
                        temp_final= 3000
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
    #Affichage d'un text temporaire d'erreur
    if temp_final!=0 :        
        temp_actuel=pygame.time.get_ticks()
        screen.blit(text_erreur_joueur,(250,700))

    if temp_final<temp_actuel :
        text_erreur_joueur=description.render(text_erreur_f,False, colors["black"])
        
    #arret de la boucle quand les perssonnages sont choisis
    if choix_joueur['Joueur1'] != None and choix_joueur['Joueur2'] != None :
        running=False

    # Mettre à jour l'affichage
    pygame.display.flip()
    

# Quitter Pygame
pygame.quit()

# Musique du menu




playing=True 

pygame.init()


#Création de la fenetre jeu
background = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Fire emblem")

carre=element("./Images/carre.JPG",(60,60))
contour=element("./Images/contour.png",(700,700))
fond = element("./Images/fond.png",(800,800))
   

 

    
#Création d'un elist contenant les différents obstacles
lst_obstacle=["./Images/rocher.png","./Images/sapin.png","./Images/arbre.png","./Images/circulation.png","./Images/chien_arthur.png"]
for i in range (len(lst_obstacle)) :
    lst_obstacle[i]=element(lst_obstacle[i],(60,60))

lst_position_obstacle=[]

#Création d'une list qui contient des coordonnées aléatoires pour les obstacles qui sont différentes de celle des unités
while len(lst_position_obstacle) <5 :
    essaie=create_obstacle(choix_joueur)
    if essaie  not in lst_position_obstacle :
        lst_position_obstacle.append(essaie)


#Création des list des coordonnées des perssonnages qui permettront de les afficher au bonne endroit durant le déroulement du jeu
lst_position_joueur_1=[]
lst_position_joueur_2=[]
for i in range (len(choix_joueur["Joueur1"])) :
    lst_position_joueur_1.append((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y))
for i in range (len(choix_joueur["Joueur2"])) :
    lst_position_joueur_2.append((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y))


#Création des variables ainsi que les élements graphiques qui nous seront necessaire pour le jeu
attaque=0
attack_time=0
abilities_graphique=False
clique_droit=0
case_maxi=4
choix_tour_joueur="Joueur1"
choix_autre_joueur="Joueur2"
running_attack=True
changement_joueur=False
fond_attaque=element("./Images/fond_attaque.png",(700,800))
wednesday_attack=element("./Images/mercredi.png",(120,200))
fond_abilities=element("./Images/fond_abilités.png",(700,800))
thing=element("./Images/the_thing.png",(40,40))
bulle=element("./Images/bulle.png",(170,135))
text_bulle=element("./Images/text_bulle.png",(120,60))
hyde=element("./Images/hyde.png",(700,800))
sang=element("./Images/sang.png",(150,100))
text_hyde=element("./Images/text_hyde.png",(140,40))
bulle2=element("./Images/bulle.png",(240,190))


# Musique du jeu
pygame.mixer.music.load("sounds/fight_music.mp3")
pygame.mixer.music.play(-1)

# Boucle de jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Si on touche à un boutton de la souris
        if event.type == pygame.MOUSEBUTTONDOWN: 
            #Si l'on appuie sur le clique gauche de la souris 
            if event.button==pygame.BUTTON_LEFT :
            #On demande au joueur de cliquer sur l'unité qu'il veut déplacer, s'il s'agit d'une de ses unité, alors il peut la déplacer
            #si la distance entre ses coordonnée de base et el les coordonnées voulu sont inferieur ou égale au déplacement max 
            #de l'unité alors cette derniére se déplace
            #Par la suite on vérifie si une unité adverse est assez proche pour qu'il puisse l'attaqué, si oui alors on met la variable
            #permettant d'afficher les attaques à 1, sinon c'est au tour du joueur 2 de jouer, on fait cela grace aux variable 
            #Choix_tour_joueur et choix_autre_joueur
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
                            deplacement=deplacemet_total(coordonate_base,coordonate_want)
                            if case_max<=case_maxi :
                                
                                if detecte_obstacle(choix_joueur,lst_position_obstacle,coordonate_want)  :
                                    if choix_tour_joueur=="Joueur1" :
                                        if coordonate_base in lst_position_joueur_1 :
                                            

                                            lst_position_joueur_1=modificate_list_position(lst_position_joueur_1,coordonate_base,coordonate_want)
                                            

                                            choix_joueur[elem_move[1]][elem_move[0]]=modificate_place(choix_joueur[elem_move[1]][elem_move[0]],deplacement)
                                            if close_elem_of_unit(coordonate_want,"Joueur2",choix_joueur,1) != [] :
                                                
                                                attaque=1
                                                if changement_joueur==True :
                                                    choix_tour_joueur="Joueur2"
                                                    choix_autre_joueur="Joueur1"
                                            else :
                                                choix_tour_joueur="Joueur2"
                                                choix_autre_joueur="Joueur1"
                                    elif choix_tour_joueur=="Joueur2" :
                                        if coordonate_base in lst_position_joueur_2 :
                                        
                                            lst_position_joueur_2=modificate_list_position(lst_position_joueur_2,coordonate_base,coordonate_want)

                                            choix_joueur[elem_move[1]][elem_move[0]]=modificate_place(choix_joueur[elem_move[1]][elem_move[0]],deplacement)
                                            if close_elem_of_unit(coordonate_want,"Joueur1",choix_joueur,1) != [] :
                                                attaque=1 
                                                if changement_joueur==True : 
                                                    choix_tour_joueur="Joueur1" 
                                                    choix_autre_joueur="Joueur2"
                                            else :
                                                choix_tour_joueur="Joueur1" 
                                                choix_autre_joueur="Joueur2"                               
                                                    
            #Vérifie si l'on appuie sur le clique droit de la souris                                        
            if event.button== BUTTON_RIGHT :
                coordonate_attack=pygame.mouse.get_pos()
                coordonate_attack=search_coordinate(coordonate_attack)
                print(coordonate_attack)
                print(choix_tour_joueur)
                lst=[]
                for i in range (len(choix_joueur[choix_tour_joueur])) :
                    lst.append((choix_joueur[choix_autre_joueur][i].rect.x,choix_joueur[choix_autre_joueur][i].rect.y))
                print(lst)
                if coordonate_attack in lst :
                    print("dfhdfh")
                    can_attack=True
        #Verifie si une touche de clavier est presser
        if event.type==pygame.KEYDOWN :
            #Vérifie si la touche espace est pressée
            if event.key==pygame.K_SPACE :
                #Prend en compte les coordonnées de la souris et verifie si elle correspone à l'emplacement d'une attaque
                #Si oui alors met la variable qui permet l'affichage des abilités sur vrai
                if can_attack :
                    attack_finish=pygame.mouse.get_pos()
                    
                    if 810 <= attack_finish[0] <= 870 and \
                    100 <= attack_finish[1] <= 130 :
                        abilities_graphique=True
                    if 810 <= attack_finish[0] <= 870 and \
                    200 <= attack_finish[1] <= 230 :
                        abilities_graphique=True
                    can_attack=False

                    attaque=0
            
            #Vérifie si la touche (a) du clavier est presser        
            if event.key==pygame.K_a :
                #Prend en compte les coordonnées de la souris et verifie si elle correspone à l'emplacement d'une abilité
                #Si oui alors met la variable qui permet l'affichage des abilités sur vrai et aprés rien du tout parce que 
                #un membre du groupe n'a pas travailler 

                print("poli")

                abilities_finish=pygame.mouse.get_pos()
                good_abilities=0
                if 807 <= attack_finish[0] <= 867 and \
                    200 <= attack_finish[1] <= 230 :

                    good_abilities=1
                
                if 807 <= attack_finish[0] <= 867 and \
                270 <= attack_finish[1] <= 300 :
                        
                        good_abilities=1
                print(good_abilities)
                if good_abilities==1 :

                    print("2")
                    abilities_graphique=False
                    ataque=0
            
                    choix_tour_joueur,choix_autre_joueur=choix_autre_joueur,choix_tour_joueur

                                                          
                
    #On affiche le fond           
    background.fill((0,0,0)) 
    background.blit(fond,(0,0))
    background.blit(contour,(50,50))

    #On affiche les unités des joueurs au coordonnées respective
    for i in range(10) :
        for j in range(10) :
            background.blit(carre,((100+j*60),(100+i*60)))
    for i in range (len(choix_joueur["Joueur1"])) :
        background.blit(choix_joueur["Joueur1"][i].image,(choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y))
    for i in range (len(choix_joueur["Joueur2"])) :
        background.blit(choix_joueur["Joueur2"][i].image,(choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y))
    #On affiche les obstacles
    for i in range (len(lst_obstacle)) :
        background.blit(lst_obstacle[i],(lst_position_obstacle[i][0],lst_position_obstacle[i][1]))
    #Si aucune attaque ni abilités n'est en cour alors on affiche un fond spécifique
    if attaque==0 and abilities_graphique== False :
        background.blit(hyde,(800,0))
        background.blit(bulle2,(1255,220))
        background.blit(sang,(1300,250))
        background.blit(text_hyde,(1310,285))
    #On affiche quelle joueur doit jouer
    if choix_tour_joueur=="Joueur1" :
        background.blit(tour_joueur1,(130,20))

    if choix_tour_joueur=="Joueur2" :
        background.blit(tour_joueur2,(130,20))

    #On propose les attaques de l'unité jouer
    if attaque==1 :
        
        background.blit(fond_attaque,(800,0))
        background.blit(wednesday_attack,(900,600))
        background.blit(thing,(1150,560))
        background.blit(bulle,(970,480))
        background.blit(text_bulle,(1000,510))
        pygame.draw.rect(background, (255,0,0), (810, 100, 60, 30))
        pygame.draw.rect(background, (0,255,0), (810, 200, 60, 30)) 
        a=search_element(choix_joueur,coordonate_want)
        for i in range (5) :
            background.blit(affiche_attaque(corespondance(choix_joueur,a)[0],corespondance(choix_joueur,a)[1])[i],position_attaque[i])
        health_bar(background,choix_joueur,choix_tour_joueur)
        if abilities_graphique==True :
            attaque=0


    #On affiche les abilités du joueur adverse
    if abilities_graphique==True :
        
        background.blit(fond_abilities,(800,0))
        background.blit(text_abilities,(820,45))
        stock_abilities=search_element(choix_joueur,coordonate_attack)
        print(stock_abilities)
        pygame.draw.rect(background,(100,0,90),(807,200,60,30))
        
        print(corespondance(choix_joueur,stock_abilities)[0])
        print(corespondance(choix_joueur,stock_abilities)[1])
        if corespondance(choix_joueur,stock_abilities)[1]!="dustin_poirier" or corespondance(choix_joueur,stock_abilities)[1]!="singe" :
            pygame.draw.rect(background,(100,200,0),(807,270,60,30))

        print(position_attaque)
        for i in range(4) :
            background.blit(affiche_abillities(corespondance(choix_joueur,stock_abilities)[0],corespondance(choix_joueur,stock_abilities)[1])[i],position_abilities[i])
        if attaque==1 :
            abilities_graphique=False
        
    
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()

sys.exit()
