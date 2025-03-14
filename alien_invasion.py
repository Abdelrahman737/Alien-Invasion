import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bg_image = self.settings.bg_image
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.center = self.screen_rect.center
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)
    
    def check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
    
    def update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.blit(self.bg_image, self.bg_rect)
        self.ship.update()
        self.ship.blit_me()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()