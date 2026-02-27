from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import circleshape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = pygame.Vector2(asteroid1.position.x, asteroid1.position.y).rotate(angle) * 1.2
            asteroid2.velocity = pygame.Vector2(asteroid2.position.x, asteroid2.position.y).rotate(-angle) * 1.2


        
