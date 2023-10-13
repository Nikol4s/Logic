import random
import os
def sorteador(minimo, maximo):
    sorteando = random.randint(minimo, maximo)
    return sorteando

l1 = 10 * '-'
l2 = 46 * '-'
exercicioLista = sorteador(1, 7)
os.system('cls')
if exercicioLista == 1:
    print(f'{l1} Sequencial - 1 {l1}')
    print(f'Exercício: {sorteador(1, 18)}\n{l2}')
    print('https://wiki.python.org.br/EstruturaSequencial')
elif exercicioLista == 2:
    print(f'{l1} Decisão - 2 {l1}')
    print(f'Exercício: {sorteador(1, 28)}\n{l2}')
    print('https://wiki.python.org.br/EstruturaDeDecisao')
elif exercicioLista == 3:
    print(f'{l1} Repetição - 3 {l1}')
    print(f'Exercício: {sorteador(1, 51)}\n{l2}')
    print('https://wiki.python.org.br/EstruturaDeRepeticao')
elif exercicioLista == 4:
    print(f'{l1} Lista {l1}')
    print(f'Exercício: {sorteador(1, 24)}\n{l2}')
    print('https://wiki.python.org.br/ExerciciosListas')
elif exercicioLista == 5:
    print(f'{l1} Funções - 4 {l1}')
    print(f'Exercício: {sorteador(1, 14)}\n{l2}')
    print('https://wiki.python.org.br/ExerciciosFuncoes')
elif exercicioLista == 6:
    print(f'{l1} Strings - 5 {l1}')
    print(f'Exercício: {sorteador(1, 14)}\n{l2}')
    print('https://wiki.python.org.br/ExerciciosComStrings')
elif exercicioLista == 7:
    print(f'{l1} Classes - 6 {l1}')
    print(f'Exercício: {sorteador(1, 17 )}\n{l2}')
    print('https://wiki.python.org.br/ExerciciosClasses')