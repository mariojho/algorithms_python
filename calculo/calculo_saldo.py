''' Cálculo del saldo '''

print("Dame el saldo actual: ")
saldo = float(input())

if (saldo < 10000.00):
    saldo = saldo * (1 + 0.03)
else:
    saldo = saldo * (1 + 0.04)

print("Saldo final es: %5.2f" %saldo)