# RPD: Plano para LLM Executar o Exercício 5

## Objetivo

Executar o exercício de Testes de Mutação com `mutmut` no diretório `5/`, usando como base o código e os testes herdados da Aula 4, identificar 5 mutantes sobreviventes, explicar por que sobreviveram, escrever novos testes para matá-los e atualizar os artefatos pedidos no exercício.

## Contexto do Diretório

Arquivos de referência já disponíveis:

- `5/relatorio.md`: resumo das entregas exigidas
- `5/mutantes_sobreviventes.md`: arquivo a ser preenchido com a análise dos mutantes
- `5/pyproject.toml`: configuração do `mutmut`
- `5/enunciado/enunciado-exercicio-5.pdf`: enunciado original
- `5/enunciado/slides-aula-5-mutacao.pdf`: material teórico
- `5_/5/`: solução de colega, usar apenas como referência estrutural, nunca como cópia

Observação importante:

- Atualmente `5/` não contém `conteudo/` nem `tests/`.
- Antes de rodar o exercício, é necessário trazer para `5/` o código e os testes corretos da sua Aula 4.

## Estado Final Esperado

Ao final, o diretório `5/` deve conter:

- o código-fonte do exercício
- os testes herdados da Aula 4
- novos testes criados para matar mutantes sobreviventes
- `mutantes_sobreviventes.md` preenchido
- `relatorio.md` preenchido com os comandos e evidências solicitados

## Restrições

- Não copiar testes da pasta `5_/5/`; usar apenas como inspiração
- Não alterar o comportamento do sistema sem necessidade; a prioridade é matar mutantes com novos testes
- Só alterar código de produção se ficar claro que o comportamento original está ambíguo ou incorreto
- Os novos testes devem ser identificáveis no repositório e distinguíveis dos testes herdados

## Passo a Passo

### 1. Preparar a base do exercício

Objetivo:

- Garantir que `5/` tenha a estrutura mínima executável

Ações:

1. Copiar para `5/` os diretórios e arquivos da sua solução da Aula 4.
2. Confirmar que existem pelo menos:
   - `5/conteudo/`
   - `5/tests/`
3. Confirmar que o arquivo alvo do `mutmut` existe:
   - `5/conteudo/puzzle_game.py`

Critério de sucesso:

- O projeto dentro de `5/` executa os testes sem erros de importação por arquivos ausentes.

### 2. Executar os testes existentes

Objetivo:

- Registrar o comportamento inicial da suíte

Ações:

1. Entrar no diretório `5/`.
2. Rodar a suíte atual com o executor compatível com o projeto.

Comandos prováveis:

```bash
cd 5
python -m unittest
```

Se o projeto usar `pytest`:

```bash
cd 5
pytest
```

Registrar no `relatorio.md`:

- comando executado
- quantidade de testes executados
- resultado final da execução

Critério de sucesso:

- Todos os testes herdados passam antes da mutação.

### 3. Validar a configuração do `mutmut`

Objetivo:

- Confirmar que a ferramenta conseguirá mutar o arquivo correto

Ações:

1. Ler `5/pyproject.toml`.
2. Confirmar que o alvo é `conteudo/puzzle_game.py`.
3. Se a versão instalada do `mutmut` não aceitar a chave atual, ajustar a configuração de acordo com a versão em uso.

Observação:

- O arquivo atual usa:

```toml
[tool.mutmut]
paths_to_mutate = ["conteudo/puzzle_game.py"]
```

- Algumas versões usam outra chave, como `source_paths`.
- Se houver erro de configuração, descobrir a sintaxe correta pela ajuda local da ferramenta antes de continuar.

Critério de sucesso:

- `mutmut` reconhece o projeto e inicia a análise.

### 4. Executar os testes de mutação

Objetivo:

- Gerar a lista de mutantes mortos e sobreviventes

Ações:

1. Rodar a ferramenta de mutação.
2. Inspecionar os resultados.

Comandos prováveis:

```bash
cd 5
mutmut run
```

Depois:

```bash
mutmut browse
```

ou, dependendo da versão:

```bash
mutmut show
```

Registrar no `relatorio.md`:

- comando executado
- resumo dos resultados
- quantidade de sobreviventes

Critério de sucesso:

- Existe uma lista de mutantes sobreviventes identificáveis por nome e diff.

### 5. Selecionar 5 mutantes sobreviventes

Objetivo:

- Escolher 5 mutantes relevantes e justificáveis para análise

Critérios de seleção:

- Preferir mutantes em trechos com regra de negócio clara
- Preferir mutantes que possam ser mortos com testes específicos
- Priorizar mutações em:
  - operadores lógicos (`and`, `or`)
  - operadores relacionais (`>`, `>=`, `<`, `<=`)
  - verificações de fronteira
  - decisões sobre retorno ou exceção

Evitar, se possível:

- mutantes equivalentes
- mutantes cujo comportamento não seja observável pelos testes

Critério de sucesso:

- Há 5 mutantes sobreviventes escolhidos com diff claro e hipótese plausível do motivo de sobrevivência.

