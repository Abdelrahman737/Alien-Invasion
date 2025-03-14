import pygame

class Settings:
    """A class to store all settings of the game"""

    def __init__(self):
        """Initializes game settings"""
        # Screen settigns
        self.width = 1200
        self.height = 800
        self.bg_image = pygame.image.load('images/space.bmp')