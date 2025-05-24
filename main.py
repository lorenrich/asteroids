import pygame
from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Colors
    black = "#000000"

    # Clock
    clock = pygame.time.Clock()
    clock.tick(60)
    dt = 0/1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(black)

        # Refresh the screen
        pygame.display.flip()



if __name__ == "__main__":
    main()