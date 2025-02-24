import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = () # Will be set dynamically in main.py

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # Call parent constructor

    def split(self):
        """Splits the asteroid into two smaller ones if it's large enough."""
        self.kill()  # Remove the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Smallest asteroids do not split

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle for the split
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Spawn two smaller asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2    

    def update(self, dt):
        self.position += self.velocity * dt # Move asteroid

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # Draw asteroid