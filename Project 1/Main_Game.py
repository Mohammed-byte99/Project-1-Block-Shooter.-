import pygame
import random
import library_block
import library_player
import bad_block
import good_block
import bul
import instructions1
import instructions2
import powerup_cleaner

# --- Global Constants ---

# Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PEACH = (248, 182, 142)
SKY = (142, 208, 248)

# Screen Stuff (Width and Height)
Screen_width = 700
Screen_height = 400

# --- Global Constants ---

class Game(object):

    def __init__(self):
    
        # Attributes/Variables
        self.lives = 5
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.level = -1
   
        # Sound Stuff
        self.click_sound = pygame.mixer.Sound('good.wav')
        self.click_sound2 = pygame.mixer.Sound('bad.wav')

        # Create sprite lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.powerup_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
 
        for i in range(8):
            # This represents a GOOD block (Calls My Good Block Class for its Movement)
            block = good_block.Good(GREEN, 20, 15)
 
            # Set a random location for the block
            block.rect.x = random.randrange(Screen_width)
            block.rect.y = random.randrange(Screen_height)
 
            # Add the block to the list of objects
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        for i in range(15):
            # This represents a BAD block (Calls My Bad Block Class for its Movement)
            block = bad_block.Bad(RED, 20, 15)
 
            # Set a random location for the block
            block.rect.x = random.randrange(Screen_width)
            block.rect.y = random.randrange(Screen_height)
 
            # Add the block to the list of objects
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        # Create a Player block (Calls My Player Block Class for its Values)
        self.player = library_player.Player(60, 45)
        self.all_sprites_list.add(self.player)
 
    def checkEvent(self):
        # --- Process all of the events. Return a "True" if we need to close the window.---
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                return True
            
            # Processes How to Move Player
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 3)
            # How to Move Through Instruction Screens
                elif event.key == pygame.K_SPACE and self.level < 1:
                    self.level += 1
            # How To Restart My Game
                elif event.key == pygame.K_r:
                    if self.game_over or self.game_won:
                        self.__init__()

            # Processes How to Move Player 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -3) 
            
            # How to Shoot and Aim my Bullets
            elif event.type == pygame.MOUSEBUTTONDOWN and self.level > 0:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                bullet = bul.Bullet(self.player.rect.x, self.player.rect.y, mouse_x, mouse_y)
                self.all_sprites_list.add(bullet)
                self.bullet_list.add(bullet)

        return False  
    
    def run_logic(self):
        # --- This method is run each time through the frame. It updates positions and checks for collisions. ---
        if (not self.game_over) or (not self.game_won):
       
            # Move all the sprites
            self.all_sprites_list.update()

            # See if the player or bullet has collided with anything.
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            blocks_hit_list2 = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)
            blocks_hit_list4 = pygame.sprite.spritecollide(self.player, self.powerup_list, True)
        
            # Check the list of collisions. This Means Every time this Block Collides with
            # My Player Block, something will happen. 
            for block in blocks_hit_list:
                self.click_sound.play()
                self.score += 1
            for block in blocks_hit_list2:
                self.click_sound2.play() 
                self.lives -= 1
            ## -- Example Block Collision Explanation -- ##
            # So When My PowerUp Block Collides With My Player...
            for block in blocks_hit_list4:
                # ...Store my the number of bad block elements in my bad block list in a variable
                num_blocks = len(self.bad_block_list)
                # Then, Get Rid of ALL my Bad Blocks in all my lists
                for block in self.bad_block_list:
                    block.kill()
                # Then, Use The Variable I stored my bad block elements in, and make it draw half of 
                # Bad Blocks I had in my Bad block list, before it got deleted.
                # Then Add My Bad Blocks To both my all sprites and bad block list.
                for i in range(num_blocks // 2):
                    temp_block = bad_block.Bad(RED, 20, 15)
                    temp_block.rect.x = random.randrange(Screen_width)
                    temp_block.rect.y = random.randrange(Screen_height)
                    self.bad_block_list.add(temp_block)
                    self.all_sprites_list.add(temp_block)

            # Bullet Collision
            for bullet in self.bullet_list: 
                # See if it hits a block
                block_hit_list3 = pygame.sprite.spritecollide(bullet, self.bad_block_list, True)
                # For each block hit, remove the bullet and add to the score
                for block in block_hit_list3:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.score += 1
                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)

            # Sees if Lives are Zero and If they are it makes game_over variable True
            if self.lives <= 0:
                self.game_over = True
            
    ## -- RUNS MY FIRST LEVEL YAYAYAAYAY -- ##        
    def game_level1(self):

        self.run_logic()

    ## --- Changes I am Making for my Second Level --- ##
        if len(self.good_block_list) == 0 and len(self.bad_block_list) == 0:
                self.level += 1
                
                for i in range(24):
                    
                    # Changing My Speed Vectors
                    bad_block.num1 = -5
                    bad_block.num2 = 5

                    # This represents a BAD block
                    block = bad_block.Bad(RED, 20, 15)

                    # Set a random location for the block
                    block.rect.x = random.randrange(Screen_width)
                    block.rect.y = random.randrange(Screen_height)
        
                    # Add the block to the list of objects
                    self.bad_block_list.add(block)
                    self.all_sprites_list.add(block)

   
                for i in range(10):
                    # This represents a  GOOD block
                    block = good_block.Good(GREEN, 20, 15)
        
                    # Set a random location for the block
                    block.rect.x = random.randrange(Screen_width)
                    block.rect.y = random.randrange(Screen_height)
        
                    # Add the block to the list of objects
                    self.good_block_list.add(block)
                    self.all_sprites_list.add(block)
                
                
                for i in range(1):
                    # This represents a POWERUP block
                    block = powerup_cleaner.Cleaner(BLACK, 20, 15)
                    
                    # Set a random location for the block
                    block.rect.x = random.randrange(Screen_width)
                    block.rect.y = random.randrange(Screen_height)
                    
                    # Add the block to the list of objects
                    self.powerup_list.add(block)
                    self.all_sprites_list.add(block)

    ## -- RUNS MY SECOND LEVEL YAYAYAY -- ##  
    def game_level2(self):
        
        self.run_logic()

    ## --- Changes I am Making for my Third Level --- ##
        if len(self.good_block_list) == 0 and len(self.bad_block_list) == 0:
                self.level += 1
                
                for i in range(35):
                    # Changing My Speed Vectors
                    bad_block.num1 = -9
                    bad_block.num2 = 9

                    # This represents a BAD block
                    block = bad_block.Bad(RED, 20, 15)

                    # Set a random location for the block
                    block.rect.x = random.randrange(Screen_width)
                    block.rect.y = random.randrange(Screen_height)
        
                    # Add the block to the list of objects
                    self.bad_block_list.add(block)
                    self.all_sprites_list.add(block)
                
                for i in range(15):
                    # This represents a  GOOD block
                    block = good_block.Good(GREEN, 20, 15)
        
                    # Set a random location for the block
                    block.rect.x = random.randrange(Screen_width)
                    block.rect.y = random.randrange(Screen_height)
        
                    # Add the block to the list of objects
                    self.good_block_list.add(block)
                    self.all_sprites_list.add(block)

            
    ## -- RUNS MY THIRD LEVEL YAYAYA -- ##
    def game_level3(self):
        
        self.game_level2()


    def display_frame(self, screen):
        # --- Display everything to the screen for the game.---
        screen.fill(PEACH)
  
        # If My Game is Lost, Print this on my Screen
        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, Press R to Restart", True, BLACK)
            center_x = (Screen_width // 2) - (text.get_width() // 2)
            center_y = (Screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        
        # If My Game is Won, Print this on my Screen
        elif self.game_won:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("WINNER, Press R to Restart", True, BLACK)
            center_x = (Screen_width // 2) - (text.get_width() // 2)
            center_y = (Screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
      
        # If Neither of that happens, draw my sprites for my levels and any text I need for my Levels
        else:
            self.all_sprites_list.draw(screen)
            
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Score: " + str(self.score), True, BLACK)
            screen.blit(text, [0, 370])

            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Lives: " + str(self.lives), True, BLACK)
            screen.blit(text, [0, 350])

            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Level: " + str(self.level), True, BLACK)
            screen.blit(text, [0, 330])

    # Level Organization, Tells the program what to do at each level
    def game_logic(self, screen):
        if (self.level == -1):
            instructions1.number_1(screen)
        elif (self.level == 0):
            instructions2.number_2(screen)
        elif (self.level == 1):
            self.game_level1()
            self.display_frame(screen)
        elif (self.level == 2):
            self.game_level2()
            self.display_frame(screen)
        elif (self.level == 3):
            self.game_level3()
            self.display_frame(screen)
        elif (self.level == 4):
            self.game_won = True
            self.display_frame(screen)
           
            
def main():
    # -------- Main Program Function -----------
    # Initialize Pygame and set up the window
    pygame.init()
    screen = pygame.display.set_mode([Screen_width, Screen_height])
    pygame.display.set_caption("Block Shooter Game")

    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()

    # Create an instance of the Game class
    game = Game()

    # Main Game Loop
    while not done:
        # Process events (keystrokes, mouse clicks, etc)
        done = game.checkEvent()
            
        game.game_logic(screen)
        
        # Pause for the next frame
        clock.tick(100)

        #Update ALL Screens
        pygame.display.flip()
        
    # Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()


    