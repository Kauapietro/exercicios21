# Lê o valor depositado
valor_depositado = float(input("Digite o valor depositado: "))

# Calcula o valor com rendimento após um mês considerando o juro da poupança em 0,70% ao mês
juro = 0.007  # juro de 0,70% ao mês
valor_rendimento = valor_depositado + (valor_depositado * juro)

# Apresenta o resultado
print("Valor com rendimento após um mês:", valor_rendimento)
