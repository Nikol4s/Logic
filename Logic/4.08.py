def validarNumero(num):
    if num >= 1:
        return 'Positivo'
    else:
        return 'Negativo'
    
numero = int(input('Digite: '))

print(validarNumero(numero))