from .Plant import Plant

class Grass(Plant):
    INITIAL_POWER = 0
    INITIAL_INITIATIVE = 0
    LIVE_LENGTH = 6
    POWER_TO_REPRODUCE = 3
    SIGN = 'G'

    def __init__(self, grass=None, position=None, world=None):
        super(Grass, self).__init__(grass, position, world)

    def clone(self):
        return Grass(self, None, None)

    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.LIVE_LENGTH
        self.powerToReproduce = self.POWER_TO_REPRODUCE
        self.sign = self.SIGN
