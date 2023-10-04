linha1 = 63 * "-"
linha2 = 35 * "-"

while True:
    numero = int(input("Digite o número: "))

    if numero >= 1000:
        print(
            f"{linha1}\nValor Invalido! Apenas numeros com centenas, dezenas e unidade.\n{linha1}"
        )

    if numero <= 999 and numero >= 100:
        convertendo = str(numero)
        centenas = convertendo[0:1]
        dezenas = convertendo[1:2]
        unidades = convertendo[2:3]

        junção_centenas = f"{centenas} centenas {dezenas} dezenas é {unidades} unidades"

        print(f"{linha2}\n{junção_centenas}\n{linha2}")

    elif numero <= 99 and numero >= 10:
        convertendo = str(numero)
        dezenas = convertendo[0:1]
        unidades = convertendo[1:2]

        junção_dezenas = f"{dezenas} dezenas é {unidades} unidades"

        print(f"{linha2}\n{junção_dezenas}\n{linha2}")
        
    elif numero <= 9 and numero >= 1:
        convertendo = str(numero)
        unidades = convertendo[0:1]

        junção_unidades = f'{unidades} unidades'
        
        print(f'{linha2}\n{junção_unidades}\n{linha2}')
    
    elif numero == 0:
        print('Fim!')
        break