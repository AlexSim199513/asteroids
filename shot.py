from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)