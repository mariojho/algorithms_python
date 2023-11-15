''' Palíndromo 
Determina si una frase es palíndromo 
TODO: Revisar el código, no funciona correctamente'''

from math import ceil

numero = 0; contador = 0

print("Dame el número de letras de la frases: ")
max = int(input())
print("Dame las letras de la frase: ")
letra = []
while(numero <= max - 1):
    print("Dame una letra de la frase: ")
    letra += [input()]
    numero = numero + 1

inverso = max
numero = 0
frase = [None] * max

while(numero <= max - 1):
    frase[inverso - 1] = letra[numero]
    inverso = inverso + 1
    numero = numero + 1

numero = 0; contador = 0 

while(numero <= ceil(max / 2)):
    if (frase[numero] == letra[numero]):
        contador = contador + 1
    numero = numero + 1

if (contador == ceil(max / 2) + 1):
    print("La frase SÍ es palíndromo")
else:
    print("La frase NO es palíndromo")