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