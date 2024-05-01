import random
import pygame
from constants import *
from ecosystem_manager import EcosystemManager
from creature_manager import CreatureManager
from food_manager import FoodManager

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ecosystem Simulation')

# Initialize managers
creature_manager = CreatureManager()
food_manager = FoodManager()
ecosystem_manager = EcosystemManager(creature_manager, food_manager)

creature_manager.init_creatures()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    ecosystem_manager.update()

    print(len(creature_manager.creatures))

    creature_manager.creatures.draw(screen)
    food_manager.food_sources.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
