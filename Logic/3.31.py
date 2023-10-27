ListaCompras = []

while True:
    for ordinais in range(1000):
        compras = float(input(f'Produto {ordinais}: '))
        ListaCompras.append(compras)
        
        if compras == 0:
            total = sum(item for item in ListaCompras)
            print(f'\nTotal: R${total:.2f}')
            dinheiro = float(input('Dinheiro: R$'))
            print(f'Troco: R${dinheiro - total:.2f}')
            break
    break