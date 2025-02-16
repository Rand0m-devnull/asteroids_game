import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
 
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("#000000")
        
        for object in drawable:
            object.draw(screen)
   
        pygame.display.flip()

        dt = clock.tick(60)/1000       
       

if __name__ == "__main__":
    main()
    