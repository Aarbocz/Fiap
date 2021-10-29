# Recebe minutos do usuario (0-60)
minutos = int(input("Quantos minutos são agora: "))

if minutos < 0 or minutos > 60:
    print("Minutos ínvalido")
    exit()

# Calcula fatorial do minutos
fatorial = 1

for minuto in range(minutos, 0, -1):
    fatorial = fatorial * minuto

# Imprimi senha
print(f"LIBERDADE{fatorial}")