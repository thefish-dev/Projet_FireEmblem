import pygame
import sys

pygame.init()

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définir la taille de l'écran
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Détection de la touche Entrée (Pavé Numérique)")

# Définir la police
font = pygame.font.Font(None, 36)

kp_enter_pressed = False
print("huu")

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Touche Entrée du pavé numérique
                kp_enter_pressed = True
                print("yy")

        
    if kp_enter_pressed:
        text = font.render("Touche Entrée (Pavé Numérique) pressée!", True, BLACK)
        screen.blit(text, (100, 250))

    pygame.display.flip()