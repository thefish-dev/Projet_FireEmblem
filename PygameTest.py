
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Fire emblem')
clock = pygame.time.Clock()
demande = pygame.font.SysFont("monospace",20)

# Constants
colors = {
    "blue" : (0,255,255),
    "red" : (255,0,0)
}
deplacement = 57

# Components
image_text = demande.render('Déplacer vous avec les fléches', 1, colors["blue"])

msg_depart=demande.render('deplacer vous', True, colors["blue"])
contour = pygame.image.load("./Images/contour.PNG")
contour = contour.convert_alpha()
contour = pygame.transform.scale(contour,(700,700))

picture = pygame.image.load("./Images/Cadrillage.PNG")
picture = picture.convert_alpha()
picture = pygame.transform.scale(picture,(600,600))

carre = pygame.image.load("./Images/carre.JPG")
carre = carre.convert_alpha()
carre = pygame.transform.scale(carre,(60,60))


class Sprite(pygame.sprite.Sprite) :
    def __init__(self, yes_or_no) :
        super().__init__()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0

def game() :
    noir=(0,0,0)
    blanc=(255,255,255)
    #pygame.draw.rect(screen,noir,[rect[0],rect[1],60,60])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    """
        if events.type==KEYDOWN :
            if events.key == K_RIGHT :
                pygame.draw.rect(background,blanc,[rect[0],rect[1],60,60])
                rect[0]+=deplacement
                if rect[0]>=700 :
                    rect[0]=700
                draw.rect(background,noir,[rect[0],rect[1],60,60])
            if events.key == K_LEFT :
                draw.rect(background,blanc,[rect[0],rect[1],60,60])
                rect[0]-=deplacement
                if rect[0]<= 100 :
                    rect[0]=100
                draw.rect(background,noir,[rect[0],rect[1],60,60]) 
            if events.key == K_DOWN :
                draw.rect(background,blanc,[rect[0],rect[1],60,60])
                rect[1]+=deplacement
                if rect[1]>=700 :
                    rect[1]=700
                draw.rect(background,noir,[rect[0],rect[1],60,60])
            if events.key == K_UP :
                draw.rect(background,blanc,[rect[0],rect[1],60,60])
                rect[1]-=deplacement
                if rect[1]<=100 :
                    rect[1]
                draw.rect(background,noir,[rect[0],rect[1],60,60]) 
            """
    
running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.circle(screen, "red", tuple(player_pos), 40)
    game()

    screen.blit(contour,(50,50))
    for x in range(10) :
        for y in range(10) :
            screen.blit(carre,((100+x*60),(100+y*60)))
            
    screen.blit(image_text,(220,20))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()