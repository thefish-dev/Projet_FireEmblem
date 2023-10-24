from Pygame import *

import Pygame
Pygame.init()

sources_path = "./Images/"
screen = Pygame.display.set_mode([800, 800])
picture=Pygame.image.load(sources_path +"Cadrillage.png")
picture_use=picture.convert
running = True
while running:
    screen.fill((255, 255, 255))
    picture.blit(picture_use,(0,0))

    
    for event in Pygame.event.get():
        if event.type == Pygame.QUIT:
            running = False
    
    
    
    Pygame.display.flip()


Pygame.quit()