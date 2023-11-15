''' Varianaza y desviación estándard '''

from math import sqrt

suma = 0; vector = [None] * 5; var = 0; desv = 0

for cont in range(5):
    print("Dame un elemento:")
    vector[cont] = int(input())
    suma = suma + vector[cont]

pr = suma / 5

for k in range(5):
    var = var + pow(vector[k] - pr, 2)
    var = var / 5
    desv = sqrt(var)
    
print("Varianza, Desviación Estándard")
print(var,"\t", desv)