def verficadorDI(numero):
    inteiro = round(numero)
    if numero == inteiro:
        return f'Número {numeros:.0f} é inteiro'
    else:
        return f'Número {numeros} é Decimal'

numeros = float(input('Digite o número: '))
print(verficadorDI(numeros))



