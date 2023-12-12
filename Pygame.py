import pygame
from pygame import *
import sys

# Initialisation de Pygame
pygame.init()
class Elem_Graphique(pygame.sprite.Sprite):
    
    def __init__(self,position_x,position_y,chemin):
        super().__init__()
        self.image= self.element(chemin,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = position_x # Position initiale x
        self.rect.y = position_y  # Position initiale y
    
    def bouger(self, deplacement_x, deplacement_y):
        self.rect.x += deplacement_x
        self.rect.y += deplacement_y

    def element(self,chemin,tall) :
        var=image.load(chemin)
        var=var.convert_alpha()
        var=transform.scale(var,tall)
        return var
    
bombe = Elem_Graphique(200,200,"./Images/bombe.png")
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fire emblem")
    
# Boucle de jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
            # Déplacement du sprite avec les touches directionnelles
            
    fenetre.fill((0,0,0))  # Remplir l'écran avec une couleur de fond
      # Dessiner tous les sprites
    fenetre.blit(bombe.image,(200,200))
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()