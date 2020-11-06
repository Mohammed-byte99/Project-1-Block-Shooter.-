import pygame
import random

BLUE = (0, 0, 255)

# Creating My Player Block, Making it able to Move, Setting It's Speed and Making Boundaries for It

class Player(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self, x, y):
      
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
    
        self.change_x += x
        self.change_y += y
 
    def update(self):
        
        self.rect.y += self.change_y
        self.rect.x += self.change_x
        
        # Did this update cause us to hit a wall?
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 685:
            self.rect.x = 685
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 385:
            self.rect.y = 385
