import pygame
from constants import *


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, nutrition):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.nutrition = nutrition
