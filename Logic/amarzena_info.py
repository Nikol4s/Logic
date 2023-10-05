palavras_embaralhadas_frutas = [
    embaralhar_palavra(palavra) for palavra in palavras_frutas
]

palavras_embaralhadas_profissões = [
    embaralhar_palavra(palavra) for palavra in palavras_profissões
]

jogador = str(input("Digite a palavra:"))

        if jogador == palavra_sorteada:
            print(f"Você ganhou!\nPalavra desembaralhada: {palavra_sorteada}")
            break
        elif jogador != palavra_sorteada:
            print(f"Você errou! Palavra ainda embaralhada!")
