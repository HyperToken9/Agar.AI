import pygame


class Colony(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
    
        self.cells = pygame.sprite.Group()