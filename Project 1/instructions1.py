import pygame
import random

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)

# This is my Instructions Page Number 1
# Pretty Much where I Create my First Instruction Page

def number_1(screen):
    
    # Setting My Font Size
    font = pygame.font.Font(None, 36)

    # Filling my Screen Black Before I Display my Text
    screen.fill(BLACK)

    # What Text I Want, What color I want and Where I want it 
    text = font.render("Welcome to Block Shooter!", True, GREEN)
    screen.blit(text, [175, 150])
 
    text = font.render("Click Spacebar to Continue Past Instruction Screens!", True, RED)
    screen.blit(text, [40, 200])

