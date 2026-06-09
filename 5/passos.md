### Execução dos testes existentes do projeto

Rodar os testes antigos:

```bash
python -m pytest tests/test_old.py -v
```

### Cenário inicial:

```bash
mv tests/test_get_tile_mutant_killers.py ./test_get_tile_mutant_killers.py.bak
rm -rf mutants
mutmut run
mutmut results
```

Resultado:

```text
322 mutantes testados
🎉 155 killed  🫥 142 no tests  🙁 25 survived
```

Mutantes sobreviventes do `conteudo/puzzle_game.py` get_tile()
```bash
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_1: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_2: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_3: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_4: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_6: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_7: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_8: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_11: survived
    conteudo.puzzle_game.xǁPuzzleGameǁget_tile__mutmut_13: survived
```

Mutantes selecionados:

- `get_tile_4`
- `get_tile_6`
- `get_tile_7`
- `get_tile_11`
- `get_tile_13`

Novos testes escritos

Arquivo criado:

- `tests/test_get_tile_mutant_killers.py`

Testes adicionados:

- `test_get_tile_line_zero_raises_invalid_position`
- `test_get_tile_last_valid_line_returns_tile`
- `test_get_tile_line_above_board_raises_invalid_position`
- `test_get_tile_column_zero_raises_invalid_position`
- `test_get_tile_first_valid_column_returns_tile`
- `test_get_tile_at_empty_position_returns_space`
- `test_get_tile_same_column_different_line_returns_tile_not_space`
- `test_get_tile_same_line_different_column_returns_tile_not_space`

### Nova execução mostrando os mutantes mortos

Comandos:

```bash
mv ./test_get_tile_mutant_killers.py.bak tests/test_get_tile_mutant_killers.py
python -m pytest tests/test_old.py tests/test_get_tile_mutant_killers.py -v
```

Resultado:

```text
collected 13 items

tests/test_old.py::ClasseTestes::test_path_0_1_2_3_4_returns_true PASSED
tests/test_old.py::ClasseTestes::test_path_0_1_2_5_returns_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_4_second_condition_true PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_5_second_condition_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_5_first_condition_false PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_last_valid_line_returns_tile PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_line_above_board_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_line_zero_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryColumn::test_get_tile_column_zero_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryColumn::test_get_tile_first_valid_column_returns_tile PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_at_empty_position_returns_space PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_same_column_different_line_returns_tile_not_space PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_same_line_different_column_returns_tile_not_space PASSED

13 passed in 0.03s
```

### Nova execução do mutmut

Comandos:

```bash
rm -rf mutants
mutmut run
mutmut results
```

Resultado:

```text
322 mutantes testados
🎉 174 killed  🫥 142 no tests  🙁 6 survived
```

Os 5 mutantes analisados foram mortos.
