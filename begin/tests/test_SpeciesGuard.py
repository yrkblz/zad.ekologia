import unittest
from World import World
from Position import Position
from Organisms.Sheep import Sheep
from Organisms.Lynx import Lynx
from Organisms.Grass import Grass
from Organisms.Antelope import Antelope
from SpeciesGuard import SpeciesGuard

class TestSpeciesGuard(unittest.TestCase):

    def setUp(self):
        # Inicjalizacja świata i strażnika
        self.world = World(5, 5)
        self.guard = SpeciesGuard()

    def test_apply_bonus_single_survivor(self):
        #nałożenie bonusu dla ostatniego osobnika
        sheep = Sheep(position=Position(xPosition=0, yPosition=0), world=self.world)
        self.world.addOrganism(sheep)
        original_power = sheep.powerToReproduce
        
        self.guard.manage_species(self.world)
        
        self.assertEqual(sheep.powerToReproduce, original_power // SpeciesGuard.BONUS_DIVIDER)
        self.assertIn(sheep, self.guard.buffed_organisms)

    def test_bonus_expires_after_3_turns(self):
        #czy bonus znika po 3 turach
        sheep1 = Sheep(position=Position(xPosition=0, yPosition=0), world=self.world)
        self.world.addOrganism(sheep1)
        original_power = sheep1.powerToReproduce
        
        self.guard.manage_species(self.world) # 
        
        sheep2 = Sheep(position=Position(xPosition=1, yPosition=1), world=self.world)
        self.world.addOrganism(sheep2)
        
        self.guard.manage_species(self.world) # 
        self.guard.manage_species(self.world) #  
        self.guard.manage_species(self.world) # 
        
        self.assertEqual(sheep1.powerToReproduce, original_power)
        self.assertNotIn(sheep1, self.guard.buffed_organisms)

    def test_resurrect_species_when_extinct(self):
        #odrodzenie wymarłych gatunków
        self.guard.manage_species(self.world)
        self.assertEqual(len(self.world.organisms), 4)

    def test_dead_buffed_organism_is_removed(self):
        # usunięcie martwego organizmu ze słownika buffów
        sheep = Sheep(position=Position(xPosition=0, yPosition=0), world=self.world)
        self.world.addOrganism(sheep)
        self.guard.manage_species(self.world)
        
        self.world.organisms.remove(sheep)
        self.guard.manage_species(self.world)
        
        self.assertNotIn(sheep, self.guard.buffed_organisms)

if __name__ == '__main__':
    unittest.main()