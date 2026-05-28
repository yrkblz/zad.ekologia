import unittest
from World import World
from Position import Position
from Organisms.Sheep import Sheep
from WorldRender import WorldRenderer
from TurnManager import TurnManager

class TestWorld(unittest.TestCase):
    def setUp(self):
        # Inicjalizacja pustego świata
        self.world = World(5, 5)

    def test_position_on_board(self):
        # Weryfikacja granic planszy
        self.assertTrue(self.world.positionOnBoard(Position(xPosition=0, yPosition=0)))
        self.assertFalse(self.world.positionOnBoard(Position(xPosition=-1, yPosition=0)))

    def test_add_and_get_organism(self):
        # Zapis i odczyt organizmu na planszy
        sheep = Sheep(position=Position(xPosition=2, yPosition=2), world=self.world)
        self.world.addOrganism(sheep)
        
        self.assertEqual(self.world.getOrganismFromPosition(Position(xPosition=2, yPosition=2)), sheep)
        self.assertIsNone(self.world.getOrganismFromPosition(Position(xPosition=0, yPosition=0)))

class TestTurnManager(unittest.TestCase):
    def setUp(self):
        # Inicjalizacja zarządcy tur
        self.world = World(5, 5)
        self.turn_manager = TurnManager(self.world)

    def test_cleanup_dead_organisms(self):
        # Usuwanie martwych organizmów z planszy
        sheep = Sheep(position=Position(xPosition=1, yPosition=1), world=self.world)
        sheep.liveLength = 1 
        self.world.addOrganism(sheep)
        
        self.turn_manager.makeTurn()
        self.assertNotIn(sheep, self.world.organisms)

    def test_incorporate_new_organisms(self):
        # Przenoszenie nowo narodzonych organizmów na planszę
        baby_sheep = Sheep(position=Position(xPosition=2, yPosition=2), world=self.world)
        self.world.newOrganisms.append(baby_sheep)
        
        self.turn_manager.makeTurn()
        self.assertIn(baby_sheep, self.world.organisms)

class TestWorldRenderer(unittest.TestCase):
    def test_render_empty_and_occupied_fields(self):
        # Renderowanie wizualizacji 
        world = World(2, 2)
        renderer = WorldRenderer(separator='.')
        
        sheep = Sheep(position=Position(xPosition=0, yPosition=0), world=world)
        world.addOrganism(sheep)
        world.turn = 5
        
        output = renderer.render(world)
        self.assertIn('turn: 5', output)
        self.assertIn('S', output)
        self.assertIn('.', output)

if __name__ == '__main__':
    unittest.main()