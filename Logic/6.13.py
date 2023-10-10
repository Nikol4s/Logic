import random

l1 = 16 * "-"
titulo = f"{l1}\nJogo Embaralhado\n{l1}"
palavras = [
    "contundido",
    "cursivo",
    "indagar",
    "folhagem",
    "navegador",
    "iris",
    "digital",
    "odontologo",
    "grande",
    "fardado",
    "palido",
    "alto-astral",
    "recomendaria",
    "facultativo",
    "fisico",
    "paredro",
    "unicamente",
    "moralizador",
    "lesante",
    "geotecnica",
]


def sorteador(string):
    sorteando = random.choice(string)
    return sorteando


def embaralhador(palavra):
    caracteres = list(palavra)
    random.shuffle(caracteres)
    embaralhado = "".join(caracteres)
    return embaralhado

palavras_sorteada = sorteador(palavras)
palavras_embaralhadas = embaralhador(palavras_sorteada)

while True:
    print(titulo)
    player = str(
        input(f"Palavra embaralhada: {palavras_embaralhadas}\nDigite a palavra: ")
    )

    if player == palavras_sorteada:
        print(f'\n{l1} Você Ganhou! {l1}\n\nPalavra desembaralhada: {palavras_sorteada}')
        break
    else:
        print(f'\n{l1} Você errou! Tente novamente {l1}\n')