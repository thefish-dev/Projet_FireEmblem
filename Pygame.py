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
 
while jouer:
   
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()
    background.blit(picture,(100,100))
    if joueur1.yes_or_no==True :
        for i in range(len(joueur1.list_perso)) :
            background.blit(joueur1.list_perso[i], joueur1.list_position[i])
    
            
    
    
    display.flip()
quit()