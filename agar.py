import pygame
import numpy as np

class Agar(pygame.sprite.Sprite):
    
    def __init__(self, id_number = 0, focus=False):
        
        pygame.sprite.Sprite.__init__(self)
    
        self.points = 100
        
        self.position = np.array([ 25, 0. ]) # x, y
        
        self.image = pygame.image.load("sprites/agar.png")
        
        self.rect = self.image.get_rect()