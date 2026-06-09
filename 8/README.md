# Exercício 8 - Selenium

## Arquivos

- `google_tiago_search.side`: teste exportado do Selenium IDE para procurar `Tiago` no Google.
- `test_duckduckgo_calculator.py`: testes Selenium WebDriver em Python para a calculadora do DuckDuckGo.
- `requirements.txt`: dependência Python necessária.

## Como executar os testes WebDriver

A partir do diretório `8`:

```bash
../.venv/bin/python -m unittest test_duckduckgo_calculator.py
```

Para abrir o navegador visualmente durante a apresentação:

```bash
HEADLESS=0 ../.venv/bin/python -m unittest test_duckduckgo_calculator.py
```

Se estiver fora da virtualenv do projeto, instale antes:

```bash
python -m pip install -r requirements.txt
```

Por padrão o teste usa `/usr/bin/chromium` e `/usr/bin/chromedriver`. Para trocar:

```bash
CHROME_BINARY=/caminho/chromium CHROMEDRIVER=/caminho/chromedriver python -m unittest test_duckduckgo_calculator.py
```
