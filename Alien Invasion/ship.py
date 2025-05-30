import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    
    def __init__(self, ai_game):
        """Initialise the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)
        
        # MOVEMENT FLAG; START WITH A SHIP THAT IS NOT MOVING
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's x value, not the rect
        # the below ensures the ship does not go out of bounds         
        if self.moving_right and self.moving_left < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # update rect object from self.x
        self.rect.x = self.x
               
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        