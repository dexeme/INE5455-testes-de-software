import unittest

from puzzle_game import PuzzleGame
from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame2x2To1X32

class ClasseTestes(unittest.TestCase):
    def test_path_0_1_2_3_4_returns_true(self):
        # 0, 1, 2, 3, 4
        game = PuzzleGame(2)
        game.shuffle(TestingShufflerPuzzleGame2x2To1X32())

        changed = game.move_tile(1)

        self.assertTrue(changed)
        self.assertEqual((1, 1), (game.line_of_empty_position, game.column_of_empty_position))
        self.assertEqual(1, game.get_tile(1, 2))

    def test_path_0_1_2_5_returns_false(self):
        # 0, 1, 2, 5
        game = PuzzleGame(2)
        game.shuffle(TestingShufflerPuzzleGame2x2To1X32())

        changed = game.move_tile(3)

        self.assertFalse(changed)
        self.assertEqual((1, 2), (game.line_of_empty_position, game.column_of_empty_position))

class TestMoveTileBranchCoverage(unittest.TestCase):
    def test_path_0_1_2_5_first_condition_false(self):
        # 0, 1, 2, 3, 4
        game = PuzzleGame(2)

        game.dic_positions_of_tiles[1] = (0, 1)

        changed = game.move_tile(1)

        self.assertFalse(changed)

    def test_path_0_1_2_3_5_second_condition_false(self):
        # 0, 1, 2, 5
        game = PuzzleGame(2)
        game.shuffle(TestingShufflerPuzzleGame2x2To1X32())

        changed = game.move_tile(3) # N a

        self.assertFalse(changed)

    def test_path_0_1_2_3_4_second_condition_true(self):
        # 0, 1, 2, 3
        game = PuzzleGame(2)
        game.shuffle(TestingShufflerPuzzleGame2x2To1X32())

        changed = game.move_tile(1)  # A

        self.assertTrue(changed)