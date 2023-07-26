import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class ToolKit:

    def __init__(self):
        pass

    @staticmethod
    def plot_heat_map(sprite_group):
        
        # Extract x and y coordinates from the sprite group
        x = [sprite.position[0] for sprite in sprite_group]
        y = [sprite.position[1] for sprite in sprite_group]

        print(f"{x = }")
        print(f"{y = }")
        # Create a 2D histogram using the extracted coordinates
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)

        # Set up the figure and axes
        fig, ax = plt.subplots()

        # Create the heatmap using imshow
        im = ax.imshow(heatmap, cmap='hot', origin='lower')

        # Add a colorbar to show the intensity scale
        cbar = plt.colorbar(im)

        # Set the labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Heat Map')

        # Show the plot
        plt.show()

    @staticmethod
    def create_obstacle_map(arena_size = [1000, 1000], **kwargs):

        # TODO: Let this method taken in a list of groups, based on which the spawn map is updated.

        spawn_map = np.ones(arena_size)

        sprite_groups = np.array(kwargs.get('sprite_groups'))

        # print(sprite_groups, "wow")

        exclude = kwargs.get('exclude', [])

        for group in sprite_groups:
            
            # print(type(group))
            for sprite in group.sprites():
                
                if sprite in exclude:
                    continue
                
                cv.circle(img=spawn_map,
                          center=tuple(sprite.position.astype(int)),
                          radius=int(sprite.get_size()),
                          color=0, thickness=-1)

        return spawn_map
    
    @staticmethod
    def calculate_goal(sprite, map, destination):
        
        k_size = int(sprite.get_size()) # Kernel Size

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, 
                                          (k_size, k_size))
        # map = cv.dilate(map, kernel, iterations=1)

        move_by = destination - sprite.position

        factor = 1

        while factor > 0.25:

            move_to  = sprite.position + move_by * factor 

            if map[int(move_to[1]), int(move_to[0])] == 1:
                return sprite.position + move_by * factor
            
            factor /= 2

        return sprite.position


    @staticmethod
    def vector_projection(vector, onto):
        """
            Returns the projection of vector onto onto
        """
        return np.dot(vector, onto) / np.linalg.norm(onto)


