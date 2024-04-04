''' Cálculo del valor presente '''

valor_presente = 0; tasa_interes = 0; anios = 0; capital = 0

capital = float(input("Ingrese el capital: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))
anios = float(input("Ingrese el número de años: "))

if capital > 0 and tasa_interes > 0 and anios > 0:
    valor_presente = capital / ((1 + tasa_interes) ** anios)
    print("El valor presente es: ", valor_presente)
else:
    print("El capital, la tasa de interés y el número de años deben ser mayores a cero")
