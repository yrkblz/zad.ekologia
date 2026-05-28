from .Animal import Animal


class Sheep(Animal):
    INITIAL_POWER = 3
    INITIAL_INITIATIVE = 3
    LIVE_LENGTH = 10
    POWER_TO_REPRODUCE = 6
    SIGN = 'S'

    def __init__(self, sheep=None, position=None, world=None):
        super(Sheep, self).__init__(sheep, position, world)

    def clone(self):
        return Sheep(self, None, None)

    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.LIVE_LENGTH
        self.powerToReproduce = self.POWER_TO_REPRODUCE
        self.sign = self.SIGN

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position)
        )
