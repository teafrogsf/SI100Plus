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
        pygame.display.set_caption(f"Maze Game - FPS: {int(self.clock.get_fps())}")
        self.maze.update()

    def draw(self):
        self.maze.draw(self.screen)

    
    # def check_front(self) -> bool:
    #     x, y = self.player_pos
    #     dx, dy = MoveDirections.get_direction(self.player_dir)
    #     x += dx
    #     y += dy
    #     return self.grid[x][y]
    
    # def turn_left(self):
    #     self.player_dir = Direction((self.player_dir.value - 1) % 4)
    
    # def turn_right(self):
    #     self.player_dir = Direction((self.player_dir.value + 1) % 4)
        
    # def try_move(self) -> None:
    #     if self.check_front():
    #         dx, dy = MoveDirections.get_direction(self.player_dir)
    #         x, y = self.player_pos
    #         x += dx
    #         y += dy
    #         self.player_pos = (x, y)
            
    # def try_exit(self) -> bool:
    #     return self.player_pos == self.exit_pos 