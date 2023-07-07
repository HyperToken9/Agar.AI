
import pygame
import numpy as np
import time

# Parameters
BASE_SIZE   = 50.00
SIZE_FACTOR = 00.005

class Colony(pygame.sprite.Sprite):
    
    def __init__(self, id_number = 0, focus=False):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.id = id_number
        
        self.points = 0
        
        self.position = np.array([ 550, 500. ]) # x, y
        
        self.base_image = pygame.image.load("sprites/red.png")
        
        self.image = self.base_image

        print(type(self.image))

        self.rect = self.image.get_rect()

        # self.color = (255, 0, 0)
        
        self.focus = focus
        
        self.resize()

        # self.image.fill(self.color)
        
    def update(self, control_dicitonary):
        
        move_by = control_dicitonary.get(self.id, np.array([0, 0]))
        
        self.position += move_by
        
        # self.resize(point_shift = 2)
        
        # print(f"{self.position = }")
    
    def get_size(self):
        return BASE_SIZE + self.points * SIZE_FACTOR

    def resize(self):

        new_size = self.get_size()
        new_size = (new_size, new_size)

        center = self.rect.center
        self.image = pygame.transform.scale(self.base_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def eat(self, agars):

        # if len(agars) > 10:
        #     for agar in agars:
        #         print(agar.position)
        #     exit(0)

        for agar in agars:
    
            if not agar.alive():
                continue
            
            if not self.rect.contains(agar):
                # print("Not eating")
                continue 
            
            
            self.update_points(delta = agar.points)
            agar.kill()

    def update_points(self, delta = 0, new = -1):
        
        self.points += delta

        self.resize()


if __name__ == '__main__':
    
    print("Running player.py as main")
    
    