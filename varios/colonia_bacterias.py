'''Programa: Población de una colonia de bacterias.
Se calcula el número de días en que la población de 
una colonia de bacterias se multiplica. '''

nd = 1
MO = 10 

Mmax = int(input("Dame la población máxima: \n"))

while(MO <= Mmax):
    MO = 2 * MO
    if MO <= Mmax:
        nd = nd + 2

print("El número de días es: ", nd)
print("La población de bacterias es: ", MO)