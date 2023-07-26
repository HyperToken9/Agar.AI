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
        control_dicitonary = game_arguments.get('control', {})
        
        self.players.update(control_dicitonary)
        
        # # Eating Agar
        # eat_dict = pygame.sprite.groupcollide(self.colonies, self.agar, False, False)
        
        # for colony, agars in eat_dict.items():
            
        #     colony.eat(agars)

        # Eating Colony
        # eat_dict = pygame.sprite.groupcollide(self.colonies, self.colonies, False, False)

        # for colony, colonies in eat_dict.items():
        #     # print(colonies)
        #     colony.eat(colonies)
        
        # Spawing Agar
        # self.spawner.spawn_agar()

    def get_players(self):

        return self.players.player_index.values()

    # def add_player(self, position = np.array([500, 500.])): 
    #     self.players.spawn_player(position)
        # global COLONY_ID
        # if COLONY_ID == 0:
        #     self.colonies[COLONY_ID] = Colony(id = COLONY_ID,
        #                                       spawn_position = position,
        #                                       focus=True)
        # else:
        #     self.colonies[COLONY_ID] = Colony(id = COLONY_ID, 
        #                                       spawn_position = position, 
        #                                       points = 900)
        # COLONY_ID += 1
                    
if __name__ == "__main__":

    print("This is the game.py file.")