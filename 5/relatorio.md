```bash
python -m pytest tests/ -v
```

Resultado:

```
collected 5 items

tests/test_old.py::ClasseTestes::test_path_0_1_2_3_4_returns_true PASSED
tests/test_old.py::ClasseTestes::test_path_0_1_2_5_returns_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_4_second_condition_true PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_5_second_condition_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_5_first_condition_false PASSED

5 passed in 0.02s
```

```toml
also_copy = ["conteudo", "conftest.py"]
```

```bash
mutmut run
```

Resultado:

```
1 files mutated, 0 ignored, 0 unmodified
322 mutantes gerados e testados
🎉 155 killed  🫥 142 no tests  🙁 25 survived
```

Os 25 sobreviventes em funções cobertas por testes estavam distribuídos entre
`get_tile` (9 sobreviventes), `move_tile_from_a_position_to_the_empty_position` (5),
`__generate_list_of_tiles__` (2), `__put_tiles_in_the_board__` (6), e
`__put_tiles_in_dic_positions__` (1). Os 142 sem testes eram das funções
`__move_empty_cell_to_*`, `move_empty_tile` e `__print_board_of_puzzle_game__`.

---

## 3. Identificação e explicação dos 5 mutantes vivos

Os 5 mutantes selecionados estão todos no método `get_tile`. Ver análise detalhada
em `mutantes_sobreviventes.md`.

Causa raiz comum: a classe `GetTileTests` está aninhada dentro de
`TestMoveTileBranchCoverage` no arquivo `tests/test_old.py`. O pytest não coleta
classes `TestCase` aninhadas, portanto nenhum teste de `get_tile` era executado.

Mutantes escolhidos:

| ID           | Mutação                                            | Tipo              |
|--------------|----------------------------------------------------|-------------------|
| get_tile_4   | `line > 0` → `line >= 0`                          | fronteira inferior |
| get_tile_6   | `line <= N` → `line < N`                          | fronteira superior |
| get_tile_7   | `column > 0` → `column >= 0`                      | fronteira inferior |
| get_tile_11  | `line == empty_line` → `line != empty_line`        | inversão lógica   |
| get_tile_13  | `return (" ")` → `return ("XX XX")`               | valor errado      |

---

## 4. Novos testes escritos

Arquivo criado: `tests/test_get_tile_mutant_killers.py`

Classes e testes adicionados:

- **TestGetTileBoundaryLine**
  - `test_get_tile_line_zero_raises_invalid_position` — mata mutmut_4
  - `test_get_tile_last_valid_line_returns_tile` — mata mutmut_6
  - `test_get_tile_line_above_board_raises_invalid_position` — reforço geral
- **TestGetTileBoundaryColumn**
  - `test_get_tile_column_zero_raises_invalid_position` — mata mutmut_7
  - `test_get_tile_first_valid_column_returns_tile` — reforço geral
- **TestGetTileEmptyPosition**
  - `test_get_tile_at_empty_position_returns_space` — mata mutmut_13
  - `test_get_tile_same_column_different_line_returns_tile_not_space` — mata mutmut_11
  - `test_get_tile_same_line_different_column_returns_tile_not_space` — reforço geral

Todos os testes foram escritos como classes de nível superior, não aninhadas.

---

## 5. Reexecução mostrando os 5 mutantes mortos

### 5a. Suíte de testes com novos testes

Comando:

```bash
python -m pytest tests/ -v
```

Resultado:

```
collected 13 items

tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_last_valid_line_returns_tile PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_line_above_board_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryLine::test_get_tile_line_zero_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryColumn::test_get_tile_column_zero_raises_invalid_position PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileBoundaryColumn::test_get_tile_first_valid_column_returns_tile PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_at_empty_position_returns_space PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_same_column_different_line_returns_tile_not_space PASSED
tests/test_get_tile_mutant_killers.py::TestGetTileEmptyPosition::test_get_tile_same_line_different_column_returns_tile_not_space PASSED
tests/test_old.py::ClasseTestes::test_path_0_1_2_3_4_returns_true PASSED
tests/test_old.py::ClasseTestes::test_path_0_1_2_5_returns_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_4_second_condition_true PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_3_5_second_condition_false PASSED
tests/test_old.py::TestMoveTileBranchCoverage::test_path_0_1_2_5_first_condition_false PASSED

13 passed in 0.01s
```

### 5b. Segunda execução do mutmut

Comando:

```bash
mutmut run
```

Resultado final:

```
322 mutantes testados
🎉 174 killed  🫥 142 no tests  🙁 6 survived
```

Os 6 sobreviventes restantes são de métodos diferentes dos 5 selecionados.
Nenhum dos 5 mutantes analisados (`get_tile_4`, `get_tile_6`, `get_tile_7`,
`get_tile_11`, `get_tile_13`) aparece na lista de sobreviventes — todos foram mortos.

Sobreviventes remanescentes (fora do escopo desta análise):

```
__generate_list_of_tiles____mutmut_3: survived
__generate_list_of_tiles____mutmut_12: survived
__put_tiles_in_dic_positions____mutmut_20: survived
move_tile_from_a_position_to_the_empty_position__mutmut_1: survived
move_tile_from_a_position_to_the_empty_position__mutmut_33: survived
move_tile_from_a_position_to_the_empty_position__mutmut_34: survived
```
