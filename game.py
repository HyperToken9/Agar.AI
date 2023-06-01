
import pygame

from .player import Player

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    
    def __init__(self):
        
        self.players = []
        
        self.running = True
        
        pygame.init()
        
        # Set the width and height of the screen [width, height]
        size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        
        pygame.display.set_caption("Agar.AI")
                
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def add_player(self, player):
        
        self.players.append(player)
    
    
    def start(self):
        
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
        

            # background image -> blit the background image.
            self.screen.fill(WHITE)
        
            # --- Drawing code should go here
        
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
        
            # --- Limit to 60 frames per second
            self.clock.tick(60)
        
        # Close the window and quit.
        pygame.quit()
        
    
if __name__ == "__main__":
    
    game = Game()
    
    game.add_player(Player())
    
    game.start()
    
    
    