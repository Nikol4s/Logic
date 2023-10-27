#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def numerosImpares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 != 0:
            contador += 1
    return contador

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = numerosImpares(lista_de_numeros)
print("Número de ímpares na lista:", resultado)