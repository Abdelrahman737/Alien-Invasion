import pygame

class Settings:
    """A class to store all settings of the game"""

    def __init__(self):
        """Initializes game settings"""
        # Screen settigns
        self.width = 1200
        self.height = 800
        self.bg_image = pygame.image.load('images/space.bmp')
        
        # Ship settings
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 14
        self.bullet_color = (255, 100, 100)
        self.bullet_cooldown = 500