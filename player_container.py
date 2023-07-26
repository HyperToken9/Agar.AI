import pygame
import numpy as np

from player import Player

PLAYER_ID = 0

class PlayerContainer:

    def __init__(self):
        
        self.player_index = {}

    def spawn_player(self, position=np.array([100., 100.])):
        
        global PLAYER_ID

        new_player = Player(PLAYER_ID, position)

        self.player_index[PLAYER_ID] = new_player

        PLAYER_ID += 1

    def update(self, control_dictionary):
        
        # print(control_dictionary)
        for player_id, commands in control_dictionary.items():
            # print("player_id", player_id, "commands", commands)
            self.player_index[player_id].update(commands)

    def draw(self, screen):

        for player in self.player_index.values():
            
            player.draw(screen)


