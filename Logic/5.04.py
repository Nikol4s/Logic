def verficadorPN(num):
    if num <= 0:  
        return 'Negativo'
    else:
        return 'Positivo'
    
numero = int(input('Digite o número: '))
print(verficadorPN(numero))