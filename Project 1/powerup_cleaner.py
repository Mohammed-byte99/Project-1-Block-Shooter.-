import pygame
import random
import library_block

# Power Up Block Movement, and makes sure it Does not move off the Screen

class Cleaner(library_block.Block):
    def update(self):
        self.rect.x += random.randint(-2, 2)
        self.rect.y += random.randint(-2, 2)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 685:
            self.rect.x = 685
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 385:
            self.rect.y = 385