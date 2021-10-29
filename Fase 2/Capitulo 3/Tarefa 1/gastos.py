# Get total de transações no dia
transacoes = int(input("Quantas transações você fez hoje: "))

# Guarda total de gasto no dia
gastos = 0

print("Custo de cada transação")

# Get transações do user
for transacao in range(1, transacoes + 1):
    gasto = float(input(f"Transação {transacao}: "))
    gastos += gasto

# Calcula media por transação
media = gastos / transacoes

# Helper function - transforma em real
def real(value):
    return f"R${value:,.2f}"

# Imprimi resultados 
print(f"Você gastou um total de {real(gastos)} hoje. Em média você gastou {real(media)} por item.")