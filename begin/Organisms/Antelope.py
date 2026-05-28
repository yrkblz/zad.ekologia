from .Animal import Animal
from .Lynx import Lynx
from Action import Action
from ActionEnum import ActionEnum
from Position import Position

class Antelope(Animal):
    INITIAL_POWER = 4
    INITIAL_INITIATIVE = 3
    LIVE_LENGTH = 11
    POWER_TO_REPRODUCE = 5
    SIGN = 'A'
    ESCAPE_DISTANCE = 2
    
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

    
    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position)
        )

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
        
        pos_1 = Position(xPosition=self.position.x + dx, yPosition=self.position.y + dy)
        pos_2 = Position(xPosition=self.position.x + (self.ESCAPE_DISTANCE * dx), yPosition=self.position.y + (self.ESCAPE_DISTANCE * dy))
        
       
        if self.world.positionOnBoard(pos_2) and self.world.getOrganismFromPosition(pos_1) is None:
            metOrganismPos2 = self.world.getOrganismFromPosition(pos_2)
            
            if metOrganismPos2 is None or not isinstance(metOrganismPos2, Lynx):
                result.append(Action(ActionEnum.A_MOVE, pos_2, 0, self))
                self.lastPosition = self.position
                if metOrganismPos2 is not None:
                    result.extend(metOrganismPos2.consequences(self))
                return result
            
        if self.world.positionOnBoard(pos_1):
            metOrganismPos1 = self.world.getOrganismFromPosition(pos_1)
            if metOrganismPos1 is None or not isinstance(metOrganismPos1, Lynx):
                result.append(Action(ActionEnum.A_MOVE, pos_1, 0, self))
                self.lastPosition = self.position
                if metOrganismPos1 is not None:
                    result.extend(metOrganismPos1.consequences(self))
                return result
        result.append(Action(ActionEnum.A_MOVE, lynx_position, 0, self))
        self.lastPosition = self.position
        result.extend(lynx_organism.consequences(self))
            
        return result