### 6. Analisar cada mutante sobrevivente

Objetivo:

- Descobrir qual cenário de teste está faltando

Para cada mutante, seguir este procedimento:

1. Comparar código original e código mutado.
2. Descrever exatamente o que mudou.
3. Perguntar:
   - Que comportamento incorreto o mutante permite?
   - Em que entrada o original e o mutado divergem?
   - Os testes atuais cobrem a linha, mas sem assert suficiente?
   - Falta um caso de borda?
   - Falta validar exceção?
4. Definir o menor caso de teste que diferencia o original do mutado.

Padrões de análise esperados para `puzzle_game.py`:

- linha válida com coluna inválida
- coluna válida com linha inválida
- linha `0`
- coluna `0`
- última linha válida
- última coluna válida
- posição da célula vazia
- mesma linha da célula vazia com coluna diferente
- mesma coluna da célula vazia com linha diferente

Exemplos típicos de sobrevivência:

- `and` trocado por `or`: falta teste com apenas uma dimensão inválida
- `>` trocado por `>=`: falta teste com zero
- `<=` trocado por `<`: falta teste no limite superior
- comparação com posição vazia alterada: falta teste distinguindo mesma linha de mesma coluna

Critério de sucesso:

- Cada mutante escolhido tem uma explicação objetiva e um caso de teste planejado para matá-lo.

### 7. Preencher `mutantes_sobreviventes.md`

Objetivo:

- Registrar formalmente a análise pedida no exercício

Para cada um dos 5 mutantes, preencher neste formato:

```md
### Mutante N

Explicação objetiva da mutação e do motivo de sobrevivência.
Descrever também qual cenário de teste faltava.

```py
Código antes
```

```py
Código depois
```
```

Conteúdo mínimo esperado por mutante:

- o que mudou no código
- por que os testes atuais não detectaram a mutação
- qual novo teste deve matar esse mutante

Critério de sucesso:

- O arquivo contém 5 mutantes bem descritos, sem explicações genéricas.

### 8. Implementar novos testes

Objetivo:

- Escrever testes que matem especificamente os 5 mutantes escolhidos

Diretrizes:

- Criar testes focados no comportamento observável
- Nomear os testes de forma clara
- Se possível, concentrar os novos casos em um novo arquivo de teste ou em uma nova classe de testes
- Garantir que fique evidente quais testes foram adicionados nesta atividade

Heurística principal:

- Não escrever “mais testes” genericamente
- Escrever um teste por lacuna semântica descoberta

Exemplos de intenção de teste:

- verificar exceção quando `line == 0`
- verificar exceção quando `column == 0`
- verificar exceção quando uma coordenada é válida e a outra não
- verificar retorno correto no limite superior do tabuleiro
- verificar que apenas a posição exata da célula vazia retorna `" "`

Critério de sucesso:

- Os novos testes passam no código original e falhariam no mutante correspondente.

### 9. Reexecutar a suíte normal

Objetivo:

- Garantir que os novos testes não quebraram o comportamento correto

Ações:

1. Rodar novamente a suíte completa.
2. Registrar a execução no `relatorio.md`.

Critério de sucesso:

- Todos os testes passam.

### 10. Reexecutar o `mutmut`

Objetivo:

- Verificar se os 5 mutantes escolhidos foram mortos

Ações:

1. Rodar novamente o `mutmut`.
2. Conferir o status dos mutantes antes selecionados.
3. Se algum ainda sobreviver, refinar o teste correspondente.

Critério de sucesso:

- Os 5 mutantes analisados deixam de aparecer como `survived`.

### 11. Finalizar `relatorio.md`

Objetivo:

- Entregar as evidências na ordem exigida

Estrutura mínima esperada no `relatorio.md`:

1. Execução dos testes existentes do projeto
2. Execução da ferramenta `mutmut`
3. Identificação e explicação de 5 mutantes vivos
4. Descrição dos novos testes escritos
5. Nova execução mostrando os mutantes mortos

Em cada seção incluir:

- o comando executado
- um resumo fiel do resultado
- observações relevantes quando necessário

## Regras de Decisão Durante a Execução

Se um mutante sobreviver, decidir assim:

- Se o mutante alterou comportamento observável e existe entrada que diferencia original e mutado:
  - escrever ou fortalecer teste
- Se o mutante parece equivalente:
  - justificar e escolher outro mutante, se o exercício permitir
- Se os testes cobrem a linha, mas não validam a saída correta:
  - fortalecer asserções
- Se o comportamento original estiver ambíguo:
  - consultar enunciado e comportamento esperado antes de alterar código

## Sinais de Boa Solução

- Os novos testes atacam fronteiras e combinações inválidas
- As explicações dos mutantes conectam mutação, lacuna de teste e correção
- O relatório deixa claro o antes e depois
- A solução não depende de copiar a resposta do colega

## Entregáveis Finais

- `5/mutantes_sobreviventes.md` preenchido
- `5/relatorio.md` preenchido
- novos testes adicionados ao projeto em `5/`
- evidência de que os 5 mutantes escolhidos foram mortos
