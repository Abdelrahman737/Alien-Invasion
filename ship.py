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

        # Flags for moving right or left
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings

    def update(self):
        """Updates ship's position based on movment flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x += -self.settings.ship_speed

    def blit_me(self):
        self.screen.blit(self.image, self.rect)