import pygame
import random

BLACK = (  0,   0,   0)
BLUE = (0, 0, 255)
SKY = (142, 208, 248)


# This is my Instructions Page Number 1
# Pretty Much where I Create my First Instruction Page

def number_2(screen):
    
    # Setting My Font Size
    font = pygame.font.Font(None, 24)

    # Filling my Screen Black Before I Display my Text
    screen.fill(BLACK)

    # What Text I Want, What color I want and Where I want it 
    text = font.render("Instructions:", True, BLUE)
    screen.blit(text, [10, 20])
 
    text = font.render("LEVELS: 3", True, SKY)
    screen.blit(text, [10, 50])

    text = font.render("OBJECTIVE: GRAB ALL GREEN BLOCKS AND DESTORY RED BLOCKS", True, SKY)
    screen.blit(text, [10, 80])       

    text = font.render("MOVEMENT: UTILIZE ARROW KEYS", True, SKY)
    screen.blit(text, [10, 110])   

    text = font.render("DESTRUCTION: AIM AND CLICK MOUSE TO DESTORY RED BLOCKS", True, SKY)
    screen.blit(text, [10, 140]) 

    text = font.render("POWERUP: COLLECT THE BAD BLOCK TO GET RID OF HALF OF THE RED BLOCKS", True, SKY)
    screen.blit(text, [10, 170]) 

    text = font.render("HAVE FUN AND GOOD LUCK!", True, SKY)
    screen.blit(text, [10, 200]) 
    
     
    
    
