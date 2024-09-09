from enum import Enum

class BlockType(Enum):
    WALL = 0
    GROUND = 1
    EXIT = 2

class ResourcePath:
    player = [r"./assets/facing_up.png", r"./assets/facing_right.png", r"./assets/facing_down.png", r"./assets/facing_left.png"]
    block = [r"./assets/con_wall.png", r"./assets/ground.png", r"./assets/arrow.png", r"./assets/arrow_dark.png"]
    exit = r"./assets/arrow.png"
    font = r"./assets/CaskaydiaCoveNerdFont-SemiLight.ttf"

class MapSettings:
    blockSize = 32
    blockXNum = 25
    blockYNum = 25
    
    maxBlockNum = 35
    minBlockNum = 21
    
    playModeBlockXNum = 13
    playModeBlockYNum = 13

class GameSettings:
    FPS = 30
    Title = "Maze Game"
    WindowHeight = MapSettings.blockSize * (MapSettings.blockYNum + 2)
    WindowWidth = MapSettings.blockSize * (MapSettings.blockXNum + 2) + 500
    CodePaddingLeft = MapSettings.blockSize * (MapSettings.blockXNum + 2) + 10
    
class GameMode(Enum):
    PLAY = 0
    DEBUG = 1
    CHECK = 2

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class MoveDirections:
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    
    @staticmethod
    def get_direction(direction: Direction):
        return MoveDirections.UP if direction == Direction.UP else \
            MoveDirections.RIGHT if direction == Direction.RIGHT else \
            MoveDirections.DOWN if direction == Direction.DOWN else \
            MoveDirections.LEFT