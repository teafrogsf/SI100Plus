import pygame
import random
from . import objs

# Player direction
from .statics import Direction, MapSettings
move_directions = [
    (0, -1), # UP
    (1, 0), # RIGHT
    (0, 1), # DOWN
    (-1, 0) # LEFT
]

class Maze:
    """
    Singleton class for the maze.
    
    use maze = Maze() to get the instance of the maze.
    use maze = Maze(row, column) to initialize the maze or generate a new maze.
    """
    _instance = None
    
    def __new__(cls, row: int = None, column: int = None):
        
        if cls._instance is None:
            cls._instance = super(Maze, cls).__new__(cls)
            
        if column is not None and row is not None:
            cls._instance._initialize(row, column)
            
        return cls._instance
        
            
    def _initialize(self, row: int, column: int):
        self.row = 2 * (row // 2) + 1
        self.column = 2 * (column // 2) + 1
        self.player_pos = (0, self.column - 1)
        self.player_dir = Direction.LEFT
        self.exit_pos = (self.row - 1, 0)
        self.generate_maze()
        self.blocks = pygame.sprite.Group()
        self.initialize_gui()
        
    def generate_maze(self):
        self.grid = [[False for x in range(self.column)] for y in range(self.row)]
        
        unvisited = []
        
        for x in range(self.row):
            for y in range(self.column):
                if x % 2 == 0 and y % 2 == 0:
                    unvisited.append((x, y))
                    
        unvisited.remove(self.player_pos)
        
        move_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def pick_next_cell(cell):
            x, y = cell
            while True:
                direction = random.choice(move_directions)
                new_cell = (x + 2 * direction[0], y + 2 * direction[1])
                if 0 <= new_cell[0] < self.row and 0 <= new_cell[1] < self.column:
                    return new_cell
        while unvisited:
            path = []
            start = random.choice(unvisited)
            path.append(start)
            while path[-1] in unvisited:
                next_cell = pick_next_cell(path[-1])
                if next_cell in path:
                    path = path[:path.index(next_cell) + 1]
                else:
                    path.append(next_cell)
            for p in path:
                self.grid[p[0]][p[1]] = True
                if p in unvisited:
                    unvisited.remove(p)
            for i in range(len(path) - 1):
                x = (path[i][0] + path[i + 1][0]) // 2
                y = (path[i][1] + path[i + 1][1]) // 2
                self.grid[x][y] = True
                
        # solve maze by BFS
        queue = [self.player_pos]
        route = dict()
        while queue:
            x, y = queue.pop(0)
            if (x, y) == self.exit_pos:
                break
            for dx, dy in move_directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.row and 0 <= new_y < self.column and self.grid[new_x][new_y] and (new_x, new_y) not in route:
                    queue.append((new_x, new_y))
                    route[(new_x, new_y)] = (x, y)
        self.route = []
        x, y = self.exit_pos
        while (x, y) != self.player_pos:
            self.route.append((x, y))
            x, y = route[(x, y)]
        self.route.append(self.player_pos)
        self.route.reverse()
        
                
    
    def __str__(self) -> str:
        # show maze without route
        # the print format
        s = "#" * (self.column + 2) + "\n"
        for i in range(self.row):
            s += "#"
            for j in range(self.column):
                if(self.exit_pos == (i, j)):
                    s += "E"
                elif (self.player_pos == (i, j)):
                    s += "P"
                else:    
                    s += " " if self.grid[i][j] else "#"
            s += "#\n"
        s += "#" * (self.column + 2)
        return s
    
    def __repr__(self) -> str:
        # show maze with route
        # extra row for better visualization
        s = "##" * (self.column + 2) + "\n"
        for i in range(self.row):
            s += "##"
            for j in range(self.column):
                if (i, j) in self.route:
                    s += "**"
                else:
                    s += "  " if self.grid[i][j] else "##"
            s += "##\n"
        s += "##" * (self.column + 2)
        return s
        
    def initialize_gui(self):
        # # IDK what should be done here
        # self.walls = pygame.sprite.Group()
        # self.player = None
        # self.exit = None
        # # Add the player and exit to the maze
        # pass
        # # Add the walls to the maze
        # pass

        # I think maze should only be responsible for the maze generation
        # and the game manager should be responsible for the GUI

        
        # Gen the maze center
        for i in range(self.row):
            for j in range(self.column):
                if not self.grid[i][j]:
                    self.blocks.add(objs.Block(objs.BlockType.WALL, (i + 1) * MapSettings.blockSize, (j + 1) * MapSettings.blockSize))
                else:
                    self.blocks.add(objs.Block(objs.BlockType.GROUND, (i + 1) * MapSettings.blockSize, (j + 1) * MapSettings.blockSize))
        # Gen the maze border
        for i in range(self.column + 2):
            self.blocks.add(objs.Block(objs.BlockType.WALL, i * MapSettings.blockSize, 0))
            self.blocks.add(objs.Block(objs.BlockType.WALL, i * MapSettings.blockSize, (self.row + 1) * MapSettings.blockSize))
        for j in range(self.row):
            self.blocks.add(objs.Block(objs.BlockType.WALL, 0, (j + 1) * MapSettings.blockSize))
            self.blocks.add(objs.Block(objs.BlockType.WALL, (self.column + 1) * MapSettings.blockSize, (j + 1) * MapSettings.blockSize))
        # Gen Exit
        self.blocks.add(objs.Exit((self.exit_pos[0] + 1) * MapSettings.blockSize, (self.exit_pos[1] + 1) * MapSettings.blockSize))
    
    def update(self):
        self.blocks.update()
        # self.player.update()
        # self.walls.update()
        # self.exit.update()

    def draw(self, screen):
        self.blocks.draw(screen)
        
    