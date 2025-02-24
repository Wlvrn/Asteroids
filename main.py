import pygame # type: ignore
from player import Player
from asteroid_fields import AsteroidField
from asteroid import Asteroid
from constants import *
from shot import Shot

def main():
    pygame.init()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    # Set static containers for asteroid and asteroid field
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    # Create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Create asteroid field
    asteroid_field = AsteroidField()

    # Game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all sprites
        updatable.update(dt)
        
        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                exit()  # Immediately exit the game on collision

        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    # asteroid.kill()  # Remove asteroid
                    shot.kill()  # Remove bullet
                    asteroid.split()  # Split the asteroid instead of killing it

        for shot in shots:
            shot.update(dt)

        # drawable.draw(screen)

        # Render all drawable sprites
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)  # Manually call the draw method instead of Group.draw()

        pygame.display.flip()

        # Maintain 60 FPS
        dt = clock.tick(60) / 1000  # Convert ms to seconds

if __name__ == "__main__":
    main()
