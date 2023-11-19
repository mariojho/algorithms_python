''' Cálculo del volúmen de un cono '''
from math import pi

radio = 0; altura = 0; volumen_cono = 0

radio = float(input("Dame el radio del cono: "))
altura = float(input("Dame la altura del cono: "))
volumen_cono = (pi * radio * radio * altura) / 3

print("El volúmen del cono es: ", volumen_cono, "\n")