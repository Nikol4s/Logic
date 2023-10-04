import random


def sorteio(minimo, maximo):
    return random.randint(minimo, maximo)


linhas = 35 * "-"
lista_de_exercicios = sorteio(1, 2)

if lista_de_exercicios == 1:
    sequencial = sorteio(1, 18)
    print(
        f"{linhas}\n      |Estrutura Sequencial|     \n{linhas}\nExercicios: {sequencial}\n{linhas}\nhttps://wiki.python.org.br/EstruturaSequencial\n{linhas}"
    )
elif lista_de_exercicios == 2:
    desisão = sorteio(1, 28)
    print(
        f"{linhas}\n      |Estrutura Decisão|     \n{linhas}\nExercicios: {desisão}\n{linhas}\nhttps://wiki.python.org.br/EstruturaDeDecisao\n{linhas}"
    )
