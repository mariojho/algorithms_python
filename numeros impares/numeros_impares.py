''' Algoritmo para seleccionar impares y terminar al
encontrar el primero divisible por 5 '''

for x in range(1, 10):
    if(not x%2) and (x%5):
        continue
    if(x%5 == 0):
        break
    print(x, "\n")