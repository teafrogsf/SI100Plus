import pygame, sys
from maze.statics import GameMode
from maze.manager import GameManager

manager = GameManager(GameMode.PLAY)
manager.draw()
pygame.display.flip()

# Main Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                manager.try_move()
                manager.update()
                manager.move_draw()
                pygame.display.flip()
            elif event.key == pygame.K_a:
                manager.turn_left()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif event.key == pygame.K_d:
                manager.turn_right()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif event.key == pygame.K_RETURN:
                if(manager.try_exit()):
                    manager.end_game("You Win!")

    manager.clock.tick(30) # Frame 30fps