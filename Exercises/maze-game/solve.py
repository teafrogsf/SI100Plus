import pygame, sys
from maze.manager import GameManager
from maze.statics import BlockType
import threading, time

manager = GameManager()

def turn_left():
    manager.turn_left()
    manager.update()
    manager.turn_draw()
    # pygame.display.flip()

def turn_right():
    manager.turn_right()
    manager.update()
    manager.turn_draw()
    # pygame.display.flip()

def move_forward():
    manager.try_move()
    manager.update()
    manager.move_draw()
    # pygame.display.flip()

def try_exit():
    if(manager.try_exit()):
        print("WIN")
        manager.clock.tick(0.25)
        pygame.quit()
        sys.exit()

def check_front():
    return manager.check_front()

def _operation():
    from logic import operation
    while True:
        operation()
        time.sleep(0.01)

def main():
    # Initial Draw
    manager.draw()
    pygame.display.flip()
    thread = threading.Thread(target=_operation)
    thread.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        manager.clock.tick(60)
        pygame.display.flip()

    

if __name__ == "__main__":
    print("Run this file in logic.py")