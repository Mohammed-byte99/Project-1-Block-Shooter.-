import pygame
import random
import library_block

# These are made as variables, so I can change the movement of my bad blocks to be faster and faster every level
num1 = -3
num2 = 3

# This Class sets the movement for my bad blocks (AKA: Red Blocks) and also bars the red blocks
# From going outside my screen

class Bad(library_block.Block):
    def update(self):
        
        # Setting the Erratic Movement
        self.rect.x += random.randint(num1, num2)
        self.rect.y += random.randint(num1, num2)

        # Barring the Blocks to Go Oustide my Screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 685:
            self.rect.x = 685
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 385:
            self.rect.y = 385


