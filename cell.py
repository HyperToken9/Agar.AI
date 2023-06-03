
import pygame
import numpy as np

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.points = 100
        
        self.position = np.array([ 50, 0. ]) # x, y
        
        self.image = pygame.Surface(self.get_size())

        self.rect = self.image.get_rect()
        
        self.color = (255, 0, 0)
        
        self.focus = True
        
        self.image.fill(self.color)
        
    def update(self, **kwargs):
        
        move_by = kwargs.get("move_by", np.array([0, 0]))
        
        # if self.focus:   
        #     # print('Moving by: ', move_by)
        #     self.position += move_by
        
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    
    def get_size(self):
        
        return [self.points, self.points]


if __name__ == '__main__':
    
    print("Running player.py as main")
    
    