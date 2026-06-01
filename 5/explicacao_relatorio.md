# Explicação do Exercício 5

Este arquivo é para estudo e entendimento. Ele explica o que aconteceu no exercício, por que o
resultado "antes" e "depois" pode parecer igual quando o procedimento é feito de forma errada, e
qual foi a lógica usada para matar os 5 mutantes escolhidos.

## 1. Por que apagar `mutants/` não basta

A pasta `mutants/` guarda artefatos da execução do `mutmut`, mas ela não controla quais testes
existem no projeto. O `mutmut` sempre executa os testes que estão atualmente dentro do diretório
configurado em `tests_dir`.

No projeto, a configuração é:

```toml
[tool.mutmut]
paths_to_mutate = ["conteudo/puzzle_game.py"]
tests_dir = ["tests/"]
```

Então, se o arquivo `tests/test_get_tile_mutant_killers.py` continuar dentro de `tests/`, o
`mutmut` sempre vai usar a suíte nova, mesmo que a pasta `mutants/` seja apagada.

Conclusão:

- apagar `mutants/` limpa o resultado anterior
- mas não volta o projeto ao estado "antes"
- para reproduzir o "antes", é necessário executar o `mutmut` sem o arquivo de testes novos

## 2. Como demonstrar corretamente o antes e o depois

O projeto já preserva bem os dois cenários:

- `tests/test_old.py` representa a suíte antiga
- `tests/test_get_tile_mutant_killers.py` representa os novos testes adicionados

Então:

- o "antes" é rodar apenas `tests/test_old.py`
- o "depois" é rodar `tests/test_old.py` junto com `tests/test_get_tile_mutant_killers.py`

Para o `pytest`, isso é simples porque dá para escolher os arquivos explicitamente.

Para o `mutmut`, como ele lê toda a pasta `tests/`, o jeito mais direto de demonstrar é mover
temporariamente o arquivo novo para fora de `tests/`, rodar o `mutmut`, e depois restaurar o
arquivo e rodar de novo.

## 3. O que causava os mutantes sobreviventes em `get_tile`

Os 5 mutantes escolhidos estavam todos no método `get_tile` de
`conteudo/puzzle_game.py`.

A causa raiz comum foi esta:

- existiam testes de `get_tile` no arquivo antigo
- mas eles estavam dentro de uma classe aninhada
- o `pytest` não coletava essa classe
- na prática, os testes de `get_tile` não rodavam

Isso explica por que mutantes de fronteira e de lógica sobreviveram mesmo existindo testes
aparentemente relacionados no arquivo antigo.

## 4. Quais mutantes foram escolhidos

Os 5 mutantes escolhidos foram:

1. `line > 0` → `line >= 0`
2. `line <= N` → `line < N`
3. `column > 0` → `column >= 0`
4. `line == empty_line` → `line != empty_line`
5. `return (" ")` → `return ("XX XX")`

Eles foram escolhidos porque:

- são mutações fáceis de explicar
- representam falhas reais de fronteira e lógica
- podem ser mortos com testes observáveis e objetivos

## 5. Como os novos testes matam os mutantes

Os novos testes foram colocados em `tests/test_get_tile_mutant_killers.py`.

Lógica de cada grupo:

- testes de fronteira inferior de linha:
  - verificam que `line = 0` deve levantar `InvalidPositionException`
- testes de fronteira superior de linha:
  - verificam que a última linha válida ainda deve ser aceita
- testes de fronteira inferior de coluna:
  - verificam que `column = 0` deve levantar `InvalidPositionException`
- testes da posição vazia:
  - verificam que só a posição exata da célula vazia retorna `" "`
  - verificam que posições parecidas, mas não iguais, retornam o tile real

Isso força diferença observável entre programa original e programa mutado.

## 6. Como interpretar o resultado final

Resultado "antes":

- 5 testes executados
- 25 mutantes sobreviventes

Resultado "depois":

- 13 testes executados
- 6 mutantes sobreviventes

Isso não significa que todos os mutantes do sistema foram mortos. Significa que os 5 mutantes
selecionados para análise deixaram de sobreviver após a inclusão dos novos testes.

Os 6 sobreviventes restantes pertencem a outros métodos e ficaram fora do escopo desta entrega.

## 7. O que dizer ao professor, em termos simples

Resumo curto:

- a suíte antiga não exercitava de fato `get_tile` porque os testes estavam em classe aninhada
- por isso vários mutantes desse método sobreviveram
- foram escolhidos 5 mutantes de `get_tile`
- foram adicionados testes específicos de fronteira e posição da célula vazia
- depois disso, os 5 mutantes escolhidos morreram
- ainda restaram outros mutantes em métodos diferentes, fora do escopo da análise
