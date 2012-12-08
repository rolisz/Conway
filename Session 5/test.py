
from main import *
import unittest

class GameTest(unittest.TestCase):

    def test_cell_with_too_few_neighbours_dies(self):
        lives = cell_lives_in_next_generation(previous_state=True, neighbour_count=1)
        self.assertFalse(lives)

    def test_cell_with_too_many_neighbours_dies(self):
        lives = cell_lives_in_next_generation(previous_state=True, neighbour_count=4)
        self.assertFalse(lives)

    def test_cell_with_2_neighbours_lives(self):
        lives = cell_lives_in_next_generation(previous_state=True, neighbour_count=2)
        self.assertTrue(lives)

    def test_cell_with_3_neighbours_lives(self):
        lives = cell_lives_in_next_generation(previous_state=True, neighbour_count=3)
        self.assertTrue(lives)

    def test_dead_cell_with_3_neighbours_resurects(self):
        lives = cell_lives_in_next_generation(previous_state=False, neighbour_count=3)
        self.assertTrue(lives)

    def test_dead_cell_with_other_then_3_neighbours_remains_dead(self):
        for neighbours in range(1,10):
            if neighbours != 3:
                lives = cell_lives_in_next_generation(previous_state=False, neighbour_count=neighbours)
                self.assertFalse(lives)

    def test_initializing_universe(self):
        u = Universe()
        self.assertEqual(u.cellCount(),0)

    def test_adding_cells(self):
        u = Universe()
        u.resurect(0,0)
        self.assertEqual(u.cellCount(),1)

    def test_cell_death(self):
        u = Universe()
        u.resurect(0,0)
        u.die(0,0)
        self.assertEqual(u.cellCount(),0)

    def test_cell_neighbors(self):
        u = Universe()
        u.resurect(0,0)
        u.resurect(0,1)
        self.assertEqual(u.nrNeighbors(0,0),1)
        u.resurect(1,0)
        self.assertEqual(u.nrNeighbors(0,0),2)
        u.die(0,1)
        self.assertEqual(u.nrNeighbors(0,0),1)

    def test_equal_universes(self):
        u = Universe()
        u2 = Universe()
        u.resurect(0,0)
        u2.resurect(0,0)
        self.assertEqual(u,u2)

    def test_dead_neighbors(self):
        u = Universe()
        u.resurect(0,0)
        self.assertEqual(len(u.deadNeighbors(0,0)),8)
        u.resurect(0,1)
        self.assertEqual(len(u.deadNeighbors(0,0)),7)

    def test_lonely_cell_in_universe_dies(self):
        u = Universe()
        u.resurect(0,0)
        t = u.tick()
        self.assertEqual(t.cellCount(),0)

    def test_square_is_constant(self):
        u = Universe()
        u.resurect(0,0)
        u.resurect(0,1)
        u.resurect(1,0)
        u.resurect(1,1)
        t =u.tick()
        self.assertEqual(t.cellCount(),4)

    def test_vertical_line_to_horizontal_line_universe_transition(self):
        u = Universe()
        u.resurect(1,0)
        u.resurect(1,1)
        u.resurect(1,2)
        expected_universe = Universe()
        expected_universe.resurect(0,1)
        expected_universe.resurect(1,1)
        expected_universe.resurect(2,1)
        transformed_universe = u.tick()
        print(u)
        print(expected_universe)
        self.assertEqual(transformed_universe, expected_universe)
