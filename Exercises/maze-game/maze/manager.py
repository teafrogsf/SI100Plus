import pygame
from maze.maze import Maze
from maze.statics import BlockType, Direction, GameSettings, MapSettings, MoveDirections
from maze.objs import Player

class GameManager:
    """
    Singleton class for the game manager.
    Update and draw the game.
    """
    _instance = None    
    _temp_tick = 0
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.maze = Maze(MapSettings.blockXNum, MapSettings.blockYNum)
        print(self.maze)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (GameSettings.WindowWidth, GameSettings.WindowHeight))
        # self.player = Player(1, self.maze.column)
        self.player = Player(self.maze.player_pos[0] + 1, self.maze.player_pos[1] + 1)
        

    def update(self):
        pygame.display.set_caption(f"Maze Game - FPS: {int(self.clock.get_fps())}")
        # self._temp_tick += 1
        # if self._temp_tick > 30:
        #     self.turn_right()
        #     self._temp_tick = 0
        self.maze.update()

    def draw(self):
        self.maze.draw(self.screen)
        self.player.draw(self.screen)

    
    def check_front(self) -> BlockType:
        x, y = self.player.x, self.player.y
        dx, dy = MoveDirections.get_direction(self.player.direction)
        x += dx
        y += dy
        return BlockType(self.maze.grid[x - 1][y - 1]) # TODO: Change single bool to multi BlockType
        # TODO: Fix grid: add border!!!
    
    def turn_left(self):
        self.player.direction = Direction((self.player.direction.value - 1) % 4)
    
    def turn_right(self):
        self.player.direction = Direction((self.player.direction.value + 1) % 4)
        
    def try_move(self) -> None:
        if self.check_front() == BlockType.GROUND or self.check_front() == BlockType.COIN:
            # TODO: Coin
            self.player.move_forward()
            
    def try_exit(self) -> bool:
        return (self.player.x, self.player.y) == self.maze.exit_pos