''' Ecuación de segundo grado '''

from math import *

a = float(input("Dame a: "))
b = float(input("Dame b: "))
c = float(input("Dame c: "))

# Calcular discriminante
d = b ** 2 - 4 * a * c
if (d > 0):
    print("Raíces reales")
    print("y diferentes")
    x1 = (-b + sqrt(d)) / 2 / a
    x2 = (-b - sqrt(d)) / 2 / a
    print(x1)
    print(x2)

if (d == 0):
    print("Raices cuadradas")
    print("e iguales")
    x1 = -b / 2 / a
    x2 = x1 
    print(x1)
    print(x2)

if (d < 0):
    print("Raices complejas")
    print("y conjugadas:")
    x1_parte_real = -b / 2 / a 
    x1_parte_im = sqrt(-d) / 2 / a
    x2_parte_real = -b /2 / a
    x2_parte_im = -sqrt(-d) / 2 / a
    print(x1_parte_real)
    print(x1_parte_im)
    print(x2_parte_real)
    print(x2_parte_im)