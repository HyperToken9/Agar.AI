
import pygame
import numpy as np
import time

from agar import Agar

# Parameters
BASE_SIZE   = 50.000
SIZE_FACTOR = 00.005

cell_id = 0

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, position, points= 0, focus=False):

        pygame.sprite.Sprite.__init__(self)
        
        global cell_id

        self.id = cell_id

        cell_id += 1

        self.points = points
        
        self.position = position # x, y
        
        self.base_image = pygame.image.load("sprites/red.png")
        
        self.image = self.base_image

        self.rect = self.image.get_rect()
        self.rect.center = self.position
        # self.color = (255, 0, 0)
        
        self.focus = focus
        
        self.resize()

        # self.image.fill(self.color)

    def move(self, move_by):

        arena_size = 1000

        factor = 1 # / (1 + self.points)

        magnitude = np.linalg.norm(move_by)

        if magnitude > 0.5:
            move_by /= magnitude
            move_by *= self.top_speed()


        self.position += move_by * factor

        size = self.get_size() / 2.1

        if self.position[0] - size < 0:
            self.position[0] = size
        
        if self.position[1] - size < 0:
            self.position[1] = size

        if self.position[0] + size > arena_size:
            self.position[0] = arena_size - size
        
        if self.position[1] + size > arena_size:
            self.position[1] = arena_size - size
    
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
        MIN_SPEED = 0.5
        MAX_SPEED = 5.0
        CURVE = 0.0001 # Decrease to make curve smoother
        return MIN_SPEED + (MAX_SPEED - MIN_SPEED) * np.exp(-CURVE * self.points)
    
    def update_points(self, delta = 0, new = -1):
        
        self.points += delta

        self.resize()


if __name__ == '__main__':
    
    print("Running player.py as main")
    
    