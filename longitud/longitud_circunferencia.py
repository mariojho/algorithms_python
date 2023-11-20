''' Cálculo de la logitud de la circunferencia de radio '''
from math import pi

longitud = 0; radio = 0
longitud = float(input("Dame la longitud de la circunferencia: "))
radio = longitud / (2 * pi)

print("El radio de la circunferencia es: ", radio, "\n")