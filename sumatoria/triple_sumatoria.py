''' Algoritmo que realiza una triple sumatoria. '''

S = 0
for i in range(11):
    for j in range (5, 10):
        for k in range(-1, 8):
            S = S + i * j * k 

S = S + 23
print("El valor de S es: ", S)