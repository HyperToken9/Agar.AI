import numpy as np
import pygame

from agar import Agar
from player_container import PlayerContainer
from spawner import Spawner

class Game:

    def __init__(self):

        self.arena_size = np.array([1000, 1000]) # Height, Width
        
        self.agar = pygame.sprite.Group()
        
        self.players = PlayerContainer()

        self.spawner = Spawner(self)

    def start(self):
        
        self.players.spawn_player(position=np.array([155., 100]))
        # self.add_player()

        self.players.spawn_player(position=np.array([100., 100]))
        # self.add_player(position = np.array([100, 100]))


    def update(self, game_arguments):
        """
            The control dictionary assigns each colony with their updated speed.
        """
        
        self.process_agar_consumption()

        control_dicitonary = game_arguments.get('control', {})
        
        self.players.update(control_dicitonary)

 
        # Spawing Agar
        self.spawner.spawn_agar()

    def get_players(self):

        return self.players.player_index.values()

    def process_agar_consumption(self):

        # Eating Agar
        collision_dict = pygame.sprite.groupcollide(
                                self.players.raw_cells, self.agar, 
                                False, False)

        for player_cell, agars in collision_dict.items():
            
            player_cell.eat(agars)

    def scores(self):
        
        score_list = [[player, player.get_score()] for player in self.get_players()]

        return sorted(score_list, key=lambda x: x[1], reverse=True)
    
if __name__ == "__main__":

    print("This is the game.py file.")