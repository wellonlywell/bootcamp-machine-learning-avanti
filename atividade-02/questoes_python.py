def numeros_impares(numeros):
    """Retorna apenas os números ímpares da lista."""
    impares = []

    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)

    return impares


def eh_primo(numero):
    """Verifica se um número é primo."""
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


def numeros_primos(numeros):
    """Retorna apenas os números primos da lista."""
    primos = []

    for numero in numeros:
        if eh_primo(numero):
            primos.append(numero)

    return primos


def elementos_exclusivos(lista1, lista2):
    """Retorna elementos que aparecem em somente uma das listas."""
    exclusivos = []

    for elemento in lista1:
        if elemento not in lista2 and elemento not in exclusivos:
            exclusivos.append(elemento)

    for elemento in lista2:
        if elemento not in lista1 and elemento not in exclusivos:
            exclusivos.append(elemento)

    return exclusivos


def segundo_maior(numeros):
    """Retorna o segundo maior valor diferente do maior."""
    valores_unicos = []

    for numero in numeros:
        if numero not in valores_unicos:
            valores_unicos.append(numero)

    if len(valores_unicos) < 2:
        return None

    valores_unicos.sort(reverse=True)
    return valores_unicos[1]


def ordenar_pessoas(pessoas):
    """Ordena pessoas pelo nome, ignorando maiúsculas e minúsculas."""
    return sorted(pessoas, key=lambda pessoa: pessoa[0].lower())


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    lista_a = [1, 2, 3, 4, 4, 5]
    lista_b = [4, 5, 6, 7, 7, 8]
    valores = [10, 30, 20, 30, 5]
    valores_repetidos = [8, 8, 8]
    pessoas = [
        ("Marina", 22),
        ("ana", 18),
        ("Bruno", 25),
        ("carlos", 17),
    ]

    print("QUESTÃO 1")
    print("Números ímpares:", numeros_impares(numeros))

    print("\nQUESTÃO 2")
    print("Números primos:", numeros_primos(numeros))

    print("\nQUESTÃO 3")
    print("Elementos exclusivos:", elementos_exclusivos(lista_a, lista_b))

    print("\nQUESTÃO 4")
    print("Segundo maior:", segundo_maior(valores))
    print("Segundo maior quando não existe:", segundo_maior(valores_repetidos))

    print("\nQUESTÃO 5")
    print("Pessoas ordenadas:", ordenar_pessoas(pessoas))
