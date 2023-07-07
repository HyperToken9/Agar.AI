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

        self.spawn_colony()

    def update(self, game_arguments):
        """
            The control dictionary assigns each colony with their updated speed.
        """
        control_dicitonary = game_arguments.get('control', {})
        
        self.colonies.update(control_dicitonary)
        
        # Check for collisions
        eat_dict = pygame.sprite.groupcollide(self.colonies, self.agar, False, False)
        
        for colony, agars in eat_dict.items():
            
            colony.eat(agars)

        self.spawner.spawn_agar()

    def spawn_colony(self):
        
        if len(self.colonies.sprites()) == 0:
            self.colonies.add(Colony(focus=True))
        else:
            self.colonies.add(Colony())
     

                    
if __name__ == "__main__":

    print("This is the game.py file.")