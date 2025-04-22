import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)
        # similar to draw.polygon, either specify each KEY= or none, or it'll complain.

    def update(self, dt):
        self.position += (self.velocity * dt)