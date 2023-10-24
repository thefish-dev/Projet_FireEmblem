from Pygame import *

import pygame
pygame.init()


screen = pygame.display.set_mode([800, 800])
picture=pygame.image.load('./Image/Cadrillage.png')
picture_use=picture.convert
running = True
while running:
    screen.fill((255, 255, 255))
    picture.blit(picture_use,(0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    pygame.display.flip()


pygame.quit()