import unittest

from invalid_position_exception import InvalidPositionException
from puzzle_game import PuzzleGame
from shufflers_for_testing_puzzles import TestingShufflerPuzzleGame3x3To1X3425786


class GetTileTests(unittest.TestCase):

'''

    Metodo get_tile

    def get_tile(self, line, column):
        if line > 0 and line <= self.board.number_of_lines and \
                column > 0 and column <= self.board.number_of_columns:
            if line == self.line_of_empty_position and \
                column == self.column_of_empty_position:
                return (" ")
            else:
                return self.board.get_tile(line, column)
        else:
            raise InvalidPositionException()

    Grafo:

    [ ] nodo
    { }{ } aresta saindo de indo para
    ( ) label aresta
    [1] Initialize: line, column
    {1 (line > 0 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns)}{2}
    {1 NOT (line > 0 and line <= self.__number_of_lines and column > 0 and column <= self.number_of_columns)}{3}
    {2 (line == self.line_of_empty_position and \ column == self.column_of_empty_position:)}{4}
    {2 NOT (line == self.line_of_empty_position and \ column == self.column_of_empty_position:)}{5}
    [2] Null
    [3] Throw InvalidPositionException
    [4] Return " "
    [5] return self.board.get_tile(line, column)

    All-p-uses:
    Para cada variável x e para cada nodo i tal que x tem
    uma definição global no nodo i, selecione caminhos
    completos que incluam def-clear paths a partir do
    nodo i até todas as arestas (j,k) tal que exista um p-
    use de x na aresta (j,k).
    ➔ Para cada variável, para cada atribuição feita a ela,
    identificar caminhos que passam por esta atribuição e depois por
    todos os seus usos em predicado (sem que tenha sido feito uma
    nova atribuição antes deste uso).

    All-c-uses/Some-p-uses
    Critério idêntico ao all-c-uses, mas se a variável x não
    tem global c-use, o critério é reduzido a some-p-uses.
    ▪ Some-p-uses: Para cada variável x e para cada
    nodo i tal que x tem uma definição global no nodo i,
    selecione caminhos completos que incluam def-clear
    paths a partir do nodo i até algumas arestas (j,k) tal
    que exista um p-use de x na aresta (j,k).
    ➔ Mesma regra do All-c-uses, mas se a variável não tiver uso em
    uma computação, identificar pelo menos um caminho com um uso
    em predicado.

    Objetivo:

    Indique os caminhos selecionados utilizando os seguintes
    critérios de teste de fluxo de dados:
    (i) All-c-uses/Some-p-uses e
    (ii) All-p-uses.
    Considere os dados line e column.

    Caminhos selecionados:

    (i) All-c-uses/Some-p-uses
    - Caminho selecionado:
      [1] -> [2] -> [5]

    (ii) All-p-uses
    - cobrir p-uses nas arestas de decisão que usam line e column (todas no caso):
    - Caminhos completos selecionados:
      [1] -> [3]
      [1] -> [2] -> [4]
      [1] -> [2] -> [5]

'''


