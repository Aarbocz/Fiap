# Get número do usuario
numero = int(input("Digite aqui um número na sequenência do Fibonacci: "))

# Numeros da sequencia
fibo1 = 0 
fibo2 = 1
fibo3 = fibo1 + fibo2

# Verifica se o numero faz parte da sequencia
while fibo3 <= numero:

    if fibo3 == numero:
        print("Ação bem sucedida!")
        exit()
    
    else:
        # Update sequencia
        fibo1 = fibo2
        fibo2 = fibo3
        fibo3 = fibo1 + fibo2

print("A ação falhou...")