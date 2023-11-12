''' Programa: Suma de enteros 1.
Usa la instrucción while (mientras)
Esta aplicación suma los enteros del 1 al N. '''

suma = 0
j = 1
print("Dame el valor de N:")
N = int(input())

while (j <= N):
    suma = suma + j
    j = j + 1

print("La suma es: ", suma)