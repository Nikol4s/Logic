import os

cardapio = {
    100: ["Cachorro Quente", 1.20],
    101: ["Bauru Simples", 1.30],
    102: ["Bauru com ovo", 1.50],
    103: ["Hambúrguer", 1.20],
    104: ["Cheeseburguer", 1.30],
    105: ["Refrigerante", 1.00],
}

sacolaPedido = 0
linha = 30 * "-"

os.system("cls")
while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))

    if codigo == 0:
        break

    if codigo in cardapio:
        quantidade = int(input("Digite a quantidade desejada: "))

        nome, preco = cardapio[codigo]
        valorTotal = preco * quantidade

        print(
            f"{linha}\nCód: {codigo}\n{nome}: {quantidade} Unidades\nValor: R${valorTotal:.2f}\n{linha}"
        )
        sacolaPedido += valorTotal
    else:
        print("Código inválido. Por favor, digite um código válido.")

print(f"\n------------Total: R${sacolaPedido:.2f}------------")
