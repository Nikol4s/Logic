print('Loja Quase Dois - Tabela de preços\n')
for numerosOrdinais in range(1, 51):
    preco = 1.99 * numerosOrdinais
    print(f'{numerosOrdinais} - R${preco:.2f}')