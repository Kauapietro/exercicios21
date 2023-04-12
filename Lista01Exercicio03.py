custo_fabrica = float(input("Digite o custo de fábrica do carro:"))

percentagem_distribuidor = 0.28
impostos = 0.45

custo_consumidor = custo_fabrica + (custo_fabrica * percentagem_distribuidor) + (custo_fabrica * impostos)

print("O custo do consumidor é R$", custo_consumidor)