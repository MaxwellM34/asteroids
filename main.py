import pygame
import constants
from logger import log_state
import circleshape
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        player.update(dt)
        log_state()
        player.draw(screen)
        pygame.display.flip()
        
       
        
if __name__ == "__main__":
    main()
