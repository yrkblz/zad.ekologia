from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
import random

class Animal(Organism):
    POWER_REPRODUCTION_PENALTY_DIVIDER = 2 

    def __init__(self, animal=None, position=None, world=None):
        super(Animal, self).__init__(animal, position, world)
        self.__lastPosition = position

    @property
    def lastPosition(self):
        return self.__lastPosition

    @lastPosition.setter
    def lastPosition(self, value):
        self.__lastPosition = value

    def move(self):
        result = []
        candidatePositions = self.getNeighboringPositions() # Zmieniona nazwa
        newPosition = None

        if candidatePositions:
            newPosition = random.choice(candidatePositions)
            result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
            self.lastPosition = self.position
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        return result

    def action(self):
        result = []
        birthPositions = self.getNeighboringBirthPositions() # Zmieniona nazwa

        if self.canReproduce() and birthPositions:
            newAnimalPosition = random.choice(birthPositions)
            newAnimal = self.clone()
            newAnimal.initParams()
            newAnimal.position = newAnimalPosition
            self.power = self.power // self.POWER_REPRODUCTION_PENALTY_DIVIDER
            result.append(Action(ActionEnum.A_ADD, newAnimalPosition, 0, newAnimal))
        return result

    # Poprawione nazewnictwo na liczbę mnogą
    def getNeighboringPositions(self):
        return self.world.getNeighboringPositions(self.position)

    def getNeighboringBirthPositions(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))

	
