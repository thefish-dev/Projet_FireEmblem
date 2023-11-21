from pygame import *

bleu=(0,255,255)
background = display.set_mode((800,800))
display.set_caption('Fire emblem')
init()


demande=font.SysFont("monospace",20)
image_text=demande.render('Déplacer vous avec les fléches', 1,bleu)

msg_depart=demande.render('deplacer vous', True, bleu)
contour=image.load("./Images/contour.PNG")
contour=contour.convert_alpha()
contour=transform.scale(contour,(700,700))

picture=image.load("./Images/Cadrillage.PNG")
picture=picture.convert_alpha()
picture=transform.scale(picture,(600,600))

carre=image.load("./Images/carre.JPG")
carre=carre.convert_alpha()
carre=transform.scale(carre,(60,60))

def game(rect:list) :
    noir=(0,0,0)
    blanc=(255,255,255)
    draw.rect(background,noir,[rect[0],rect[1],60,60])
    while not K_KP_ENTER :
       if K_RIGHT :
           
           draw.rect(background,blanc,[rect[0],rect[1],60,60])
           rect[0]+=57
           if rect[0]>=700 :
               rect[0]=700
           draw.rect(background,noir,[rect[0],rect[1],60,60])
       if K_LEFT :
           draw.rect(background,blanc,[rect[0],rect[1],60,60])
           rect[0]-=57
           if rect[0]<= 100 :
               rect[0]=100
           draw.rect(background,noir,[rect[0],rect[1],60,60]) 
       if K_DOWN :
           draw.rect(background,blanc,[rect[0],rect[1],60,60])
           rect[1]+=57
           if rect[1]>=700 :
               rect[1]=700
           draw.rect(background,noir,[rect[0],rect[1],60,60])
       if K_UP :
           draw.rect(background,blanc,[rect[0],rect[1],60,60])
           rect[1]-=57
           if rect[1]<=100 :
               rect[1]
           draw.rect(background,noir,[rect[0],rect[1],60,60]) 
        
           



class Karim(sprite.Sprite) :
    def __init__(self,yes_or_no) :
        super().__init__()

        self.yes_or_no=yes_or_no
        if yes_or_no==True :

            self.bombe1 =self.element("./Images/bombe.PNG",(60,60))
            self.bombe1_rect=self.bombe1.get_rect()
            self.bombe1_rect.x=160
            self.bombe1_rect.y=160

            

            self.bombe2 =self.element("./Images/bombe.PNG",(60,60))
            self.bombe2_rect=self.bombe2.get_rect()
            self.bombe2_rect.x=460
            self.bombe2_rect.y=280

            self.bombe3 =self.element("./Images/bombe.PNG",(60,60))
            self.bombe3_rect=self.bombe3.get_rect()
            self.bombe3_rect.x=340
            self.bombe3_rect.y=520

            self.bombe4 =self.element("./Images/bombe.PNG",(60,60))
            self.bombe4_rect=self.bombe4.get_rect()
            self.bombe4_rect.x=220
            self.bombe4_rect.y=340

            self.bombe5 =self.element("./Images/bombe.PNG",(60,60))
            self.bombe5_rect=self.bombe5.get_rect()
            self.bombe5_rect.x=460
            self.bombe5_rect.y=460

            self.mohamed = self.element("./Images/mohamed.PNG",(60,60))
            self.mohamed_rect=self.mohamed.get_rect()
            self.mohamed_rect.x=520
            self.mohamed_rect.y=520

            self.mohamed2 = self.element("./Images/mohamed.PNG",(60,60))
            self.mohamed2_rect=self.mohamed2.get_rect()
            self.mohamed2_rect.x=580
            self.mohamed2_rect.y=580

            self.list_position=[self.bombe1_rect,self.bombe2_rect,self.bombe3_rect,self.bombe4_rect,self.bombe5_rect,self.mohamed_rect,self.mohamed2_rect]
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
joueur1_tour=True
joueur2_tour=False
 
while jouer:
   
    for events in event.get():
         if events.type == QUIT:
             jouer=False
             quit()
        
         elif events.type==KEYDOWN :
                if events.key==K_KP_ENTER :
                    joueur1.position_bombe1=(200,600)


    
    background.blit(contour,(50,50))
    for i in range(10) :
        for j in range(10) :
            background.blit(carre,((100+j*60),(100+i*60)))
    background.blit(image_text,(220,20))
    if joueur1.yes_or_no==True :
        for i in range(len(joueur1.list_perso)) :
            background.blit(joueur1.list_perso[i], joueur1.list_position[i])
        game(joueur1.bombe1_rect)
   

    
    
            
    
    
    display.flip()
quit()