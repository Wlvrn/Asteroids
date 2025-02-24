# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
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

    updatable = []
    drawable = []

    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable.append(player)
    drawable.append(player)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Allow user to close the window
                return
            
        dt = clock.tick(60) / 1000 # Maintain 60 FPS

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)            
        
        screen.fill("black") # Clear screen

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # player.update(dt) # Update player rotation
        # player.draw(screen) # Draw player

        pygame.display.flip() # Refresh the display

if __name__ == "__main__":
    main()