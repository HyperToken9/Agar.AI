
import pygame
import numpy as np

from game import Game

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Renderer:
    
    def __init__(self):
        
        pygame.init()
        
        self.running = True
        
        self.game = Game()
                
        # Pygame Surface
        self.background = pygame.image.load("sprites/background_tile.png")        
        
        self.background_size = self.background.get_size()
        
        print(f"{self.background_size = }")
        
        # Set the width and height of the screen [width, height]
        self.screen_size = np.array((700, 500))
        
        self.screen = pygame.display.set_mode(self.screen_size)
        
        pygame.display.set_caption("Agar.AI")
                
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def cursor_relative_position(self):
        
        if not pygame.mouse.get_focused():
            return np.array([0, 0])
        
        global_position = np.array(pygame.mouse.get_pos())
        # print(f"Global position: {global_position}")
        return global_position - self.screen_size / 2
    
    def start(self):
        """
            Initializes Game With GUI
        """
        self.game.start()
        
        # self.game.spawn_colony()
        
        self.game.spawn_colony()
        
        # -------- Main Program Loop -----------
        while self.running:
            
            # --- Main event loop
            for event in pygame.event.get():
                  
                
                if event.type == pygame.QUIT:
                    self.running = False            
            
            # --- Drawing code should go here
            self.render_background()
        
            self.render_game_entities()

            # self.players.update(move_by = )

           
            # TODO: Calculate Positional Updates

            control_dictionary = {}

            control_dictionary[0] = self.cursor_relative_position() / 500

            game_arguments = {'control': control_dictionary, }

            self.game.update(game_arguments)


            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
    
    def render_game_entities(self):
        """
            Renders All Game Entities
                - Colonies
                - Agar
                - Spikes
        """
        # Colonies
        focused_entity = self.game.colonies.sprites()[0]
        
        for sprite in self.game.colonies.sprites():
        
            location = sprite.position - focused_entity.position + self.screen_size / 2
            sprite.rect.center = location
                
        # Agar 
        # self.game.petri_dish.
        for sprite in self.game.agar.sprites():
            
            location = sprite.position - focused_entity.position + self.screen_size / 2
            
            sprite.rect.center = location
        
        self.game.agar.draw(self.screen)
        self.game.colonies.draw(self.screen)
    
    def render_background(self):
        """
            Tiles the screen with the background image
        """

        focused_entity = self.game.colonies.sprites()[0]
        
        offset = focused_entity.position * -1
        
        offset %= self.background_size
        
        offset -= self.background_size
        
        # print(f"{offset = }")
        
        for i in range(int(offset[0]), self.screen_size[0], self.background_size[0]):
        
            for j in range(int(offset[1]), self.screen_size[1], self.background_size[1]):
                
                self.screen.blit(self.background, (i, j))
        
        
    
if __name__ == "__main__":
    
    game_gui = Renderer()
    
    game_gui.start()
    
    
    