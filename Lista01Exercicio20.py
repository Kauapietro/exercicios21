# Lê a quantidade de cada tipo de moeda
um_centavo = int(input("Quantidade de moedas de 1 centavo: "))
cinco_centavos = int(input("Quantidade de moedas de 5 centavos: "))
dez_centavos = int(input("Quantidade de moedas de 10 centavos: "))
vinte_e_cinco_centavos = int(input("Quantidade de moedas de 25 centavos: "))
cinquenta_centavos = int(input("Quantidade de moedas de 50 centavos: "))
um_real = int(input("Quantidade de moedas de 1 real: "))

# Calcula o valor total em reais
total_em_centavos = um_centavo + cinco_centavos*5 + dez_centavos*10 + \
                    vinte_e_cinco_centavos*25 + cinquenta_centavos*50 + um_real*100
total_em_reais = total_em_centavos / 100

# Exibe o valor total economizado
print("O valor total economizado é de R$ %.2f" % total_em_reais)
