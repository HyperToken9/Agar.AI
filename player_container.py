import pygame
import numpy as np

from player import Player

PLAYER_ID = 0

class PlayerContainer:

    def __init__(self):
        
        self.player_index = {}

        self.raw_cells = pygame.sprite.Group()

    def spawn_player(self, position=np.array([100., 100.])):
        
        global PLAYER_ID

        new_player = Player(player_id = PLAYER_ID, 
                            spawn_position = position,
                            raw_cells = self.raw_cells)

        self.player_index[PLAYER_ID] = new_player

        PLAYER_ID += 1

    def update(self, control_dictionary):

        self.process_cell_consumption()
        
        # print(control_dictionary)
        for player_id, commands in control_dictionary.items():
            # print("player_id", player_id, "commands", commands)
            self.player_index[player_id].update(commands)

    def draw(self, screen):

        for player in self.player_index.values():
            
            player.draw(screen)


    def process_cell_consumption(self):

        # Eating Players
        collision_dict = pygame.sprite.groupcollide(
            self.raw_cells,
            self.raw_cells,
            False, False)

        for player_cell, cells in collision_dict.items():

            player_cell.eat(cells)
