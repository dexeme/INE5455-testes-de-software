import unittest

from conteudo.puzzle_game import PuzzleGame, InvalidPositionException
from tests.shufflers_for_testing_puzzles import (
    TestingShufflerPuzzleGame3x3To1X3425786,
    TestingShufflerPuzzleGame3x3To12345X786,
)


class TestGetTileBoundaryLine(unittest.TestCase):
    """Kills mutmut_4 (line > 0 → line >= 0) and mutmut_6 (line <= N → line < N)."""

    def test_get_tile_line_zero_raises_invalid_position(self):
        # Mutante 4: line >= 0 deixaria line=0 passar sem exceção.
        game = PuzzleGame(3)
        with self.assertRaises(InvalidPositionException):
            game.get_tile(0, 1)

    def test_get_tile_last_valid_line_returns_tile(self):
        # Mutante 6: line < N rejeitaria a última linha válida (line == N).
        # No 3x3 inicial o vazio é em (3,3), logo get_tile(3,1) deve retornar 7.
        game = PuzzleGame(3)
        result = game.get_tile(3, 1)
        self.assertEqual(7, result)
    #
    # def test_get_tile_line_above_board_raises_invalid_position(self):
    #     game = PuzzleGame(3)
    #     with self.assertRaises(InvalidPositionException):
    #         game.get_tile(4, 1)


class TestGetTileBoundaryColumn(unittest.TestCase):
    """Kills mutmut_7 (column > 0 → column >= 0)."""

    def test_get_tile_column_zero_raises_invalid_position(self):
        # Mutante 7: column >= 0 deixaria column=0 passar sem exceção.
        game = PuzzleGame(3)
        with self.assertRaises(InvalidPositionException):
            game.get_tile(1, 0)
    #
    # def test_get_tile_first_valid_column_returns_tile(self):
    #     # Confirma que column=1 é válido (garante que o limite inferior correto é > 0).
    #     game = PuzzleGame(3)
    #     result = game.get_tile(1, 1)
    #     self.assertEqual(1, result)


class TestGetTileEmptyPosition(unittest.TestCase):
    """Kills mutmut_11 (line == → line !=) and mutmut_13 (return " " → return "XX XX")."""

    def setUp(self):
        # Após shuffle: vazio em (1,2)
        # 1  -  3
        # 4  2  5
        # 7  8  6
        self.game = PuzzleGame(3)
        self.game.shuffle(TestingShufflerPuzzleGame3x3To1X3425786())
        self.empty_line = self.game.line_of_empty_position    # 1
        self.empty_col = self.game.column_of_empty_position   # 2

    def test_get_tile_at_empty_position_returns_space(self):
        # Mutante 13: retornaria "XX XX" em vez de " ".
        result = self.game.get_tile(self.empty_line, self.empty_col)
        self.assertEqual(" ", result)

    # def test_get_tile_same_column_different_line_returns_tile_not_space(self):
    #     # Mutante 11: line != empty_line faria a posição (2,2) retornar " "
    #     # porque satisfaz (2 != 1) and (2 == 2).
    #     # Na posição (2,2) está o tile 2.
    #     result = self.game.get_tile(2, self.empty_col)
    #     self.assertNotEqual(" ", result)
    #     self.assertEqual(2, result)
    #
