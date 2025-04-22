import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)
        # similar to draw.polygon, either specify each KEY= or none, or it'll complain.

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        randangle = random.uniform(20, 50)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        veca = self.velocity.rotate(randangle)
        vecb = self.velocity.rotate(-randangle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = veca * 1.2
        asteroid2.velocity = vecb
