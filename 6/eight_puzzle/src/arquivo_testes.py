import unittest
from unittest.mock import patch

from shufflers_for_testing_puzzles import *
from puzzle_game import PuzzleGame
from puzzle_game_with_mock import PuzzleGameWithPlayer


class TesteMockParte1(unittest.TestCase):
    def test_get_tile_sucesso(self):
        # Testa sucesso do get_tile sem mock
        # 1 2
        # 3 -
        game = PuzzleGame(2)

        TestingShufflerPuzzleGame2x2To1X32().shuffle(game)

        tile = game.get_tile(2, 1)

        self.assertEqual(tile, 3)

    def test_get_tile_vazio(self):
        # Testa get_tile retornando tile vazio sem mock
        # 1 -
        # 3 2
        game = PuzzleGame(2)
        TestingShufflerPuzzleGame2x2To1X32().shuffle(game)

        tile = game.get_tile(1, 2)

        self.assertEqual(tile, " ")

    @patch("puzzle_game.PuzzleGame.get_tile")
    def test_get_tile_sucesso_mock(self, mock_get_tile):
        # Testa sucesso do get_tile com mock
        # 1 2
        # 3 -
        game = PuzzleGame(2)
        mock_get_tile.return_value = 3

        tile = game.get_tile(2, 1)

        self.assertEqual(tile, 3)

    @patch("puzzle_game.PuzzleGame.get_tile")
    def test_get_tile_vazio_mock(self, mock_get_tile):
        # Testa get_tile retornando tile vazio com mock
        # 1 2
        # 3 -
        game = PuzzleGame(2)
        mock_get_tile.return_value = " "

        tile = game.get_tile(1, 2)

        self.assertEqual(tile, " ")


class TesteMockParte2(unittest.TestCase):
    def test_end_of_game_not_finished(self):
        # Testa end of game retornando game not finished
        # 1 2 3
        # 4 5 -
        # 7 8 6
        game = PuzzleGameWithPlayer(3, "Tiago")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Game not finished")

    def test_end_of_game_saved(self):
        # Testa end of game retornando saved, que chama o save_game_to_file
        # 1 2 3
        # 4 5 6
        # 7 8 -
        game = PuzzleGameWithPlayer(3, "Tiago")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.move_tile(6)

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Saved")

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_game_not_finished_mock(self, mock_save_game_to_file):
        # Testa end of game retornando game not finished com mock,
        # o mock n tem efeito pq end_of_game nem chama save_game_to_file
        # 1 2 3
        # 4 5 -
        # 7 8 6
        game = PuzzleGameWithPlayer(3, "Tiago")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        mock_save_game_to_file.return_value = "Saved"

        resultado = game.end_of_the_game()

        self.assertEqual(resultado, "Game not finished")

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_game_saved_mock(self, mock_save_game_to_file):
        # Testa end of game retornando saved, que usa o save_game_to_file
        # mockado (retorna Saved mas n escreve o arquivo)
        # 1 2 3
        # 4 5 8
        # 7 8 -
        game = PuzzleGameWithPlayer(3, "Tiago")
        TestingShufflerPuzzleGame3x3To12345X786().shuffle(game)
        game.move_tile(6)
        mock_save_game_to_file.return_value = "Saved"

        resultado = game.end_of_the_game()

        print(game.board)
        self.assertEqual(resultado, "Saved")

if __name__ == "__main__":
    unittest.main()
