import pygame
import colorsys
import cv2 as cv
import numpy as np
import pygame.gfxdraw
from random import random
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
        
        self.generate_sprite()
        # pygame.gfxdraw.filled_circle(
        #     self.base_image, 20, 20, 20, (255, 0, 100, 255))

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
        # print(f"Points Assigned: {self.points }")

    def get_size(self):
        return BASE_SIZE + self.points * SIZE_FACTOR

    
    def resize(self):

        new_size = self.get_size()
        new_size = (new_size, new_size)

        center = self.rect.center
        self.image = pygame.transform.scale(self.base_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center


    def generate_sprite(self):

        size = self.base_image.get_size()[0]
        d = size // 2
        
        hue = random()
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        color = np.array((r, g, b, 1)) * 255
        pygame.gfxdraw.filled_circle(self.base_image, d, d, d, color)
