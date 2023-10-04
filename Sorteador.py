from random import randint

lista_de_exercicios = randint(1, 8)

sequencial = randint(1, 18)
decisao = randint(1, 28)
repeticao = randint(1, 51)
lista = randint(1, 24)
funcoes = randint(1, 14)
strings = randint(1, 14)
arquivos = randint(1, 2)
classes = randint(1, 17)

while True:
    sorteador = int(input('Digite "0" para sortear...\n  '))
    print(f'Número sorteado: {lista_de_exercicios}')
    if lista_de_exercicios == 1:
        print(f'O exercicio será: {sequencial}')
        break
    elif lista_de_exercicios == 2:
        print(f'O exercicio será: {decisao}')
        break
    elif lista_de_exercicios == 3:
        print(f'O exercicio será: {repeticao}')
        break
    elif lista_de_exercicios == 4:
        print(f'O exercicio será: {lista}')
        break
    elif lista_de_exercicios == 5:
        print(f'O exercicio será: {funcoes}')
        break
    elif lista_de_exercicios == 6:
        print(f'O exercicio será: {strings}')
        break
    elif lista_de_exercicios == 7:
        print(f'O exercicio será: {arquivos}')
        break
    elif lista_de_exercicios == 8:
        print(f'O exercicio será: {classes}')
        break
        