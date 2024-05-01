# Ecosystem Simulation

## Overview
This ecosystem simulation game models the interactions between various creatures and food sources within a virtual environment. The game runs in real-time, allowing creatures to move, eat, and reproduce, based on their internal states and the availability of resources.

## Features
- **Dynamic Creature Behavior:** Creatures have health, hunger, libido, and a lifespan. They seek out food to mitigate hunger and partners to reproduce, depending on their libido levels.
- **Food Regeneration:** Food items periodically appear on the screen. Each piece of food has a nutritional value that contributes to a creature's health when consumed.
- **Reproduction System:** Creatures can reproduce if they meet another creature with sufficient libido. Offspring are added to the ecosystem with inherited and slightly mutated traits.
- **Ecosystem Feedback Loop:** The population dynamics adjust based on the available food sources and creature interactions, providing a self-sustaining ecosystem.

## Modules
- `constants.py`: Defines all constants used across the game, including screen dimensions, creature properties, and color definitions.
- `creature.py`: Implements the creature class, handling movement, eating, health management, and reproduction.
- `creature_manager.py`: Manages all creatures within the game, updating their states and interactions.
- `food.py`: Defines the food class with properties such as position and nutritional value.
- `food_manager.py`: Manages the generation and distribution of food within the game.
- `ecosystem_manager.py`: Coordinates between the creature and food managers, updating the entire game state.
- `main.py`: Contains the game loop and initializes all managers and Pygame settings.

## Running the Simulation
Ensure you have Python and Pygame installed. Start the simulation by running the `main.py` file:
```bash
python main.py
```

## Dependencies
- Python 3.x
- Pygame

## Demo
https://github.com/brendankariniemi/EvolutionSim/assets/138073658/1f94f6ab-b9a9-4928-8f15-ed544fbc5d45



