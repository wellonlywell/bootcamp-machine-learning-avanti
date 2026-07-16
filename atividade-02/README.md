# Atividade 02 — Python, Visualização e Análise de Dados

**Curso:** Básico em Machine Learning — Atlântico Avanti
**Participante:** Well Christina Costa Sousa
**Tipo:** Atividade somativa individual

Esta pasta contém as respostas da Atividade 02. A atividade mistura exercícios de Python puro com exemplos simples de análise de dados usando pandas.

## Organização dos arquivos

- [questoes_python.py](questoes_python.py): respostas das questões 1 a 5, usando funções, listas, `for` e `if`.
- [analise_dados.py](analise_dados.py): exemplos executáveis das questões 6 a 10 usando pandas.
- [dados.csv](dados.csv): conjunto de dados pequeno criado para os exemplos, pois a atividade não forneceu um arquivo CSV.
- [requirements.txt](requirements.txt): dependência necessária para executar a análise com pandas.

## Questões da atividade

1. Escrever uma função que receba uma lista de números e retorne outra lista com os números ímpares.
2. Escrever uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
3. Escrever uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
4. Encontrar o segundo maior valor diferente do maior em uma lista de números inteiros.
5. Ordenar uma lista de tuplas com nome e idade pelo nome das pessoas em ordem alfabética.
6. Identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis.
7. Concatenar vários DataFrames por linhas ou colunas, mesmo com colunas diferentes.
8. Ler um arquivo CSV em um DataFrame e exibir as primeiras linhas.
9. Selecionar uma coluna específica e filtrar linhas com base em uma condição.
10. Lidar com valores ausentes, `NaN`, em um DataFrame.

## Soluções em Python

As cinco primeiras questões estão no arquivo [questoes_python.py](questoes_python.py).

Na questão 1, a função percorre a lista e guarda apenas os números que não são divisíveis por 2:

```python
def numeros_impares(numeros):
    impares = []

    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)

    return impares
```

Na questão 2, foi criada uma função auxiliar chamada `eh_primo(numero)`. Ela verifica se o número é menor que 2 e depois testa possíveis divisores:

```python
def eh_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True
```

Depois, `numeros_primos(numeros)` usa essa função para montar uma nova lista apenas com os primos.

Na questão 3, a função compara duas listas e retorna somente os elementos que aparecem em uma delas, evitando repetir valores no resultado:

```python
if elemento not in lista2 and elemento not in exclusivos:
    exclusivos.append(elemento)
```

Na questão 4, a função monta uma lista de valores únicos, ordena em ordem decrescente e retorna o segundo item. Se não existirem dois valores diferentes, retorna `None`.

Na questão 5, a ordenação é feita pelo nome da pessoa, ignorando diferenças entre letras maiúsculas e minúsculas:

```python
return sorted(pessoas, key=lambda pessoa: pessoa[0].lower())
```

## Soluções com pandas

As questões 6 a 10 estão no arquivo [analise_dados.py](analise_dados.py).

Na questão 6, foi criado um DataFrame com a coluna `tempo_atendimento`. Um valor muito alto foi incluído para representar um possível outlier. O script calcula os limites usando quartis e IQR:

```python
q1 = atendimentos["tempo_atendimento"].quantile(0.25)
q3 = atendimentos["tempo_atendimento"].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr
```

Nesse exemplo, o método IQR identifica o valor `120` como possível outlier. O programa também mostra limites usando média e três desvios-padrão, mas esse segundo método pode não identificar o valor `120` nessa amostra. Métodos diferentes podem apresentar resultados diferentes, por isso um valor suspeito não deve ser removido automaticamente sem análise do contexto dos dados.

Na questão 7, dois DataFrames com colunas diferentes são concatenados com `pd.concat()`. Quando a concatenação é feita por linhas com `axis=0`, as colunas que não existem em um dos DataFrames aparecem com `NaN`. Quando é feita por colunas com `axis=1`, os DataFrames são colocados lado a lado.

Na questão 8, o arquivo [dados.csv](dados.csv) é lido com pandas. O caminho foi montado com `pathlib.Path` e `__file__`, assim o programa funciona mesmo quando executado a partir da raiz do repositório:

```python
caminho_csv = Path(__file__).parent / "dados.csv"
dados = pd.read_csv(caminho_csv)
```

Na questão 9, o script seleciona a coluna `nome` e filtra pessoas com idade maior ou igual a 18:

```python
nomes = dados["nome"]
maiores_de_idade = dados[dados["idade"] >= 18]
```

Na questão 10, o script mostra valores ausentes usando `isna()` e `isna().sum()`. Também demonstra `dropna()` e faz preenchimentos em uma cópia do DataFrame:

```python
dados_preenchidos = dados.copy()
dados_preenchidos["idade"] = dados_preenchidos["idade"].fillna(mediana_idade)
dados_preenchidos["cidade"] = dados_preenchidos["cidade"].fillna("Não informado")
```

Neste exemplo, optei por usar o marcador `Não informado` em vez de preencher a cidade com a moda. Essa escolha preserva a informação de que o dado original estava ausente e evita atribuir automaticamente uma cidade que pode não corresponder à realidade.

Valores ausentes também não devem ser tratados automaticamente sem analisar o contexto. Às vezes eles indicam erro de coleta; em outras situações, podem carregar uma informação importante.

## Sobre o arquivo CSV

O arquivo [dados.csv](dados.csv) foi criado como conjunto de dados de exemplo, porque a atividade não forneceu um CSV pronto.

Ele possui as colunas:

- `nome`
- `idade`
- `cidade`
- `tempo_atendimento`

O arquivo inclui pessoas maiores e menores de idade, valores ausentes em `idade` e `cidade`, e um valor alto em `tempo_atendimento` para servir como possível outlier.

## Como instalar as dependências

Execute o comando abaixo a partir da raiz do repositório:

É necessário ter Python 3 instalado para executar os comandos.

```bash
python -m pip install -r atividade-02/requirements.txt
```

## Como executar os programas

Para executar as questões 1 a 5:

```bash
python atividade-02/questoes_python.py
```

Para executar as questões 6 a 10:

```bash
python atividade-02/analise_dados.py
```
