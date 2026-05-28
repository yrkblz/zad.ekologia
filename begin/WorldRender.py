from Position import Position

class WorldRenderer(object):

    
    def __init__(self, separator='.'):
        self.__separator = separator
        
    def render(self, world):
        result = '\nturn: ' + str(world.turn)
        
        if world.plagueTurns > 0:
            result += ' [PLAGA AKTYWNA - pozostało tur: ' + str(world.plagueTurns) + ']'
            
        result += '\n'
        
        
        result += '  ' 
        for x in range(0, world.worldX):
            result += str(x) + ' '
        result += '\n'
        
         
        for y in range(0, world.worldY):
            result += str(y) + ' '
            for x in range(0, world.worldX):
                org = world.getOrganismFromPosition(Position(xPosition=x, yPosition=y))
                if org:
                    
                    result += str(org.sign) + ' ' 
                else:
                
                    result += self.__separator + ' '
            result += '\n'
            
        return result
