import unittest
from unittest.mock import patch

from shufflers_for_testing_puzzles import *
from puzzle_game import PuzzleGame
from puzzle_game_with_mock import PuzzleGameWithPlayer


class TesteMockParte1(unittest.TestCase):
    def test_get_tile_sucesso(self):
        game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(game)

        tile = game.get_tile(2, 1)

        self.assertEqual(tile, 3)

    def test_get_tile_vazio(self):
        game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(game)

        tile = game.get_tile(1, 2)

        self.assertEqual(tile, " ")

    @patch("puzzle_game.PuzzleGame.get_tile")
    def test_get_tile_sucesso_mock(self, mock_get_tile):
        game = PuzzleGame(2)
        mock_get_tile.return_value = 3

        tile = game.get_tile(2, 1)

        self.assertEqual(tile, 3)

    @patch("puzzle_game.PuzzleGame.get_tile")
    def test_get_tile_vazio_mock(self, mock_get_tile):
        game = PuzzleGame(2)
        mock_get_tile.return_value = " "

        tile = game.get_tile(1, 2)

        self.assertEqual(tile, " ")


class TesteMockParte2(unittest.TestCase):
    def test_end_of_game_not_finished(self):
        game = PuzzleGameWithPlayer(3, "William")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Game not finished")

    def test_end_of_game_saved(self):
        game = PuzzleGameWithPlayer(3, "William")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.move_tile(6)

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Saved")

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_game_not_finished_mock(self, mock_save_game_to_file):
        game = PuzzleGameWithPlayer(3, "William")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        mock_save_game_to_file.return_value = "Saved"

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Game not finished")

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_game_saved_mock(self, mock_save_game_to_file):
        game = PuzzleGameWithPlayer(3, "William")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.move_tile(6)
        mock_save_game_to_file.return_value = "Saved"

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Saved")

if __name__ == "__main__":
    unittest.main()
