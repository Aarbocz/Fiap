# Lista de restaurantes
restaurantes = []

while True:
    # Menu
    print("Menu: ")
    print("1 - Adicionar resutarante")
    print("2 - Mostrar ranking dos restaurantes")

    # Escolha do menu
    escolha = input("Escolha: ")

    # Adiciona restaurante
    if escolha == "1":

        # Get nome do restaurant
        nome = input("Nome: ")

        # Get nota do restaurante
        nota = -1
        while nota < 0 or nota > 5:
            nota = float(input("Nota: "))

        # Get distância do restaurante
        distancia = -1
        while distancia < 0:
            distancia = float(input("Distância(km): "))

        # Adiciona restaurante a lista de de restaurantes
        restaurante = [nome, nota, distancia]
        restaurantes.append(restaurante)
        print()

    # Imprimi ranking dos restaurantes
    elif escolha == "2":
        # Ordena lista de restaurantes por nota
        for x in range(len(restaurantes) -1, 0, -1):
            for y in range(0, x, 1):
                temp = []
                if restaurantes[x][1] > restaurantes[y][1]:
                    temp = restaurantes[x]
                    restaurantes[x] = restaurantes[y]
                    restaurantes[y] = temp

                # Ordena lista de restaurantes por distância em caso de empate por nota
                elif restaurantes[x][1] == restaurantes[y][1]:
                    if restaurantes[x][2] < restaurantes[y][2]:
                        temp = restaurantes[x]
                        restaurantes[x] = restaurantes[y]
                        restaurantes[y] = temp

        # Imprimi resultados
        print()
        for i in range(len(restaurantes)):
            print(f"Rank {i+1}: {restaurantes[i][0].upper()}, Nota: {restaurantes[i][1]}, Distância: {restaurantes[i][2]}.")
        break
    
    # Lida com opção inválida do menu
    else:
        print("Escolha invalida")
        print()