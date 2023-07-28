import time
import pygame
import numpy as np

from cell import Cell
from toolkit import ToolKit

# Parameters
ATTRACTION_C = 0.1
REPULSION_C = 2

class Player:

    def __init__(self, player_id, spawn_position, raw_cells, points=0,):
    
        self.id = player_id
        
        self.cells = pygame.sprite.Group()

        self.position_goal = spawn_position

        self.raw_cells = raw_cells

        self.spawn_cell()

    def spawn_cell(self):
        new_cell = Cell(player_id= self.id,
                        cell_id = len(self.cells),
                        position = self.position_goal.copy())
        self.cells.add(new_cell)
        self.raw_cells.add(new_cell)

    def update(self, commands):
        
        move_by = commands.get('move_by', np.array([0., 0.]))

        self.move_position_goal(move_by)

        if commands.get('split', False):
            print("splitting")
            self.split()
            print("Cell COunt ", len(self.cells))

        self.update_cells()
    
    def update_cells(self):
    
        # Move Towards Goal 
        self.move_cells()


    def move_cells(self):

        for cell in self.cells.sprites():
            
            # TODO: Make Collisions between group to group
            cell.move(self.position_goal, 
                      sprite_group = self.cells)
    
    def split(self):
        # TODO: Use self.spawn_cell
        # self.cells.add(Cell(self.position_goal - np.array([100., 100])))
        pass

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
    
    def get_score(self):
        return sum([cell.points for cell in self.cells.sprites()]) / 100



    #TODO: Implement these
    # def get_position(self): 


