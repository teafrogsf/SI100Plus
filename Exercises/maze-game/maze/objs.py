import pygame
from .maze import Maze, Direction

class GameManager:
    """
    Singleton class for the game manager.
    Update and draw the game.
    """
    _instance = None    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.maze = Maze(25, 25)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x: int, y: int):
        super().__init__()
        self.image = image
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x: int, y: int):
        super().__init__()
        self.image = image
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = Direction.LEFT
        self.moving = False
        self.speed = 0
        self.move_tick = 0
        
    def change_direction(self, direction: Direction):
        pass
    
    def move_forward(self):
        pass

class Exit(pygame.sprite.Sprite):
    def __init__(self, image, x: int, y: int):
        super().__init__()
        self.image = image
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)