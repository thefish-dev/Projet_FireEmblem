import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clic sur un rectangle Pygame")

# Couleurs
background_color = (255, 255, 255)
rectangle_color = (0, 0, 255)  # Bleu
highlight_color = (255, 0, 0)  # Rouge pour mettre en évidence

# Position et taille du rectangle
rectangle_width = 100
rectangle_height = 50
rectangle_x = (screen_width - rectangle_width) // 2
rectangle_y = (screen_height - rectangle_height) // 2

# Boucle de jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Vérification du clic de souris
            mouse_pos = pygame.mouse.get_pos()  # Récupère la position de la souris
            if rectangle_x <= mouse_pos[0] <= rectangle_x + rectangle_width and \
               rectangle_y <= mouse_pos[1] <= rectangle_y + rectangle_height:
                # Vérifie si la souris est dans le rectangle
                print("Clic sur le rectangle!")

    # Affichage de la couleur de fond
    screen.fill(background_color)

    # Dessiner le rectangle
    pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()