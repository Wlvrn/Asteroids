# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialise pygame
    pygame.init()
    print("Starting Asteroids!")
    
    # Create a game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allow user to close the window
                return
            
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()