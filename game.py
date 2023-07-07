import numpy as np
import pygame

from agar import Agar
from colony import Colony
from spawner import Spawner

class Game:

    def __init__(self):

        self.arena_size = np.array([1000, 1000]) # Height, Width
        
        self.agar = pygame.sprite.Group()
                
        self.colonies = pygame.sprite.Group()

        self.spawner = Spawner(self)

    def start(self):
 
        self.spawn_colony()

        self.spawn_colony(position = np.array([100, 100]))

    def update(self, game_arguments):
        """
            The control dictionary assigns each colony with their updated speed.
        """
        control_dicitonary = game_arguments.get('control', {})
        
        self.colonies.update(control_dicitonary)
        
        # Eating Agar
        eat_dict = pygame.sprite.groupcollide(self.colonies, self.agar, False, False)
        
        for colony, agars in eat_dict.items():
            
            colony.eat(agars)

        # Eating Colony
        eat_dict = pygame.sprite.groupcollide(self.colonies, self.colonies, False, False)

        for colony, colonies in eat_dict.items():

            # print(colonies)
            colony.eat(colonies)
            # a = 1
        

        self.spawner.spawn_agar()

    def spawn_colony(self, position = np.array([500, 500.])):
        
        if len(self.colonies.sprites()) == 0:
            self.colonies.add(Colony(position= position, focus=True))
        else:
            self.colonies.add(Colony(position= position, points= 900))
     

                    
if __name__ == "__main__":

    print("This is the game.py file.")