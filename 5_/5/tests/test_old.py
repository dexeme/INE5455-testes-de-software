import unittest

from conteudo.puzzle_game import PuzzleGame, InvalidPositionException
from tests.shufflers_for_testing_puzzles import *

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

    changed = game.move_tile(3)  # N a

    self.assertFalse(changed)

  def test_path_0_1_2_3_4_second_condition_true(self):
    # 0, 1, 2, 3
    game = PuzzleGame(2)
    game.shuffle(TestingShufflerPuzzleGame2x2To1X32())

    changed = game.move_tile(1)  # A

    self.assertTrue(changed)

  class GetTileTests(unittest.TestCase):
    """
    [1] -> [3]
    [1] -> [2] -> [4]
    [1] -> [2] -> [5]
    """

    def test_path_1_2_5_returns_board_tile(self):
      # [1] -> [2] -> [5]
      game = PuzzleGame(3)
      game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

      # Estado esperado do shuffler:
      # 1  -  3
      # 4  2  5
      # 7  8  6
      self.assertEqual((1, 2), (game.line_of_empty_position, game.column_of_empty_position))
      self.assertEqual(1, game.get_tile(1, 1))

    def test_path_1_2_4_returns_empty_string_for_empty_position(self):
      # [1] -> [2] -> [4]
      game = PuzzleGame(3)
      game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

      self.assertEqual(" ", game.get_tile(game.line_of_empty_position, game.column_of_empty_position))

    def test_path_1_3_raises_invalid_position_exception(self):
      # [1] -> [3]
      game = PuzzleGame(3)
      game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())

      with self.assertRaises(InvalidPositionException):
        game.get_tile(0, 1)
