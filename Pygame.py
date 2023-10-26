from pygame import *
 
background = display.set_mode((800,800))
display.set_caption('Fire emblem')
init()
 
#les images
picture = image.load("./Images/Cadrillage.png")
picture = picture.convert_alpha()
picture=transform.scale(picture, (600, 600))

arbre = image.load("./Images/arbre.PNG")
arbre = arbre.convert_alpha()
arbre=transform.scale(arbre, (100, 100))

#les spritesheets
        
#paramètres de départ
jouer = True
 
#les fonctions du jeu
 
while jouer:
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()
    background.blit(picture, (100,100))
    background.blit(arbre, (0,100))
    display.flip()
quit()