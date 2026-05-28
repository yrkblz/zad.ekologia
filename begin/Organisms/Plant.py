from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
import random

class Plant(Organism):
    POWER_REPRODUCTION_PENALTY_DIVIDER = 2

    def __init__(self, plant=None, position=None, world=None):
        super(Plant, self).__init__(plant, position, world)

    def move(self):
        result = []
        return result

    def action(self):
        result = []
        newPlant = None
        newPosition = None

        if self.canReproduce():
            # Całkowite usunięcie ponglisha z kodu
            candidatePositions = self.getFreeNeighboringPositions(self.position)

            if candidatePositions:
                newPosition = random.choice(candidatePositions)
                newPlant = self.clone()
                newPlant.initParams()
                newPlant.position = newPosition
                self.power = self.power // self.POWER_REPRODUCTION_PENALTY_DIVIDER
                result.append(Action(ActionEnum.A_ADD, newPosition, 0, newPlant))
        return result

    # Liczba mnoga
    def getFreeNeighboringPositions(self, position):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(position))
