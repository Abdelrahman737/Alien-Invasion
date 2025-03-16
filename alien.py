import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that manages alien objects"""
    def __init__(self, ai_game):
        """Initializes alien objects"""
        super().__init__()
        self.screen = ai_game.screen

        # Loading alien image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Set the position of the alien near from the top left of the screen
        self.spacing = 30