from pygame import *
from packages import* 
 
background = display.set_mode((800,800))
display.set_caption('Fire emblem')
init()


picture=image.load("./Images/Cadrillage.PNG")
picture=picture.convert_alpha()
picture=transform.scale(picture,(600,600))

class Karim :
    def __init__(self,yes_or_no) :
        self.yes_or_no=yes_or_no
        if yes_or_no==True :

            self.bombe1 =self.element("./Images/bombe.PNG",(50,50))
            self.position_bombe1=(57,157)
            self.bombe1_get_rect=self.bombe1.get_rect()

            self.bombe2 =self.element("./Images/bombe.PNG",(50,50))

            self.position_bombe2=(157,157)

            self.bombe3 =self.element("./Images/bombe.PNG",(50,50))
            self.position_bombe3=(257,157)

            self.bombe4 =self.element("./Images/bombe.PNG",(50,50))
            self.position_bombe4=(357,157)

            self.bombe5 =self.element("./Images/bombe.PNG",(50,50))
            self.position_bombe5=(457,157)

            self.mohamed = self.element("./Images/mohamed.PNG",(50,50))
            self.position_mohamed=(357,257)

            self.mohamed2 = self.element("./Images/mohamed.PNG",(50,50))
            self.position_mohamed2=(457,257)

            self.list_position=[self.position_bombe1,self.position_bombe2,self.position_bombe3,self.position_bombe4,self.position_bombe5,self.position_mohamed,self.position_mohamed2]

        else :
            self.bombe1='None'
            self.bombe2='None'
            self.bombe3='None'
            self.bombe4='None'
            self.bombe5='None'
            self.mohamed='None'
            self.mohamed2='None'



        self.list_perso=[self.bombe1,self.bombe2,self.bombe3,self.bombe4,self.bombe5,self.mohamed,self.mohamed2]
        
    def element(self,chemin,tall) :
        var=image.load(chemin)
        var=var.convert_alpha()
        var=transform.scale(var,tall)
        return var


jouer = True
 
joueur1=Karim(True)

 
#les images
picture = image.load("./Images/Cadrillage.png")
picture = picture.convert_alpha()
picture=transform.scale(picture, (600, 600))


arbre = image.load("./Images/arbre.PNG")
arbre = arbre.convert_alpha()
arbre=transform.scale(arbre, (50, 50))


rocher = image.load("./Images/rocher.PNG")
rocher = rocher.convert_alpha()
rocher=transform.scale(rocher, (50, 50))


bombe = image.load("./Images/bombe.PNG")
bombe = bombe.convert_alpha()
bombe=transform.scale(bombe, (50, 50))


bombe2 = image.load("./Images/bombe.PNG")
bombe2 = bombe2.convert_alpha()
bombe2=transform.scale(bombe2, (50, 50))


bombe3 = image.load("./Images/bombe.PNG")
bombe3 = bombe3.convert_alpha()
bombe3=transform.scale(bombe3, (50, 50))


bombe4 = image.load("./Images/bombe.PNG")
bombe4 = bombe4.convert_alpha()
bombe4=transform.scale(bombe4, (50, 50))


bombe5 = image.load("./Images/bombe.PNG")
bombe5 = bombe5.convert_alpha()
bombe5=transform.scale(bombe5, (50, 50))


bombe5 = image.load("./Images/bombe.PNG")
bombe5 = bombe5.convert_alpha()
bombe5=transform.scale(bombe5, (50, 50))


mohamed = image.load("./Images/mohamed.PNG")
mohamed = mohamed.convert_alpha()
mohamed=transform.scale(mohamed, (50, 50))


mohamed2 = image.load("./Images/mohamed.PNG")
mohamed2 = mohamed2.convert_alpha()
mohamed2=transform.scale(mohamed2, (50, 50))


singe = image.load("./Images/singe.PNG")
singe = singe.convert_alpha()
singe=transform.scale(singe, (50, 50))


singe2 = image.load("./Images/singe.PNG")
singe2 = singe2.convert_alpha()
singe2=transform.scale(singe2, (50, 50))


singe3 = image.load("./Images/singe.PNG")
singe3 = singe3.convert_alpha()
singe3=transform.scale(singe3, (50, 50))


singe4 = image.load("./Images/singe.PNG")
singe4 = singe.convert_alpha()
singe4=transform.scale(singe4, (50, 50))







jouer = True
 
while jouer:
   
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()
             
    background.blit(picture,(100,100))
    if joueur1.yes_or_no==True :
        for i in range(len(joueur1.list_perso)) :
            background.blit(joueur1.list_perso[i], joueur1.list_position[i])
    
            
    
    
    background.blit(picture, (100,100))
    background.blit(arbre, (74,120))
    background.blit(rocher, (500,120))
    background.blit(bombe, (500,200))
    background.blit(bombe2, (600,200))
    background.blit(bombe3, (700,200))
    background.blit(bombe4, (600,300))
    background.blit(bombe5, (300,500))
    background.blit(mohamed, (400,500))
    background.blit(mohamed2, (450,500))
    background.blit(singe, (450,150))
    background.blit(singe2, (450,200))
    background.blit(singe3, (450,550))
    background.blit(singe4, (420,50))
   
    display.flip()
quit()