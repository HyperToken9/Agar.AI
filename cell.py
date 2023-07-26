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
P_TERM = 0.1


CELL_ID = 0

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, position, points= 1000):

        pygame.sprite.Sprite.__init__(self)
        
        global CELL_ID

        self.id = CELL_ID
        CELL_ID += 1

        self.points = points
        
        self.velocity = np.array([0, 0], dtype = np.float64) #BUG: When not set to Zero initally

        self.position = position # x, y
        
        self.base_image = pygame.image.load("sprites/red.png")
        
        self.image = self.base_image

        self.rect = self.image.get_rect()
        
        self.rect.center = self.position
        # self.color = (255, 0, 0)
        
        self.mask = pygame.mask.from_surface(self.image)

        self.resize()

        # self.image.fill(self.color)

    def move(self, velocity_goal = np.array([0, 0]), sprite_group = None):
        """
            Moves the cell towards the goal position
                Given by kwargs: "to"
            Shift by
                Given by kwargs: "by"
        """
        
        global P_TERM

        delta_position = velocity_goal - self.velocity

        delta_position *= P_TERM

        magnitude = np.linalg.norm(delta_position)
        
        if magnitude < 1e-4:
            return

        scaled_magnitude = min(magnitude, self.top_speed())

        delta_position *= scaled_magnitude / magnitude



        # Obstacle Avoidance
        if sprite_group is not None:
            
            hit_list = pygame.sprite.spritecollide(self, sprite_group, False)
            
            for sprite in hit_list:

                if sprite is self:
                    continue
                print(sprite)

                collision_vector = sprite.position - self.position

                collision_magnitude = np.linalg.norm(collision_vector)

                avoidance = np.dot(collision_vector, delta_position) / collision_magnitude

                avoidance = max(0, avoidance)

                avoidance = collision_vector * avoidance / collision_magnitude

                delta_position -= avoidance

        magnitude = np.linalg.norm(delta_position)

        if magnitude < 1e-1:
            return
        
        self.position += delta_position
        
    
    def update(self, control_dicitonary):
        
        player_control = control_dicitonary.get(self.id, {}) # np.array([0, 0]))

        move_by = player_control.get("move", np.array([0, 0]))

        split = player_control.get("split", False)

        if split:
            print("Why cant i split??")

        self.move(move_by)        
    
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
        
    def eat(self, game_objects):

        for obj in game_objects:
            
            if obj is self:
                continue

            if not obj.alive():
                continue
            
            if not self.rect.contains(obj):
                continue 
            
            self.update_points(delta = obj.points)

            obj.kill()

    def top_speed(self):
        global MIN_SPEED, MAX_SPEED, CURVE
        return MIN_SPEED + (MAX_SPEED - MIN_SPEED) * np.exp(-CURVE * self.points)
    
    def update_points(self, delta = 0, new = -1):
        
        self.points += delta

        self.resize()

    def is_intersecting(self, other, **kwargs):

        move_by = kwargs.get("move_by", np.array([0, 0]))
        
        distance = dist(self.position + move_by, other.position)
        
        return self.get_size() / 2 + other.get_size() / 2 > distance
        





        




if __name__ == '__main__':
    
    print("Running player.py as main")
    
    