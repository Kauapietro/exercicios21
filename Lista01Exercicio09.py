# Lê o preço do litro da gasolina e o valor do pagamento
preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor do pagamento: "))

# Calcula quantos litros de gasolina o motorista conseguiu colocar no tanque
litros = valor_pagamento / preco_litro

# Apresenta o resultado
print("O motorista conseguiu colocar", litros, "litros de gasolina no tanque.")