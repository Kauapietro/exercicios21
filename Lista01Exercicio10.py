# Lê o nome do vendedor, o salário fixo e o total de vendas
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor: "))

# Calcula o salário final com a comissão de 15% sobre as vendas
comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao

# Apresenta os resultados
print("Nome do vendedor:", nome)
print("Salário fixo:", salario_fixo)
print("Salário final:", salario_final)