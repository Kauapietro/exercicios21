# Lê o peso do prato montado pelo cliente
peso_prato = float(input("Digite o peso do prato montado pelo cliente (em quilos): "))

# Calcula o valor a pagar
valor_a_pagar = peso_prato * 19.00

# Apresenta o resultado
print("O valor a pagar é R$ {:.2f}".format(valor_a_pagar))
