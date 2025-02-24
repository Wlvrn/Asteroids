# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # Initialise pygame
    pygame.init()
    print("Starting Asteroids!")
    
    # Create a game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock to limit FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allow user to close the window
                return
            
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000 # Convert ms to seconds

if __name__ == "__main__":
    main()