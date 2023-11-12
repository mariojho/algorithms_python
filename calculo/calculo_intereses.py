'''Cálculo de intereses.
Este algoritmo calcula el interés simple y compuesto'''

capital = int(input("Dame el capital: \n"))
tasa = int(input("Dame la tasa: \n"))
n = int(input("Dame el número de meses: \n"))

int_simple = capital * n * tasa

int_compuesto = capital * pow(1 + tasa, n)

print("\n Interés simple: %0.2f" %int_simple)
print("Interés compuesto: %0.2f" %int_compuesto)
