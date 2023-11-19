''' Cálculo del área de un trapecio '''

area = 0; base_mayor = 0; base_menor = 0; altura = 0

base_mayor = float(input("Dame la base mayor del trapecio: "))
base_menor = float(input("Dame la base menor del trapecio: "))
altura = float(input("Dame la altura del trapecio: "))

area = ((base_mayor + base_menor) / 2) * altura

print("El área del trapecio es: ", area, "\n")