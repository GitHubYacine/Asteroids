import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    highscore = 0
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
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)
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
            for shot in shots:
                if astr.collision_check(shot):
                    shot.kill()
                    highscore += 1
                    astr.split()
        highscore_text = font.render(f"Score: {highscore}", True, (255, 255, 255))
        screen.fill("black")
        for drwb in drawable:
            drwb.draw(screen)
        screen.blit(highscore_text, (10,10))
        pygame.display.flip()
        dt = timer.tick(144) / 1000
    
if __name__ == "__main__":
    main()