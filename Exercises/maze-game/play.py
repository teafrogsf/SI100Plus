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
    
    keys = pygame.key.get_pressed()

    manager.update()
    manager.draw()
    manager.clock.tick(30) # Frame 30fps
    pygame.display.flip()