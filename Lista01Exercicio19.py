# entrada de dados
quantidade_sanduiches = int(input("Informe a quantidade de sanduíches a fazer: "))

# cálculo da quantidade de cada ingrediente
quantidade_queijo = quantidade_sanduiches * 2 * 0.05 # duas fatias de queijo por sanduíche, cada fatia pesa 50g
quantidade_presunto = quantidade_sanduiches * 1 * 0.05 # uma fatia de presunto por sanduíche, cada fatia pesa 50g
quantidade_carne = quantidade_sanduiches * 1 * 0.1 # uma rodela de hambúrguer por sanduíche, cada rodela pesa 100g

# exibição dos resultados
print("Para produzir", quantidade_sanduiches, "sanduíches será necessário comprar:")
print(quantidade_queijo, "quilos de queijo")
print(quantidade_presunto, "quilos de presunto")
print(quantidade_carne, "quilos de carne")
