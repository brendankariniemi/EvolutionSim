import random
import pygame
from food import Food
from constants import *


class FoodManager:
    def __init__(self):
        self.food_sources = pygame.sprite.Group()

    def update(self):
        if len(self.food_sources) < FOOD_REGEN_RATE:
            x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
            nutrition = random.randint(NUTRITION_MAX // 2, NUTRITION_MAX)
            self.food_sources.add(Food(x, y, nutrition))