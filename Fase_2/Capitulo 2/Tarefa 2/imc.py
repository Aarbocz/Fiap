# Get peso
peso = float(input("Peso: "))
# Get altura
altura = float(input("Altura "))

# Calcula IMC 
imc = peso / altura ** 2

# Verefica categoria
categoria = ""
if imc < 16:
    categoria = "Baixo peso Grau 3"
elif imc >= 16 and imc < 17:
    categoria = "Baixo peso Grau 2"
elif imc >= 17 and imc < 18.50:
    categoria = "Baixo peso Grau 1"
elif imc >= 18.50 and imc < 25:
    categoria = "Peso ideal"
elif imc >= 25 and imc < 30:
    categoria = "Sobrepeso"
elif imc >= 30 and imc < 35:
    categoria = "Obesidade Grau 1"
elif imc >= 35 and imc < 40:
    categoria = "Obesidade Grau 2"
elif imc >= 40:
    categoria = "Obesidade Grau 3"

# Print resultados
imc_formated = float("{:.2f}".format(imc))
print(f"O seu IMC é {imc_formated} e você esta na catagoria {categoria}")


