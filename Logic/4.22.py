import os
from prettytable import PrettyTable

ListaColaboradores = []

# Cria uma tabela
tabela = PrettyTable()
tabela.field_names = ['Salário', 'Abono']

while True:
    salario = float(input('Salário: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if salario == 0:
        break

    abonoSalarial = salario * 0.2
    ListaColaboradores.append([salario, abonoSalarial])
    tabela.add_row(["R$ {:.2f}".format(salario), "R$ {:.2f}".format(abonoSalarial)])

print('Projeção de Gastos com Abono\n============================')
print(tabela)

print(f'Foram processados {len(ListaColaboradores)} colaborador(es)')

totalAbono = sum(item[1] for item in ListaColaboradores)
print(f'Total gasto com abonos: R$ {totalAbono:.2f}')

menorAbono = [abono for _, abono in ListaColaboradores if _ < 1000 and _ >= 1]
print(f'Valor mínimo pago a {len(menorAbono)} colaborador(es):')

maiorAbono = max(item[1] for item in ListaColaboradores)
print(f'Maior valor de abono pago: R$ {maiorAbono:.2f}')