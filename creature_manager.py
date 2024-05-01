import random
import pygame
from creature import Creature
from constants import *


class CreatureManager:
    def __init__(self):
        self.creatures = pygame.sprite.Group()

    def init_creatures(self):
        for _ in range(INITIAL_CREATURE_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            creature = Creature(x, y)
            self.creatures.add(creature)

    def update(self, food_group):
        for creature in self.creatures:
            creature.update(food_group, self.creatures)
            self.find_mate(creature, self.creatures)
            self.find_food(creature, food_group)

    def find_mate(self, creature, creature_group):
        potential_partners = pygame.sprite.spritecollide(creature, creature_group, False)
        for partner in potential_partners:
            if creature != partner and creature.libido > creature.libido_threshold and partner.libido > partner.libido_threshold:
                child = creature.mate(partner)
                if child:
                    self.creatures.add(child)

    def find_food(self, creature, food_group):
        potential_food = pygame.sprite.spritecollide(creature, food_group, True)
        for food in potential_food:
            creature.eat(food)
