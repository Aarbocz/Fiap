# Get tipo de assinatura
print("Tipo de assinatura:")
print("1 - Basic")
print("2 - Silver")
print("3 - Gold")
print("4 - Platinum")

assinatura = int(input("Numero: "))

if not (assinatura == 1 or assinatura == 2 or assinatura == 3 or assinatura == 4):
    print("Tipo de assinatura inválida.")
    exit()

# Get faturamento anual
faturamento = float(input("Faturamento anual: "))

# Calcula valor do bonus
bonus = 0
if assinatura == 1:
    bonus = (faturamento / 100) * 30
elif assinatura == 2:
    bonus = (faturamento / 100) * 20
elif assinatura == 3:
    bonus = (faturamento / 100) * 10
elif assinatura == 4:
    bonus = (faturamento / 100) * 5

# Helper function - transforma em real
def real(value):
    return f"R${value:,.2f}"

print(f"Você deve pagar {real(bonus)}.")