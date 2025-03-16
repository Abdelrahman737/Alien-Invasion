import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.last_bullet_time = 0

        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.check_events()
            self.update_bullets()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)
    
    def check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
    
    def check_keydown_events(self, event):
        """Responds to key presses"""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
    
    def check_cooldown(self):
        """Checks the cooldown time of the bullet"""
        # Gets the current time from the beginning of the game in milleseconds
        current_time = pygame.time.get_ticks()

        # Check if the we can shoot a new bullet or wait untill the cooldown time being reached
        if current_time - self.last_bullet_time > self.settings.bullet_cooldown:
            self.last_bullet_time = current_time
            return True
        return False

    def fire_bullet(self):
        """Creat a new bullet object"""
        if self.check_cooldown():
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.bullet_sound.play()

    def clear_old_bullets(self):
        """Clear the old bullets after disappearing from the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update_bullets(self):
        """Update the possition of bullets and clears old ones"""
        self.bullets.update()
        self.clear_old_bullets()

    def create_fleet(self):
        """Creates a fleet of aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        spacing = alien.spacing
        current_x = spacing

        while current_x < (self.settings.width - (spacing + alien_width)):
            new_alien = Alien(self)
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 30 + alien_width

    def update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.blit(self.bg_image, self.bg_rect)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blit_me()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()