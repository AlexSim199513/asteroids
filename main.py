import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.collision(player):
                print("Game over!")
                exit()
            for shot in shots:
                if sprite.collision(shot):
                    sprite.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()