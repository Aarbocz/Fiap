# Get numeros de alunos
alunos = int(input("Número de alunos: "))

# Define count para dia da semana
segunda = 0
terça = 0
quarta = 0
quinta = 0
sexta = 0

# Get voto de cada aluno
for aluno in range(alunos):
    voto = ""
    while not (voto == "segunda" or voto == "terça" or voto == "quarta" or voto == "quinta" or voto == "sexta"):

        voto = input("Qual é o melhor dia da semana para as LIVES: ").lower()

        # Update count
        if voto == "segunda":
            segunda += 1
        elif voto == "terça":
            terça += 1
        elif voto == "quarta":
            quarta += 1
        elif voto == "quinta":
            quinta += 1
        elif voto == "sexta":
            sexta += 1
        else:
            print("Voto inválido, tente novamente: ")

# Print numero de votos para cada dia
print("Votos: ")
print(f"Segunda: {segunda}")
print(f"Terça: {terça}")
print(f"Quarta: {quarta}")
print(f"Quinta: {quinta}")
print(f"Sexta: {sexta}")

# Print o vencedor
if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f"Pareçe que segunda-feira venceu com {segunda} votos.")
elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print(f"Pareçe que terça-feira venceu com {terça} votos.")
elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print(f"Pareçe que quarta-feira venceu com {quarta} votos.")
elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print(f"Pareçe que quinta-feira venceu com {quinta} votos.")
elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print(f"Pareçe que sexta-feira venceu com {sexta} votos.")
else:
    print("Ah não, houve um empate...")