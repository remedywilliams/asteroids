import sys
import pygame
from shot import Shot
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    dt = 0
    afield = AsteroidField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.player_collide(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.bullet_collide(asteroid):
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)


        pygame.Surface.fill(screen, color="black")
        # player.update(dt)     // before groups were introduced 

        for sprite in drawable:
            # print(f"Player Position: {player.position}")
            sprite.draw(screen) # previously paired to comment above

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()