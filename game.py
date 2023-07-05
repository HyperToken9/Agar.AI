import numpy as np
import pygame

from agar import Agar
from colony import Colony

class Game:

    def __init__(self):

        self.arena_size = np.array([1000, 1000])
        
        self.agar = pygame.sprite.Group()
        
        self.agar.add(Agar())
        
        self.colonies = pygame.sprite.Group()

    def start(self):
        pass

    def update(self, game_arguments):
        """
            The control dictionary assigns each colony with their updated speed.
        """
        control_dicitonary = game_arguments.get('control', {})
        
        self.colonies.update(control_dicitonary)
        
        # self.petri_dish.update()
        # self.colonies.update()
        # self.spawn_colony()

        # Check for collisions
        eat_dict = pygame.sprite.groupcollide(self.colonies, self.agar, False, False)
        
        self.check_eaten(eat_dict)
        
        # print(f"{eat_dict = }")
        
        

    def spawn_colony(self):
        
        if len(self.colonies.sprites()) == 0:
            self.colonies.add(Colony(focus=True))
        else:
            self.colonies.add(Colony())
    
    
    def check_eaten(self, eat_dict):
        """
            Checks if entity had been completely consumed.
        """
        
        for predator, prey_list in eat_dict.items():
            
            for prey in prey_list:
                
                if not predator.rect.contains(prey.rect):
                    
                    eat_dict[predator].remove(prey)
                    
if __name__ == "__main__":

    print("This is the game.py file.")