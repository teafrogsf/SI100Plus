import pygame, sys
from maze.manager import GameManager
from maze.statics import BlockType

manager = GameManager()


def turn_left():
    manager.turn_left()
    manager.update()
    manager.draw()
    pygame.display.flip()

    manager.update()
    manager.draw()
def turn_right():
    manager.turn_right()
    manager.update()
    manager.draw()
    pygame.display.flip()

def move_forward():
    manager.try_move()
    manager.update()
    manager.draw()
    pygame.display.flip()

def try_exit():
    if(manager.try_exit()):
        print("WIN")

def check_front():
    return manager.check_front()

def operation():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    turn_left()
    while(check_front() == BlockType.WALL):
        turn_right()
    move_forward()
    try_exit()
while True:
    operation()
