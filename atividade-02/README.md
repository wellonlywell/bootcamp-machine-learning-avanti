# Atividade 02 â€” Python, VisualizaÃ§Ã£o e AnÃ¡lise de Dados

**Curso:** BÃ¡sico em Machine Learning â€” AtlÃ¢ntico Avanti
**Participante:** Well Christina Costa Sousa
**Tipo:** Atividade somativa individual

Esta pasta contÃ©m as respostas da Atividade 02. A atividade mistura exercÃ­cios de Python puro com exemplos simples de anÃ¡lise de dados usando pandas.

## OrganizaÃ§Ã£o dos arquivos

- [questoes_python.py](questoes_python.py): respostas das questÃµes 1 a 5, usando funÃ§Ãµes, listas, `for` e `if`.
- [analise_dados.py](analise_dados.py): exemplos executÃ¡veis das questÃµes 6 a 10 usando pandas.
- [dados.csv](dados.csv): conjunto de dados pequeno criado para os exemplos, pois a atividade nÃ£o forneceu um arquivo CSV.
- [requirements.txt](requirements.txt): dependÃªncia necessÃ¡ria para executar a anÃ¡lise com pandas.

## QuestÃµes da atividade

1. Escrever uma funÃ§Ã£o que receba uma lista de nÃºmeros e retorne outra lista com os nÃºmeros Ã­mpares.
2. Escrever uma funÃ§Ã£o que receba uma lista de nÃºmeros e retorne outra lista com os nÃºmeros primos presentes.
3. Escrever uma funÃ§Ã£o que receba duas listas e retorne outra lista com os elementos que estÃ£o presentes em apenas uma das listas.
4. Encontrar o segundo maior valor diferente do maior em uma lista de nÃºmeros inteiros.
5. Ordenar uma lista de tuplas com nome e idade pelo nome das pessoas em ordem alfabÃ©tica.
6. Identificar e tratar outliers em uma coluna numÃ©rica usando desvio padrÃ£o ou quartis.
7. Concatenar vÃ¡rios DataFrames por linhas ou colunas, mesmo com colunas diferentes.
8. Ler um arquivo CSV em um DataFrame e exibir as primeiras linhas.
9. Selecionar uma coluna especÃ­fica e filtrar linhas com base em uma condiÃ§Ã£o.
10. Lidar com valores ausentes, `NaN`, em um DataFrame.

## SoluÃ§Ãµes em Python

As cinco primeiras questÃµes estÃ£o no arquivo [questoes_python.py](questoes_python.py).

Na questÃ£o 1, a funÃ§Ã£o percorre a lista e guarda apenas os nÃºmeros que nÃ£o sÃ£o divisÃ­veis por 2:

```python
def numeros_impares(numeros):
    impares = []

    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)

    return impares
```

Na questÃ£o 2, foi criada uma funÃ§Ã£o auxiliar chamada `eh_primo(numero)`. Ela verifica se o nÃºmero Ã© menor que 2 e depois testa possÃ­veis divisores:

```python
def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True
```

Depois, `numeros_primos(numeros)` usa essa funÃ§Ã£o para montar uma nova lista apenas com os primos.

Na questÃ£o 3, a funÃ§Ã£o compara duas listas e retorna somente os elementos que aparecem em uma delas, evitando repetir valores no resultado:

```python
if elemento not in lista2 and elemento not in exclusivos:
    exclusivos.append(elemento)
```

Na questÃ£o 4, a funÃ§Ã£o monta uma lista de valores Ãºnicos, ordena em ordem decrescente e retorna o segundo item. Se nÃ£o existirem dois valores diferentes, retorna `None`.

Na questÃ£o 5, a ordenaÃ§Ã£o Ã© feita pelo nome da pessoa, ignorando diferenÃ§as entre letras maiÃºsculas e minÃºsculas:

```python
return sorted(pessoas, key=lambda pessoa: pessoa[0].lower())
```

## SoluÃ§Ãµes com pandas

