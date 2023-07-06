
import pygame
import numpy as np

class Colony(pygame.sprite.Sprite):
    
    def __init__(self, id_number = 0, focus=False):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.id = id_number
        
        self.points = 0
        
        self.position = np.array([ 45, 0. ]) # x, y
        
        self.base_image = pygame.image.load("sprites/red.png")
        
        self.image = self.base_image

        print(type(self.image))

        self.rect = self.image.get_rect()

        # self.color = (255, 0, 0)
        
        self.focus = focus
        
        self.SIZE_FACTOR = 0.01
        self.BASE_SIZE = self.image.get_size()[0]
        # self.image.fill(self.color)
        
    def update(self, control_dicitonary):
        
        move_by = control_dicitonary.get(self.id, np.array([0, 0]))
        
        self.position += move_by
        
        # self.resize(point_shift = 2)
        
        # print(f"{self.position = }")
        

    def resize(self):

        new_size = self.BASE_SIZE + self.points * self.SIZE_FACTOR
        new_size = (new_size, new_size)

        center = self.rect.center
        self.image = pygame.transform.scale(self.base_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def check_eaten(self, agars):

        for agar in agars:
    
            if not self.rect.contains(agar):
                # print("Not eating")
                continue 
            
            # Else Add points
            print("Eating", agar)
            
            self.update_points(delta = agar.points)
            agar.kill()

    def update_points(self, delta = 0, new = -1):

        self.points += delta

        self.resize()


    def get_size(self):
        
        return [self.points, self.points]


if __name__ == '__main__':
    
    print("Running player.py as main")
    
    