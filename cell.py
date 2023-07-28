import time
import pygame
import numpy as np
from math import dist

from agar import Agar

# Parameters
BASE_SIZE   = 50.000
SIZE_FACTOR = 00.005

# Speed Parameters
MIN_SPEED = 0.5
MAX_SPEED = 5.0
CURVE = 0.0001  # Decrease to make speed curve smoother
P_TERM = 0.05

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, player_id, cell_id, position, points= 1000):

        pygame.sprite.Sprite.__init__(self)
        
        self.player_id = player_id 

        self.cell_id = cell_id

        self.points = points
        
        self.velocity = np.array([0, 0], dtype = np.float64) 

        self.position = position # x, y
        
        self.base_image = pygame.image.load("sprites/red.png")
        
        self.image = self.base_image

        self.rect = self.image.get_rect()
        
        self.rect.center = self.position
        # self.color = (255, 0, 0)
        
        self.mask = pygame.mask.from_surface(self.image)

        self.resize()

        # self.image.fill(self.color)

    def move(self, position_goal, sprite_group = None):
    
        global P_TERM

        # print(self.velocity)
        # print(self.position)
        
        direction_vector = position_goal - self.position

        self.velocity = (self.velocity + direction_vector) * P_TERM
        
        delta_position = self.velocity
        
        # Obstacle Avoidance
        #BUG: Better math should fix the jittery movement
        #TODO: Make this a function self.validate_step()
        if sprite_group is not None:
            
            hit_list = pygame.sprite.spritecollide(self, sprite_group, False)
            
            for sprite in hit_list:

                if sprite is self:
                    continue

                collision_vector = sprite.position - self.position

                collision_magnitude = np.linalg.norm(collision_vector)

                avoidance = np.dot(collision_vector, delta_position) / collision_magnitude

                avoidance = max(0, avoidance)

                avoidance = collision_vector * avoidance / collision_magnitude

                delta_position -= avoidance

        #BUG: Happened Once Should Look into it
        if any(np.isnan(delta_position)):
            print("NAN", delta_position)
            return

        magnitude = np.linalg.norm(delta_position)
        
        if magnitude < 1e-4:
            return
        
        scaled_magnitude = min(magnitude, self.top_speed())

        delta_position *= scaled_magnitude / magnitude

        self.position += delta_position

    def get_size(self):
        return BASE_SIZE + self.points * SIZE_FACTOR

    def resize(self):

        new_size = self.get_size()
        new_size = (new_size, new_size)

        center = self.rect.center
        self.image = pygame.transform.scale(self.base_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pygame.mask.from_surface(self.image)
        
    def eat(self, game_objects= []):        
        
        for obj in game_objects:

            if not obj.alive():
                continue
            
            if not self.rect.contains(obj):
                continue 
            
            if isinstance(obj, Cell) and obj.player_id == self.player_id:
                continue
            
            if not self.alive():
                continue

            self.update_points(delta=obj.points)

            obj.kill()
        


    def top_speed(self):
        global MIN_SPEED, MAX_SPEED, CURVE
        return MIN_SPEED + (MAX_SPEED - MIN_SPEED) * np.exp(-CURVE * self.points)
    
    def update_points(self, delta = 0, new = -1):        
        
        self.points += delta

        self.resize()




if __name__ == '__main__':
    
    print("Running player.py as main")
    
    