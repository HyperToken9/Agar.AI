import numpy as np
import matplotlib.pyplot as plt

class Stats:

    # def __init__(self):

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
