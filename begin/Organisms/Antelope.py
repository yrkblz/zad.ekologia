from .Sheep import Sheep
from .Lynx import Lynx
from Action import Action
from ActionEnum import ActionEnum
from Position import Position

class Antelope(Sheep):
    INITIAL_POWER = 4
    INITIAL_INITIATIVE = 3
    LIVE_LENGTH = 11
    POWER_TO_REPRODUCE = 5
    SIGN = 'A'
    
    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)
        
    def clone(self):
        return Antelope(self, None, None)
    
    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.LIVE_LENGTH
        self.powerToReproduce = self.POWER_TO_REPRODUCE
        self.sign = self.SIGN

    def move(self):
        lynx_position, lynx_organism = self.__scanForLynx()
        
        if lynx_position is not None:
            return self.__escapeORattack(lynx_position, lynx_organism)
        
        return super(Antelope, self).move()
    
    def __scanForLynx(self):
        neighboring_positions = self.world.getNeighboringPositions(self.position)
        
        for position in neighboring_positions:
            candidate_organism = self.world.getOrganismFromPosition(position)
            
            if isinstance(candidate_organism, Lynx):
                return position, candidate_organism
        
        return None, None
    
    def __escapeORattack(self, lynx_position, lynx_organism):
        result = []
        dx = self.position.x - lynx_position.x
        dy = self.position.y - lynx_position.y
        escape_position = Position(xPosition=self.position.x + (2 * dx), yPosition=self.position.y + (2 * dy))
        
        if self.world.positionOnBoard(escape_position):
            result.append(Action(ActionEnum.A_MOVE, escape_position, 0, self))
            self.lastPosition = self.position
            
            metOrganism = self.world.getOrganismFromPosition(escape_position)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        else:
            result.append(Action(ActionEnum.A_MOVE, lynx_position, 0, self))
            self.lastPosition = self.position
            result.extend(lynx_organism.consequences(self))
            
        return result