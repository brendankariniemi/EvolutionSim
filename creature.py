import random
import pygame
from constants import *


class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, health=None, lifespan=None, hunger_threshold=None, libido_threshold=None,
                 health_decrement=None, hunger_increment=None, libido_increment=None):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(x, y))

        # Set defaults if None
        self.health = health if health is not None else random.randint(HEALTH_MAX // 2, HEALTH_MAX)
        self.lifespan = lifespan if lifespan is not None else random.randint(LIFESPAN_MAX // 2, LIFESPAN_MAX)
        self.hunger_threshold = hunger_threshold if hunger_threshold is not None else random.randint(HUNGER_MAX // 2, HUNGER_MAX)
        self.libido_threshold = libido_threshold if libido_threshold is not None else random.randint(LIBIDO_MAX // 2, LIBIDO_MAX)
        self.health_decrement = health_decrement if health_decrement is not None else random.randint(HEALTH_DECREMENT_MAX // 2, HEALTH_DECREMENT_MAX)
        self.hunger_increment = hunger_increment if hunger_increment is not None else random.randint(HUNGER_INCREMENT_MAX // 2, HUNGER_INCREMENT_MAX)
        self.libido_increment = libido_increment if libido_increment is not None else random.randint(LIBIDO_INCREMENT_MAX // 2, LIBIDO_INCREMENT_MAX)

        # Initialize other attributes
        self.hunger = 0
        self.libido = 0
        self.age = 0
        self.full_health = self.health

    def update(self, food_group, creature_group):
        self.hunger += self.hunger_increment
        self.libido += self.libido_increment
        self.age += 1

        if self.hunger >= self.hunger_threshold:
            self.health -= self.health_decrement
        else:
            self.health += self.health_decrement // 2
            self.health = min(self.health, self.full_health)

        if self.health <= 0 or self.age >= self.lifespan:
            self.kill()
            return

        # Determine behavior based on current state
        if self.hunger > self.hunger_threshold:
            self.search_for_food(food_group)
        elif self.libido > self.libido_threshold:
            self.search_for_mate(creature_group)
        else:
            self.wander()

    def search_for_food(self, food_group):
        closest_food = self.find_closest_sprite(food_group)
        if closest_food is not None:
            self.move_towards_target(closest_food)

    def search_for_mate(self, creature_group):
        # Exclude self from potential partners by creating a new group without self
        potential_partners = creature_group.copy()
        potential_partners.remove(self)
        closest_mate = self.find_closest_sprite(potential_partners)
        if closest_mate:
            self.move_towards_target(closest_mate)

    def wander(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    def eat(self, food):
        self.hunger -= food.nutrition
        if self.hunger < 0:
            self.hunger = 0

    def mate(self, partner):
        self.libido = 0
        partner.libido = 0

        if random.random() < REPRODUCTION_PROBABILITY:
            x = (self.rect.x + partner.rect.x) // 2
            y = (self.rect.y + partner.rect.y) // 2
            child = Creature(x, y)
            return child
        return None

    def find_closest_sprite(self, group):
        closest_sprite = None
        min_distance = float('inf')

        for sprite in group:
            distance_squared = (self.rect.centerx - sprite.rect.centerx) ** 2 + (
                    self.rect.centery - sprite.rect.centery) ** 2
            if distance_squared < min_distance:
                closest_sprite = sprite
                min_distance = distance_squared

        return closest_sprite

    def move_towards_target(self, target):
        # Calculate the direction vector to the target
        target_dx = target.rect.centerx - self.rect.centerx
        target_dy = target.rect.centery - self.rect.centery

        # Normalize the direction vector
        distance = max(1, (target_dx ** 2 + target_dy ** 2) ** 0.5)
        direction_vector = (target_dx / distance, target_dy / distance)

        # Move the creature towards the target
        self.rect.centerx += direction_vector[0]
        self.rect.centery += direction_vector[1]
