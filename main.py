import pygame
from constants import *
from player import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Colors
    black = (0, 0, 0)

    # Clock
    clock = pygame.time.Clock()
    clock.tick(60)

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    radius = PLAYER_RADIUS
    player = Player(x, y, radius)

    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(black)

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        # Update updatable objects
        updatable.update(dt)

        # For object in the drawable group, draw it on the screen
        for i in drawable:
            i.draw(screen)
        

        # Refresh the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()