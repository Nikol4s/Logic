def contador(n):
    contagem = len(n)
    return contagem

numeroTelefone = int(input('Telefone: '))
convertendoNumero = str(numeroTelefone)
numeroContado = contador(convertendoNumero)

primeiroNumero = convertendoNumero[0 : 3]
segundoNumero = convertendoNumero[3 : 8]

if numeroContado <= 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    print(f'Telefone corrigido sem formatação: 3{numeroTelefone}')
    print(f'Telefone corrigido com formatação: 3{primeiroNumero}-{segundoNumero}')
else:
    primeiroNumero = convertendoNumero[0 : 4]
    segundoNumero = convertendoNumero[4 : 8]
    print(f'{primeiroNumero}-{segundoNumero}')