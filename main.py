import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=5)
    AsteroidField()
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updt in updatable:
            updt.update(dt)
        for astr in asteroids:
            if astr.collision_check(player):
                sys.exit("Game over!")
        screen.fill("black")
        for drwb in drawable:
            drwb.draw(screen)
        pygame.display.flip()
        dt = timer.tick(144) / 1000
    
if __name__ == "__main__":
    main()