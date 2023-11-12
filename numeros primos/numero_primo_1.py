''' Programa Primo: Evalúa si un entero es primo '''
from math import sqrt

print("¿Número a evaluar?")
N = int(input())

divisor = 2
es_primo = True

while (N <= sqrt(N) and es_primo):
    cociente = N / divisor
    if (cociente * divisor == N):
        es_primo = False
        
    divisor = divisor + 1
    
if(es_primo):
    print("Sí es primo")
else:
    print("NO es primo")