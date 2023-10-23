
pesoMax = 50

pesoPeixe = float(input('Digite o peso: '))

if pesoPeixe > pesoMax:
    pesoExcedido = pesoPeixe - pesoMax 
    print(f'R${4 * pesoExcedido:.2f}')
else:
    print('Não excedeu')