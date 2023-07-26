import time
import pygame
import numpy as np

from cell import Cell
from toolkit import ToolKit

# Parameters
ATTRACTION_C = 0.1
REPULSION_C = 2

class Player:

    def __init__(self, id, spawn_position, points = 0):
    
        self.cells = pygame.sprite.Group()

        self.cells.add(Cell(spawn_position.copy()))

        self.position_goal = spawn_position

    def update(self, commands):
        
        move_by = commands.get('move_by', np.array([0., 0.]))

        self.move_position_goal(move_by)

        if commands.get('split', False):
            print("splitting")
            self.split()
            print("Cell COunt ", len(self.cells))

        self.update_cells()

        # print("position_goal", self.position_goal)
        # print("cell position", self.cells.sprites()[0].position)
    
    def update_cells(self):
    
        # Move Towards Goal 
        self.move_cells()


    def move_cells(self):

        for cell in self.cells.sprites():
            
            # print(cell.position, cell.id)
            # print(type(self.cells))

            cell.move(self.position_goal - cell.position, 
                      sprite_group = self.cells)
    
    def split(self):
        self.cells.add(Cell(self.position_goal - np.array([100, 100])))

    def move_position_goal(self, move_by):

        #TODO: This should trickle down from the game object 
        #TODO: Hardcoding this for now
        arena_size = 1000
        # print("moving", move_by)
        self.position_goal += move_by

        if self.position_goal[0] < 0:
            self.position_goal[0] = 0

        if self.position_goal[1] < 0:
            self.position_goal[1] = 0

        if self.position_goal[0] > arena_size:
            self.position_goal[0] = arena_size

        if self.position_goal[1] > arena_size:
            self.position_goal[1] = arena_size

    def get_cells(self):
        return self.cells.sprites()

    def draw(self,screen):
        self.cells.draw(screen)
    


    # def move(self, move_by):
    #     arena_size = 1000
    #     factor = 1  # / (1 + self.points)
    #     magnitude = np.linalg.norm(move_by)
    #     if magnitude > 0.5:
    #         move_by /= magnitude
    #         move_by *= self.top_speed()
    #     self.position += move_by * factor
    #     size = self.get_size() / 2.1
    #     if self.position[0] - size < 0:
    #         self.position[0] = size
    #     if self.position[1] - size < 0:
    #         self.position[1] = size
    #     if self.position[0] + size > arena_size:
    #         self.position[0] = arena_size - size
    #     if self.position[1] + size > arena_size:
    #         self.position[1] = arena_size - size
