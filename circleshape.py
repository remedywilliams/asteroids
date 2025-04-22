import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must foverride
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def player_collide(self, shape):
        # distance = self.position.distance_to(shape.position)
        # print(f"Self Position: {self.position}, Other: {shape.position}, Distance: {distance}")
        return self.position.distance_to(shape.position) <= (self.radius + shape.radius)
    
    def bullet_collide(self, object):
        return self.position.distance_to(object.position) <= (self.radius + object.radius)
