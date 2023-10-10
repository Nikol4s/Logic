lista_notas = []

def calculador_media(valor):
    media = 4
    calculo = valor / media
    return calculo

while True:
    for notas in range(4):
        notas = float(input("Digite as notas:"))
    print(f'\nMedia aluno: {calculador_media(notas)}')
    
  