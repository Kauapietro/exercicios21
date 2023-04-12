salario = float(input("Digite o salário do funcionário: "))

# Aplica aumento de 15%
salario_aumento = salario * 1.15

# Desconta 8% de impostos
salario_final = salario_aumento * 0.92

# Mostra os resultados
print("Salário inicial: R$ {:.2f}".format(salario))
print("Salário com aumento: R$ {:.2f}".format(salario_aumento))
print("Salário final: R$ {:.2f}".format(salario_final))
