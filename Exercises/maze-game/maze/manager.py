import pygame
from maze.maze import Maze
from maze.statics import GameSettings, MapSettings

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
        self.maze = Maze(MapSettings.blockXNum, MapSettings.blockYNum)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (GameSettings.WindowWidth, GameSettings.WindowHeight))
        

    def update(self):
        self.maze.update()

    def draw(self):
        self.maze.draw(self.screen)