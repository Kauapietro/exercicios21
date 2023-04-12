# Lê a quantidade de pães e bolos vendidos
qtd_paes = int(input("Digite a quantidade de pães vendidos: "))
qtd_bolos = int(input("Digite a quantidade de bolos vendidos: "))

# Calcula o valor total arrecadado
valor_paes = qtd_paes * 0.12
valor_bolos = qtd_bolos * 1.50
total_arrecadado = valor_paes + valor_bolos

# Calcula o valor a ser guardado na conta de poupança
valor_poupanca = total_arrecadado * 0.1

# Apresenta os resultados
print("Valor total arrecadado: R$", total_arrecadado)
print("Valor a ser guardado na conta de poupança: R$", valor_poupanca)
