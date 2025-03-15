import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class that manages bullets fired from the ship"""
    def __init__(self, ai_game):
        """Intializes bullet object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color

        # Create bullet rect at position 0,0 and then modifying it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midtop = ai_game.ship.rect.midtop
        

    def update(self):
        """Moves the bullet up the screen"""
        self.rect.y -= self.settings.bullet_speed
    
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)