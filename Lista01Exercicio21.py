preco = float(input("Informe o valor da roupa: "))
desconto = 0.3 # 30% de desconto
preco_liquidação = preco - (preco * desconto)
print(f"O valor da roupa com 30% de desconto é R$ {preco_liquidação:.2f}")
