total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ''
preco_mais_barato = None

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto (R$): "))
    
    total_gasto += preco

    if preco > 1000:
        produtos_acima_1000 += 1

    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    continuar = input("Deseja adicionar mais produtos? [S/N]: ").strip().upper()
    if continuar != 'S':
        break

print("\n==== RESUMO DA COMPRA ====")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")
