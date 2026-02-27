import pygame
import sys
import constants
from logger import log_state, log_event
import circleshape
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black")
        updatable.update(dt)
        log_state()
        for drawables in drawable:
            drawables.draw(screen)   
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    
                    shot.kill()
        pygame.display.flip()
        
       
        
if __name__ == "__main__":
    main()
