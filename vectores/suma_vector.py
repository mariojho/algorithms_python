''' Suma de vector.
Calcula la suma elementos de un vector. '''

suma = 0; vector = [None] * 5

for cont in range(5):
    print("Iteración: ", cont + 1)
    a = int(input("Dame un elemento "))
    vector[cont] = a
    suma = suma + vector[cont]

print("Suma: ", suma)