import pygame
from .statics import *

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType: BlockType, x: int, y: int):
        super().__init__()
        self.type = blockType
        self.image = pygame.transform.scale(
            pygame.image.load(ResourcePath.block[self.type.value]), 
                (MapSettings.blockSize, MapSettings.blockSize))
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = [pygame.transform.scale(
            pygame.image.load(ResourcePath.player[i]), 
                (MapSettings.blockSize, MapSettings.blockSize)) for i in range(4)]
        self.x, self.y = x, y
        self.prev_x, self.prev_y = x, y
        self.direction = Direction.LEFT
        self.rect = self.image[self.direction.value].get_rect()
        self.rect.topleft = (x * MapSettings.blockSize, y * MapSettings.blockSize) # x, y: x'th row, y'th column; topleft: x'th column, y'th row
        self.moving = False
        self.speed = 0
        self.move_tick = 0
    
    def draw(self, screen):
        screen.blit(self.image[self.direction.value], self.rect)
        
    def change_direction(self, direction: Direction):
        self.direction = direction
    
    def move_forward(self):
        dx, dy = MoveDirections.get_direction(self.direction)
        x, y = self.x, self.y
        x += dx
        y += dy
        self.prev_x, self.prev_y = self.x, self.y
        self.x, self.y = (x, y)
        self.rect.topleft = (x * MapSettings.blockSize, y * MapSettings.blockSize)

class Exit(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(ResourcePath.exit), 
                (MapSettings.blockSize, MapSettings.blockSize))
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class CodeText:
    def __init__(self, x: int, y: int, text: list[str], textSize: int = 20, vDist: int = 3):
        self._fontColor = (255, 255, 255)
        self.x, self.y = x, y
        self.width, self.height = GameSettings.WindowWidth - x, GameSettings.WindowHeight - y
        self._bg = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._bg.fill((0, 0, 0, 100))
        self.highlightLine = -1
        self.text = text
        self.totalLines = len(self.text)
        self.font = pygame.font.Font(ResourcePath.font, textSize)
        self._vDist = vDist
        self._textSize = textSize
        self._highlightMask = pygame.Surface((self.width, self._textSize + self._vDist), pygame.SRCALPHA)
        self._highlightMask.fill((255, 255, 255, 100))
        self._highlightRect = self._highlightMask.get_rect()

    def draw(self, screen: pygame.Surface):
        screen.blit(self._bg, (self.x, self.y))

        offset = 0
        for line in self.text:
            assert isinstance(line, str)
            screen.blit(self.font.render(line, True, self._fontColor),
                        (self.x, self.y + offset))
            offset += self._textSize + self._vDist
        if self.highlightLine != -1:
            screen.blit(self._highlightMask, 
                        (self.x, self.y + self.highlightLine * (self._textSize + self._vDist)))
    
    def setHighlightLine(self, line: int, screen: pygame.Surface):
        # restore the previous line
        self._highlightMask.fill((0, 0, 0, 255))
        screen.blit(self._highlightMask, 
                    (self.x, self.y + self.highlightLine * (self._textSize + self._vDist)))
        screen.blit(self.font.render(self.text[self.highlightLine], True, self._fontColor),
                    (self.x, self.y + self.highlightLine * (self._textSize + self._vDist)))

        # highlight the current line
        self.highlightLine = line - 1
        self._highlightMask.fill((255, 255, 255, 100))
        screen.blit(self._highlightMask, 
                    (self.x, self.y + self.highlightLine * (self._textSize + self._vDist)))