# Lê o preço de custo e o percentual de acréscimo
preco_custo = float(input("Digite o preço de custo do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))

# Calcula o valor de venda
preco_venda = preco_custo * (1 + percentual_acrescimo/100)

# Apresenta o resultado
print("Preço de venda do produto: R$", preco_venda)
