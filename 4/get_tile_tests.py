import unittest

from invalid_position_exception import InvalidPositionException
from puzzle_game import PuzzleGame
from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To1X3425786

class GetTileTests(unittest.TestCase):

    """
    All-c-uses/Some-p-uses
    0, 1, 4

    All-p-uses
    0, 1, 3
    0, 1, 4
    0, 2
    """

    def test_path_1_2_5_returns_board_tile(self):
        # [0] -> [1] -> [4]
        game = PuzzleGame(3)
        game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

        # Estado esperado do shuffler:
        # 1  -  3
        # 4  2  5
        # 7  8  6
        self.assertEqual((1, 2), (game.line_of_empty_position, game.column_of_empty_position))
        self.assertEqual(1, game.get_tile(1, 1))

    def test_path_1_2_4_returns_empty_string_for_empty_position(self):
        # [0] -> [1] -> [3]
        game = PuzzleGame(3)
        game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

        self.assertEqual(" ", game.get_tile(game.line_of_empty_position, game.column_of_empty_position))

    def test_path_1_3_raises_invalid_position_exception(self):
        # [0] -> [2]
        game = PuzzleGame(3)
        game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

        with self.assertRaises(InvalidPositionException):
            game.get_tile(0, 1)
