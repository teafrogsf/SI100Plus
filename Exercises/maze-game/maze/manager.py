import pygame
from random import randint
from maze.maze import Maze
from maze.statics import BlockType, Direction, GameSettings, MapSettings, MoveDirections, ResourcePath, GameMode
from maze.objs import CodeText, Player


class GameManager:
    """
    Singleton class for the game manager.
    Update and draw the game.
    """
    _instance = None
    _temp_tick = 0

    def __new__(cls, mode: GameMode):
        if cls._instance is None:
            pygame.init()
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def _initalize_play_mode(self):
        """
        Play mode initialization.
        No code display, controled by keyboard, smaller maze.
        """
        self.maze = Maze(MapSettings.playModeBlockXNum,
                         MapSettings.playModeBlockYNum)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (MapSettings.blockSize * (MapSettings.playModeBlockXNum + 2), MapSettings.blockSize * (MapSettings.playModeBlockYNum + 2)))
        self.player = Player(
            self.maze.player_pos[0] + 1, self.maze.player_pos[1] + 1)

    def _initialize_debug_mode(self):
        """
        Debug mode initialization.
        Code display, step by step execution, full maze.
        1 test case.
        """
        self.maze = Maze(MapSettings.blockXNum, MapSettings.blockYNum)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (GameSettings.WindowWidth, GameSettings.WindowHeight))
        self.player = Player(
            self.maze.player_pos[0] + 1, self.maze.player_pos[1] + 1)
        with open("./logic.py", "r") as f:
            file = [line.replace("\n", "").replace("    ", "  ")
                    for line in f.readlines()]
            self.codeText = CodeText(GameSettings.CodePaddingLeft, 0, file)

    def _initialize_check_mode(self):
        """
        Check mode initialization.
        No code display, various maze sizes, auto execution.
        5 test cases.
        """
        self.clock = pygame.time.Clock()
    
    def generate_test_case(self):
        if self.mode != GameMode.CHECK:
            return
        self.ended = False
        blockXNum = randint(MapSettings.minBlockNum, MapSettings.maxBlockNum)
        blockYNum = randint(MapSettings.minBlockNum, MapSettings.maxBlockNum)
        self.maze = Maze(blockXNum, blockYNum)
        self.screen = pygame.display.set_mode(
            (MapSettings.blockSize * (self.maze.row + 2), MapSettings.blockSize * (self.maze.column + 2)))
        self.player = Player(
            self.maze.player_pos[0] + 1, self.maze.player_pos[1] + 1)

    def __init__(self, mode: GameMode):
        self.mode = mode
        if mode == GameMode.PLAY:
            self._initalize_play_mode()
        elif mode == GameMode.DEBUG:
            self._initialize_debug_mode()
        elif mode == GameMode.CHECK:
            self._initialize_check_mode()

    def update(self):
        pygame.display.set_caption(
            f"Maze Game - FPS: {int(self.clock.get_fps())}")
        # self._temp_tick += 1
        # if self._temp_tick > 30:
        #     self.turn_right()
        #     self._temp_tick = 0
        self.maze.update()

    def draw(self):
        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        if self.mode == GameMode.DEBUG:
            self.codeText.draw(self.screen)

    def highlightCode(self, line: int):
        self.codeText.setHighlightLine(line, self.screen)

    def move_draw(self):
        # Incremental Draw for Move
        player_prev_x, player_prev_y = self.player.prev_x, self.player.prev_y
        # Resume previous block
        # Get image from block type
        image = pygame.transform.scale(
            pygame.image.load(ResourcePath.block[BlockType(self.maze.grid[player_prev_x - 1][player_prev_y - 1]).value]),
            (MapSettings.blockSize, MapSettings.blockSize))
        self.screen.blit(image,
                         (player_prev_x * MapSettings.blockSize, player_prev_y * MapSettings.blockSize))
        self.player.draw(self.screen)

    def turn_draw(self):
        # Incremental Draw for Turn
        player_x, player_y = self.player.x, self.player.y
        image = pygame.transform.scale(
            pygame.image.load(ResourcePath.block[BlockType.GROUND.value]),
            (MapSettings.blockSize, MapSettings.blockSize))
        self.screen.blit(image,
                         (player_x * MapSettings.blockSize, player_y * MapSettings.blockSize))
        self.player.draw(self.screen)

    def check_front(self) -> BlockType:
        x, y = self.player.x, self.player.y
        dx, dy = MoveDirections.get_direction(self.player.direction)
        x += dx
        y += dy
        if (x < 1 or x > self.maze.row or y < 1 or y > self.maze.column):
            return BlockType.WALL
        # TODO: Change single bool to multi BlockType
        return BlockType(self.maze.grid[x - 1][y - 1])

    def turn_left(self):
        self.player.direction = Direction(
            (self.player.direction.value - 1) % 4)

    def turn_right(self):
        self.player.direction = Direction(
            (self.player.direction.value + 1) % 4)

    def try_move(self) -> None:
        if self.check_front() == BlockType.GROUND or self.check_front() == BlockType.COIN:
            # TODO: Coin
            self.player.move_forward()

    def try_exit(self) -> bool:
        # return (self.player.x, self.player.y) == self.maze.exit_pos
        return (self.player.x - 1, self.player.y - 1) == self.maze.exit_pos

    def end_game(self, message: str = ""):
        if self.mode == GameMode.CHECK:
            self.ended = True
            print(message)
        else:
            print(message)
            pygame.quit()
            exit()
