# Lê o nome do aluno
nome = input("Digite o nome do aluno: ")

# Lê as notas das três provas
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

# Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Imprime o nome do aluno e a sua média
print("O aluno", nome, "obteve média", media)