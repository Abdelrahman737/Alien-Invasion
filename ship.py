import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialized a ship and sets its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Set the position of the ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        self.screen.blit(self.image, self.rect)