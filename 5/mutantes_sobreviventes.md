# Mutantes Sobreviventes

```
line > 0 → line >= 0
line <= N → line < N
column > 0 → column >= 0
line == empty_line → line != empty_line
return (" ") → return ("XX XX")
```

### Mutante 1

Trocou `line > 0` por `line >= 0` na verificação de posição válida em `get_tile`.
Com a mutação, `get_tile(0, col)` não levantava `InvalidPositionException`; passava para o
`if` interno e consultava `board.get_tile(0, col)` (que retorna `None` por indexação inválida).
Nenhum teste chamava `get_tile` com `line=0` diretamente.

```py
# Original
if line > 0 and line <= self.board.number_of_lines and \
        column > 0 and column <= self.board.number_of_columns:
```

```py
# Mutado (mutmut_4)
if line >= 0 and line <= self.board.number_of_lines and \
        column > 0 and column <= self.board.number_of_columns:
```

**Teste que mata:** `test_get_tile_line_zero_raises_invalid_position` — chama `get_tile(0, 1)` e
verifica que `InvalidPositionException` é levantada.

---

### Mutante 2

Trocou `line <= self.board.number_of_lines` por `line < self.board.number_of_lines`.
Com a mutação, a última linha válida (ex.: linha 3 em um tabuleiro 3×3) era rejeitada como fora
do tabuleiro, levantando `InvalidPositionException` ao invés de retornar o tile.
Nenhum teste verificava `get_tile` na linha máxima válida.

```py
# Original
if line > 0 and line <= self.board.number_of_lines and \
        column > 0 and column <= self.board.number_of_columns:
```

```py
# Mutado (mutmut_6)
if line > 0 and line < self.board.number_of_lines and \
        column > 0 and column <= self.board.number_of_columns:
```

**Teste que mata:** `test_get_tile_last_valid_line_returns_tile` — chama `get_tile(3, 1)` em um
jogo 3×3 e verifica que retorna `7` (e não levanta exceção).

---

### Mutante 3

Trocou `column > 0` por `column >= 0` na verificação de posição válida em `get_tile`.
Com a mutação, `get_tile(line, 0)` não levantava `InvalidPositionException`.
Nenhum teste chamava `get_tile` com `column=0` diretamente.

```py
# Original
if line > 0 and line <= self.board.number_of_lines and \
        column > 0 and column <= self.board.number_of_columns:
```

```py
# Mutado (mutmut_7)
if line > 0 and line <= self.board.number_of_lines and \
        column >= 0 and column <= self.board.number_of_columns:
```

**Teste que mata:** `test_get_tile_column_zero_raises_invalid_position` — chama `get_tile(1, 0)`
e verifica que `InvalidPositionException` é levantada.

---

### Mutante 4

Trocou `line == self.line_of_empty_position` por `line != self.line_of_empty_position` na
verificação da célula vazia. Com a mutação, a detecção da posição vazia ficou invertida: uma
posição com *linha diferente* da vazia e *mesma coluna* retornava `" "`, enquanto a posição
vazia real retornava o tile do board (que é `None`). A classe `GetTileTests` existia mas não era
descoberta, logo nenhum teste exercitava esse comportamento.

```py
# Original
if line == self.line_of_empty_position and \
        column == self.column_of_empty_position:
    return (" ")
```

```py
# Mutado (mutmut_11)
if line != self.line_of_empty_position and \
        column == self.column_of_empty_position:
    return (" ")
```

**Testes que matam:**
- `test_get_tile_at_empty_position_returns_space` — verifica que a posição vazia retorna `" "`.
- `test_get_tile_same_column_different_line_returns_tile_not_space` — verifica que uma célula
  com mesma coluna mas linha diferente retorna o tile real (e não `" "`).

---

### Mutante 5

Trocou `return (" ")` por `return ("XX XX")` na ramificação que identifica a célula vazia.
Com a mutação, `get_tile` retornava a string `"XX XX"` ao invés de `" "` para a posição vazia.
O teste `test_path_1_2_4_returns_empty_string_for_empty_position` verificava exatamente isso,
mas como estava em uma classe aninhada (`GetTileTests` dentro de `TestMoveTileBranchCoverage`),
nunca era coletado pelo pytest.

```py
# Original
return (" ")
```

```py
# Mutado (mutmut_13)
return ("XX XX")
```

**Teste que mata:** `test_get_tile_at_empty_position_returns_space` — verifica
`assertEqual(" ", game.get_tile(...))` com a posição exata da célula vazia.