As questÃµes 6 a 10 estÃ£o no arquivo [analise_dados.py](analise_dados.py).

Na questÃ£o 6, foi criado um DataFrame com a coluna `tempo_atendimento`. Um valor muito alto foi incluÃ­do para representar um possÃ­vel outlier. O script calcula os limites usando quartis e IQR:

```python
q1 = atendimentos["tempo_atendimento"].quantile(0.25)
q3 = atendimentos["tempo_atendimento"].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr
```

Nesse exemplo, o mÃ©todo IQR identifica o valor `120` como possÃ­vel outlier. O programa tambÃ©m mostra limites usando mÃ©dia e trÃªs desvios-padrÃ£o, mas esse segundo mÃ©todo pode nÃ£o identificar o valor `120` nessa amostra. MÃ©todos diferentes podem apresentar resultados diferentes, por isso um valor suspeito nÃ£o deve ser removido automaticamente sem anÃ¡lise do contexto dos dados.

Na questÃ£o 7, dois DataFrames com colunas diferentes sÃ£o concatenados com `pd.concat()`. Quando a concatenaÃ§Ã£o Ã© feita por linhas com `axis=0`, as colunas que nÃ£o existem em um dos DataFrames aparecem com `NaN`. Quando Ã© feita por colunas com `axis=1`, os DataFrames sÃ£o colocados lado a lado.

Na questÃ£o 8, o arquivo [dados.csv](dados.csv) Ã© lido com pandas. O caminho foi montado com `pathlib.Path` e `__file__`, assim o programa funciona mesmo quando executado a partir da raiz do repositÃ³rio:

```python
caminho_csv = Path(__file__).parent / "dados.csv"
dados = pd.read_csv(caminho_csv)
```

Na questÃ£o 9, o script seleciona a coluna `nome` e filtra pessoas com idade maior ou igual a 18:

```python
nomes = dados["nome"]
maiores_de_idade = dados[dados["idade"] >= 18]
```

Na questÃ£o 10, o script mostra valores ausentes usando `isna()` e `isna().sum()`. TambÃ©m demonstra `dropna()` e faz preenchimentos em uma cÃ³pia do DataFrame:

```python
dados_preenchidos = dados.copy()
dados_preenchidos["idade"] = dados_preenchidos["idade"].fillna(mediana_idade)
dados_preenchidos["cidade"] = dados_preenchidos["cidade"].fillna("NÃ£o informado")
```

Neste exemplo, optei por usar o marcador `NÃ£o informado` em vez de preencher a cidade com a moda. Essa escolha preserva a informaÃ§Ã£o de que o dado original estava ausente e evita atribuir automaticamente uma cidade que pode nÃ£o corresponder Ã  realidade.

Valores ausentes tambÃ©m nÃ£o devem ser tratados automaticamente sem analisar o contexto. Ã€s vezes eles indicam erro de coleta; em outras situaÃ§Ãµes, podem carregar uma informaÃ§Ã£o importante.

## Sobre o arquivo CSV

O arquivo [dados.csv](dados.csv) foi criado como conjunto de dados de exemplo, porque a atividade nÃ£o forneceu um CSV pronto.

Ele possui as colunas:

- `nome`
- `idade`
- `cidade`
- `tempo_atendimento`

O arquivo inclui pessoas maiores e menores de idade, valores ausentes em `idade` e `cidade`, e um valor alto em `tempo_atendimento` para servir como possÃ­vel outlier.

## Como instalar as dependÃªncias

Execute o comando abaixo a partir da raiz do repositÃ³rio:

Ã‰ necessÃ¡rio ter Python 3 instalado para executar os comandos.

```bash
python -m pip install -r atividade-02/requirements.txt
```

## Como executar os programas

Para executar as questÃµes 1 a 5:

```bash
python atividade-02/questoes_python.py
```

Para executar as questÃµes 6 a 10:

```bash
python atividade-02/analise_dados.py
```
