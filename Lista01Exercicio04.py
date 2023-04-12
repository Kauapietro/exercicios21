distancia = float(input("Digite a distância total percorrida pelo automóvel em km: "))
combustivel = float(input("Digite o total de combustível gasto em litros: "))

consumo_medio = distancia / combustivel

print(f'O consumo médio do automóvel foi de {consumo_medio:.1f} "km/l.')
