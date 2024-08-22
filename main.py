import pygame
from constants import *
from player import *


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=5)
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
        screen.fill("black")
        for drwb in drawable:
            drwb.draw(screen)
        pygame.display.flip()
        dt = timer.tick(144) / 1000
    
if __name__ == "__main__":
    main()