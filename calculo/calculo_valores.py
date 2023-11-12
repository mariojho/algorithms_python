''' Programa: Cálculo de f(x, y, z)
Este algoritmo calcula
los valores (f(x,y) = 3x ^ 3 + 7y ^ 2 * z. '''

from math import * 
x = 0

for x in range(5):
    y = 0.3
    while (y <= 1.5):
        z = -1
        while(z <= 8):
            f = 3 * pow(x, 3) + 7 * pow(y, 2) * z 
            print("f(x, y, z) = ", f)
            z = z + 3
        y = y + 0.3