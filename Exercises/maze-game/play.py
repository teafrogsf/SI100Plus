import pygame, sys
from maze import Maze
from maze.statics import *
from maze.manager import GameManager

manager = GameManager()

# Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                manager.try_move()
            elif event.key == pygame.K_a:
                manager.turn_left()
            elif event.key == pygame.K_d:
                manager.turn_right()
            elif event.key == pygame.K_RETURN:
                manager.try_exit()
    
    keys = pygame.key.get_pressed()


    manager.update()
    manager.draw()
    manager.clock.tick(30) # Frame 30fps
    pygame.display.flip()