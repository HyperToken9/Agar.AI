import numpy as np


class Spawner:

    def __init__(self, game):

        self.game = game

    def spawn_agar(self):
        pass


    def create_spawn_map(self):

        spawn_weight = np.ones(self.game.arena_size)
        print(spawn_weight.shape)