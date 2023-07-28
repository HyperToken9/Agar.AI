
import pygame
import numpy as np

from game import Game
from toolkit import ToolKit
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#TODO: There needs to be a centralized way to deal with focused player

class Renderer:
    
    def __init__(self):
        
        pygame.init()
        
        self.running = True
        
        self.game = Game()
                
        # Pygame Surface
        self.background = pygame.image.load("sprites/background_tile.png")        
        
        self.background_size = self.background.get_size()
        
        # Set the width and height of the screen [width, height]
        self.screen_size = np.array((700, 500))
        
        self.screen = pygame.display.set_mode(self.screen_size)
        
        pygame.display.set_caption("Agar.AI")

        self.font = pygame.font.SysFont("hack", size = 36)

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
        
        # -------- Main Program Loop -----------
        while self.running:
            
            control_dictionary = {}

            primary_player = {'move_by': self.cursor_relative_position() / 50}

            # --- Main event loop
            for event in pygame.event.get():
                  
                if event.type == pygame.QUIT:
                    self.running = False            

                # checking if keydown event happened or not
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        primary_player['split'] = True
            

            # TODO: Calculate Positional Updates

            control_dictionary[0] = primary_player

            game_arguments = {'control': control_dictionary, }

            self.game.update(game_arguments)

            # --- Drawing code should go here
            self.render_background()

            self.render_game_entities()

            self.render_score_board()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Stats.plot_heat_map(self.game.agar)

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
        focused_entity = self.game.players.player_index[0]
        

        for player in self.game.get_players():
        
            for sprite in player.get_cells():

                location = sprite.position - focused_entity.position_goal + self.screen_size / 2
                sprite.rect.center = location
                
        # Agar 
        for sprite in self.game.agar.sprites():
            
            location = sprite.position - focused_entity.position_goal + self.screen_size / 2
            
            sprite.rect.center = location
        
        self.game.agar.draw(self.screen)
        self.game.players.draw(self.screen)
    
    def render_background(self):
        """
            Tiles the screen with the background image
        """

        focused_entity = self.game.players.player_index[0]
        
        offset = focused_entity.position_goal * -1
        
        offset %= self.background_size
        
        offset -= self.background_size
        
        # print(f"{offset = }")
        
        for i in range(int(offset[0]), self.screen_size[0], self.background_size[0]):
        
            for j in range(int(offset[1]), self.screen_size[1], self.background_size[1]):
                
                self.screen.blit(self.background, (i, j))
        
    def render_score_board(self):
        
        y_offset = 10
        y_spacing = 30

        x_offset = 125

        score_board = ["Score"] 

        for player,score in self.game.scores():

            score_board.append(f"{player.id} {score:.0f}")

        for line in score_board:

            text_render = self.font.render(line, True, (0, 0, 0)) 

            text_rect = text_render.get_rect(topleft = (self.screen_size[0] - x_offset, 
                                                        y_offset))

            y_offset += y_spacing

            self.screen.blit(text_render, text_rect)

    
if __name__ == "__main__":
    
    game_gui = Renderer()
    
    game_gui.start()
    
    
    