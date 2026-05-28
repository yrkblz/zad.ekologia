from .Animal import Animal

class Lynx(Animal):
    INITIAL_POWER = 6
    INITIAL_INITIATIVE = 5
    LIVE_LENGTH = 18
    POWER_TO_REPRODUCE = 14
    SIGN = 'R'

    def __init__(self, lynx=None, position=None, world=None):
        super(Lynx, self).__init__(lynx, position, world)

    def clone(self):
        return Lynx(self, None, None)

    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.LIVE_LENGTH
        self.powerToReproduce = self.POWER_TO_REPRODUCE
        self.sign = self.SIGN

    def getNeighboringPosition(self):
        all_neighboring_positions = self.world.getNeighboringPositions(self.position)
        valid_position = []
        
        for field in all_neighboring_positions:
            candidate_organism = self.world.getOrganismFromPosition(field)
            
            if not isinstance(candidate_organism, Lynx):
                valid_position.append(field)
        return valid_position