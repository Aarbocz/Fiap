# Soma dos alunos impares
soma_impar = 0 
# Soma dos alunos pares
soma_par = 0

# Get notas dos alunos impares
print("Você está digitando as notas dos alunos ímpares.")
for aluno in range(1, 50, 2):
    nota = float(input(f"Por favor, insira a nota do aluno {aluno}: "))

    soma_impar += nota

# Imprimi linha em branco   
print()

# Get nota dos alunos pares
print("Você está digitando as notas dos alunos pares.")
for aluno in range(2, 51, 2):
    nota = float(input(f"Por favor, insira a nota do aluno {aluno}: "))

    soma_par += nota

# Calcula média
media_impar = soma_impar / 25
media_par = soma_par / 25

# Imprimi resultado
print()
print(f"Média dos alunos ímpares: {media_impar}")
print(f"Média dos alunos pares: {media_par}")
print()
if media_impar > media_par:
    print("Alunos ímpares tiveram uma média maior que alunos pares.")
elif media_par > media_impar:
    print("Alunos pares tiveram uma média maior que alunos ímpares.")
else:
    print("Parece que tivemos um empate.")