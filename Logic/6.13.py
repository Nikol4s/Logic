import random

def sorteador_palavras(op):
    palavra = random.choice(op)
    print(palavra)

def embaralhar_palavra(palavra):
    lista_de_caracteres = list(palavra)
    random.shuffle(lista_de_caracteres)
    palavra_embaralhada = "".join(lista_de_caracteres)
    return palavra_embaralhada


# lista de palavra: temas
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

palavras_embaralhadas_frutas = [
    embaralhar_palavra(palavra) for palavra in palavras_frutas
]
palavras_embaralhadas_animais = [
    embaralhar_palavra(palavra) for palavra in palavras_animais
]
palavras_embaralhadas_profissões = [
    embaralhar_palavra(palavra) for palavra in palavras_profissões
]

while True:
    