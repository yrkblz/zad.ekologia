import random
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx
from Organisms.Antelope import Antelope

class SpeciesGuard(object):
    def __init__(self):
        self.tracked_species = [Grass, Sheep, Lynx, Antelope]
        self.buffed_organisms = {}

    def manage_species(self, world):
        self.__manage_buffs()

        counts = {cls: 0 for cls in self.tracked_species}
        survivors = {cls: [] for cls in self.tracked_species}
        
        
        for org in world.organisms:
            org_cls = type(org)
            if org_cls in counts:
                counts[org_cls] += 1
                survivors[org_cls].append(org)

       
        for cls, count in counts.items():
            if count == 1:
                last_survivor = survivors[cls][0]
                self.__apply_bonus(last_survivor)
            elif count == 0:
                self.__resurrect_species(cls, world)

    def __apply_bonus(self, organism):
        """Nakłada bonus reprodukcyjny na 3 tury (jeśli nie jest już nałożony)"""
        if organism not in self.buffed_organisms:
            original = organism.powerToReproduce
            organism.powerToReproduce = organism.powerToReproduce // 2
            self.buffed_organisms[organism] = (3, original)

    def __manage_buffs(self):
        """Odlicza czas trwania bonusu i cofa go po 3 turach"""
        expired = []
        for org, (turns_left, original) in self.buffed_organisms.items():
            turns_left -= 1
            if turns_left <= 0:
                expired.append(org)
            else:
                self.buffed_organisms[org] = (turns_left, original)
        
        for org in expired:
            org.powerToReproduce = self.buffed_organisms[org][1]
            del self.buffed_organisms[org]

    def __resurrect_species(self, cls, world):
        """Spawnuje organizm na losowym wolnym polu"""
        all_fields = []
        for y in range(world.worldY):
            for x in range(world.worldX):
                all_fields.append(Position(xPosition=x, yPosition=y))
        
        free_fields = world.filterFreePositions(all_fields)
        if free_fields:
            spawn_pos = random.choice(free_fields)
            new_org = cls(position=spawn_pos, world=world)
            world.addOrganism(new_org)