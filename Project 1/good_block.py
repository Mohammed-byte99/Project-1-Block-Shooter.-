import pygame
import random
import library_block

# This Class sets the movement for my good blocks (AKA: Good Blocks) 
# Sets The Movement to Go From the Top of the Screen to the Bottom
# Everytime it hits the Bottom, The Good Block is then Randomly
# Moved to Fall Down the Screen from a Different Starting Point

class Good(library_block.Block):
    def update(self):
        self.rect.y += 5
        if self.rect.y > 400:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, 700)