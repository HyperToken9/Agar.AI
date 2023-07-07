import pygame
import numpy as np

class Agar(pygame.sprite.Sprite):
    
    def __init__(self, id_number = 0, focus=False, position = np.array([ 500, 500. ])):
        
        pygame.sprite.Sprite.__init__(self)
    
        self.points = 100
        
        self.position = position # x, y
        
        self.image = pygame.image.load("sprites/agar.png")
        
        self.rect = self.image.get_rect()

        self.BASE_SIZE = self.image.get_size()[0]
        self.SIZE_FACTOR = 0.1

    def get_size(self):

        return self.BASE_SIZE + self.points * self.SIZE_FACTOR

