# Quantidade de alimentos ingeridos em um dia
alimentos = 0
# Quantidade de calorias ingeridas em um dia
calorias = 0

# Menu para adicionar alimentos ingeridos
while True:

    print("1 - Adicionar alimento")
    print("2 - Calcular total de calorias e sair")

    # Opção para o usário escolher o que fazer
    escolha = int(input("Número: "))

    # Adiciona alimento e update "alimentos" e "calorias"
    if escolha == 1:
        alimento = input("Alimento: ")
        caloria = float(input("Calorias: "))

        alimentos += 1
        calorias += caloria

        print(f"Alimento registrado. {alimento}: {caloria} calorias")
    
    # Mostra resultado final e sai do programa
    elif escolha == 2:
        print(f"Você comeu {alimentos} alimentos hoje, com um total de {calorias} calorias.")
        break

    # Lida com escolha inválida no menu
    else:
        print("Escolha inválida")

