import random

# Variáveis
linha1 = 25 * "-"

# Descrisão
titulo = f"{linha1}\nPalavras Embaralhadas"
tabela_temas = f"""
{linha1}
Digite (1) -> Animais
Digite (2) -> Frutas
Digite (3) -> Profissões
{linha1}
                """

# Palavras dos temas
palavras_animais = [
    "onça-pintada",
    "peru",
    "arraia",
    "chinchila",
    "periquito",
    "gafanhoto",
    "lince",
    "tartaruga",
    "cobra",
    "gato",
]
palavras_frutas = [
    "cajá",
    "goiaba",
    "maçã",
    "ameixa",
    "laranja",
    "coco",
    "damasco",
    "banana",
    "limão",
    "tangerina",
]
palavras_profissões = [
    "sapateiro",
    "empresário",
    "jardineiro",
    "jornalista",
    "médico",
    "carteira",
    "atleta",
    "arquiteta",
    "farmacêutico",
    "carpinteiro",
]

palavras_temas = palavras_animais, palavras_frutas, palavras_profissões

# Funções
def sorteador_palavras(lista):
    palavra = random.choice(lista)
    return palavra

def embaralhar_palavra(palavra):
    lista_de_caracteres = list(palavra)
    random.shuffle(lista_de_caracteres)
    palavra_embaralhada = "".join(lista_de_caracteres)
    return palavra_embaralhada


while True:
    print(titulo, tabela_temas)
    tema = str(input("Digite qual será o tema do jogo: "))

    if tema == "1":
        print(f"{linha1}\nTema: Animais")

        palavras_sendo_embaralhadas = [
            embaralhar_palavra(palavra_sorteada)
            for palavra_sorteada in palavras_animais
        ]
