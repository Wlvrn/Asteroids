import pygame # type: ignore

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        """Check if this CircleShape collides with another CircleShape."""
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
    
    def check_collision(self, other):
        """Returns True if this object collides with another CircleShape."""
        return self.position.distance_to(other.position) < (self.radius + other.radius)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass