# leitura da quantidade de camisetas de cada tamanho
qtd_pequenas = int(input("Digite a quantidade de camisetas pequenas vendidas: "))
qtd_medias = int(input("Digite a quantidade de camisetas médias vendidas: "))
qtd_grandes = int(input("Digite a quantidade de camisetas grandes vendidas: "))

# cálculo do valor arrecadado
valor_total = (qtd_pequenas * 10) + (qtd_medias * 12) + (qtd_grandes * 15)

# exibição do valor arrecadado
print("O valor arrecadado foi de R$ {:.2f}".format(valor_total))
