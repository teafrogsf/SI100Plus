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
        self.direction = Direction.LEFT
        self.rect = self.image[self.direction.value].get_rect()
        self.rect.topleft = (y * MapSettings.blockSize, x * MapSettings.blockSize) # x, y: x'th row, y'th column; topleft: x'th column, y'th row
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
        self.x, self.y = (x, y)
        self.rect.topleft = (x * MapSettings.blockSize, y * MapSettings.blockSize)

class Exit(pygame.sprite.Sprite):
    def __init__(self, image, x: int, y: int):
        super().__init__()
        self.image = image
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)