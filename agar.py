import pygame
import numpy as np
from random import choices

# Parameters
BASE_SIZE   = 10.00
SIZE_FACTOR = 00.02

class Agar(pygame.sprite.Sprite):
    
    def __init__(self, 
                 id_number = 0,
                 focus=False,
                 points = -1, 
                 position = np.array([ 500, 500. ])):
        
        pygame.sprite.Sprite.__init__(self)
    
        self.position = position # x, y
        
        self.base_image = pygame.image.load("sprites/agar.png")
        self.image = self.base_image
        
        self.rect = self.image.get_rect()

        self.points = points
        self.assign_points()
        self.resize()
        

    def assign_points(self):
        
        if self.points != -1:
            return

        distribution = range(50, 300)
        self.points = choices(distribution, distribution)[0]
        print(f"Points Assigned: {self.points }")

    def get_size(self):
        return BASE_SIZE + self.points * SIZE_FACTOR

    
    def resize(self):

        new_size = self.get_size()
        new_size = (new_size, new_size)

        center = self.rect.center
        self.image = pygame.transform.scale(self.base_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center


        