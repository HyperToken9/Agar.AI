
import pygame
import numpy as np

class Colony(pygame.sprite.Sprite):
    
    def __init__(self, id_number = 0, focus=False):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.id = id_number
        
        self.points = 100
        
        self.position = np.array([ 50, 0. ]) # x, y
        
        self.image = pygame.image.load("sprites/red.png")

        self.rect = self.image.get_rect()
        
        # self.color = (255, 0, 0)
        
        self.focus = focus
        
        # self.image.fill(self.color)
        
    def update(self, control_dicitonary):
        
        move_by = control_dicitonary.get(self.id, np.array([0, 0]))
        
        self.position += move_by
        
        self.resize(point_shift = 2)
        
        
        
        # print(f"{self.position = }")
        
        # move_by = kwargs.get("move_by", np.array([0, 0]))
        # if self.focus:   
        #     # print('Moving by: ', move_by)
        #     self.position += move_by
        # self.rect.x = self.position[0]
        # self.rect.y = self.position[1]

    def resize(self, point_shift):
        
        # center = self.rect.center
        print("Before", self.rect.center)
        self.rect = self.rect.inflate(point_shift, point_shift)
        print("After", self.rect.center)
        # self.rect.center = center
        
    
    def get_size(self):
        
        return [self.points, self.points]


if __name__ == '__main__':
    
    print("Running player.py as main")
    
    