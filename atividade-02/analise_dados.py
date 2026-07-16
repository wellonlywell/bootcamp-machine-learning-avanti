from pathlib import Path

import pandas as pd


def mostrar_titulo(texto):
    print("\n" + "=" * 40)
    print(texto)
    print("=" * 40)


def questao_6():
    mostrar_titulo("QUESTÃO 6")

    atendimentos = pd.DataFrame(
        {
            "tempo_atendimento": [10, 12, 11, 13, 14, 15, 120],
        }
    )

    print("Dados de atendimento:")
    print(atendimentos)

    # Método dos quartis e IQR.
    q1 = atendimentos["tempo_atendimento"].quantile(0.25)
    q3 = atendimentos["tempo_atendimento"].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    outliers_iqr = atendimentos[
        (atendimentos["tempo_atendimento"] < limite_inferior)
        | (atendimentos["tempo_atendimento"] > limite_superior)
    ]

    print("\nLimites pelo IQR:")
    print("Limite inferior:", limite_inferior)
    print("Limite superior:", limite_superior)
    print("Possíveis outliers pelo IQR:")
    print(outliers_iqr)

    # Método da média e três desvios-padrão.
    media = atendimentos["tempo_atendimento"].mean()
    desvio = atendimentos["tempo_atendimento"].std()
    limite_inferior_dp = media - 3 * desvio
    limite_superior_dp = media + 3 * desvio
    outliers_dp = atendimentos[
        (atendimentos["tempo_atendimento"] < limite_inferior_dp)
        | (atendimentos["tempo_atendimento"] > limite_superior_dp)
    ]

    print("\nLimites pela média e três desvios-padrão:")
    print("Limite inferior:", limite_inferior_dp)
    print("Limite superior:", limite_superior_dp)
    print("Possíveis outliers pela média e três desvios-padrão:")
    print(outliers_dp)
    print("O valor não foi removido automaticamente.")


def questao_7():
    mostrar_titulo("QUESTÃO 7")

    df1 = pd.DataFrame(
        {
            "nome": ["Ana", "Bruno"],
            "idade": [22, 17],
        }
    )
    df2 = pd.DataFrame(
        {
            "nome": ["Carlos", "Marina"],
            "cidade": ["Salvador", "São Paulo"],
        }
    )

    linhas = pd.concat([df1, df2], axis=0, ignore_index=True)
    colunas = pd.concat([df1, df2], axis=1)

    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    print("\nConcatenação por linhas com axis=0:")
    print(linhas)
    print("\nConcatenação por colunas com axis=1:")
    print(colunas)


def carregar_dados_csv():
    caminho_csv = Path(__file__).parent / "dados.csv"
    return pd.read_csv(caminho_csv)


def questao_8(dados):
    mostrar_titulo("QUESTÃO 8")

    print("Primeiras linhas do arquivo dados.csv:")
    print(dados.head())


def questao_9(dados):
    mostrar_titulo("QUESTÃO 9")

    nomes = dados["nome"]
    maiores_de_idade = dados[dados["idade"] >= 18]

    print("Coluna nome:")
    print(nomes)
    print("\nPessoas com idade maior ou igual a 18:")
    print(maiores_de_idade)


def questao_10(dados):
    mostrar_titulo("QUESTÃO 10")

    print("Valores ausentes com isna():")
    print(dados.isna())

    print("\nQuantidade de valores ausentes por coluna:")
    print(dados.isna().sum())

    print("\nRemovendo linhas com valores ausentes usando dropna():")
    print(dados.dropna())

    dados_preenchidos = dados.copy()

    # Preenche idade com a mediana da coluna.
    mediana_idade = dados_preenchidos["idade"].median()
    dados_preenchidos["idade"] = dados_preenchidos["idade"].fillna(mediana_idade)

    # Preenche cidade com um texto padrão.
    dados_preenchidos["cidade"] = dados_preenchidos["cidade"].fillna("Não informado")

    print("\nDataFrame com valores preenchidos:")
    print(dados_preenchidos)


if __name__ == "__main__":
    questao_6()
    questao_7()

    dados_csv = carregar_dados_csv()
    questao_8(dados_csv)
    questao_9(dados_csv)
    questao_10(dados_csv)
