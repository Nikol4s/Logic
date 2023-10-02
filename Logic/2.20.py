def cauculo_media(media):
    resultado = media / 3    
    if resultado == 10:
        print(f"Aprovado com Distinção.\nNota: {resultado:.1f}")
    elif resultado >= 7 and resultado <= 9:
        print(f"Aprovado.\nNota: {resultado:.1f}")
    else:
        print(f"Reprovado.\nNota: {resultado:.1f}")
    
notas_aluno = []

for notas in range(3):
    notas = float(input("Digite a nota do aluno: "))

    notas_aluno.append(notas)
    soma_lista = sum(notas_aluno)

print(cauculo_media(soma_lista))
