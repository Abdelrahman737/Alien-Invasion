import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that manages alien objects"""
    def __init__(self, ai_game):
        """Initializes alien objects"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        # Loading alien image and set its rect attribute
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Set the position of the alien near from the top left of the screen
        self.x_spacing = 30
        self.y_spacing = 10

    def check_edges(self):
        """Checks if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to right"""
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction