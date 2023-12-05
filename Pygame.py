from pygame import *
from packages import* 
from pygame import *
 
fenetre = display.set_mode((800,800))
display.set_caption('Tutoriel pygame')
init()
bleu=(0,255,255)
demande_start=font.SysFont("monospace",20)
image_text_start=demande_start.render('Quelle joueur voulez vous jouer ?', 1,bleu)

demande_perso1=font.SysFont("monospace",20)
image_text_pers_karim=demande_perso1.render('Karim', 1,bleu)





jouer = True

def element(chemin,tall) :
        var=image.load(chemin)
        var=var.convert_alpha()
        var=transform.scale(var,tall)
        return var
karim_bombe=element("./Images/bombe.PNG",(60,60))
karim_mohamed=element("./Images/mohamed.PNG",(60,60))

singe=element("./Images/singe.PNG",(60,60))
while jouer:
    surface = display.set_mode((800,800))
  

    color = (255,0,0)
  

    draw.rect(surface, color, Rect(200, 430, 140, 70))
    draw.rect(surface, (255,120,0), Rect(350, 430, 140, 70))
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()
    fenetre.blit(karim_bombe,(200,500))
    fenetre.blit(karim_mohamed,(260,500))
    fenetre.blit(image_text_start,(100,100))
    fenetre.blit(singe,(350,500))
    
    display.flip()