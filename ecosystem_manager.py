class EcosystemManager:
    def __init__(self, creature_manager, food_manager):
        self.creature_manager = creature_manager
        self.food_manager = food_manager

    def update(self):
        self.food_manager.update()
        self.creature_manager.update(self.food_manager.food_sources)
