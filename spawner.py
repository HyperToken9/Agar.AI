import cv2 as cv
import numpy as np
from random import choices

from agar import Agar

class Spawner:

    def __init__(self, game):

        self.game = game

        self.spawn_map = None

        self.CELL_BUFFER = 1.3
        self.AGAR_BUFFER = 4.0

    def spawn_agar(self):

        SPAWN_COUNT = 3
        arean_width = self.game.arena_size[1]

        self.update_spawn_map()

        if self.limit_spawn_rate():
            return

        weights = self.spawn_map.flatten()

        indices = range(len(weights))
        
        spawn_indices = choices(indices, weights, k=SPAWN_COUNT)

        print(f"{spawn_indices = }")

        for index in spawn_indices:
            
            # print(f"{index, index}")
            position =  (index % arean_width, index // arean_width)

            # Spwan Rate seems to sky rocket at the edge of the map.

            self.game.agar.add(Agar(position = np.array(position)))

    def limit_spawn_rate(self):
        
        THRESHOLD = 0.50 # of the MAXIMUM SPAWN

        max_permissiblity = self.game.arena_size[0] * self.game.arena_size[1]
        
        current_spawn = max_permissiblity - np.sum(self.spawn_map)

        if current_spawn > max_permissiblity * THRESHOLD:
            return True
        
        return False

    def update_spawn_map(self):
        
        #TODO: Let this method taken in a list of groups, based on which the spawn map is updated.

        self.spawn_map = np.ones(self.game.arena_size)
        
        for colony in self.game.colonies.sprites():
            
            # print(f"{colony.get_size() = }")

            cv.circle(img = self.spawn_map, 
                      center = tuple(colony.position.astype(int)), 
                      radius = int(colony.get_size() * self.CELL_BUFFER), 
                      color = 0, thickness = -1)
            
        for agar in self.game.agar.sprites():
            
            cv.circle(img = self.spawn_map,
                      center = tuple(agar.position.astype(int)),
                      radius = int(agar.get_size() * self.AGAR_BUFFER   ),
                      color = 0, thickness = -1)

        # cv.imshow("Spawn Map", self.spawn_map)
        # cv.waitKey(1)