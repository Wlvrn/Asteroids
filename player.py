import pygame # type: ignore
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # Initialise rotation
        self.shoot_timer = 0  # Initialize cooldown timer

    def rotate(self, dt):
        self.rotate += PLAYER_TURN_SPEED * dt # rotate player

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return  # Prevent shooting if still in cooldown

        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown timer


    # def shoot(self):
    #     shot = Shot(self.position.x, self.position.y)
    #     direction = pygame.Vector2(0, 1).rotate(self.rotation)
    #     shot.velocity = direction * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # Turn left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]: # Turn right
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]: # Move foward
            self.move(dt)
        if keys[pygame.K_s]: # Move backward
            self.move(-dt) # Move in the opposite direction
        if keys[pygame.K_SPACE]:  # Shoot when spacebar is pressed
            self.shoot()

        # Reduce shoot cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # Draw triangle shape
        
