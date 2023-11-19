''' Algoritmo de ordenamiento por selección '''

calif = [4, 8, 6, 11, 3, 7, 9]; calif_ord = [0,0,0,0,0,0]
print("calif", calif)

'''for estudiante in range(6):
    print("Dame las calificaciones: ")
    calif.append(float(input()))
'''

print(calif)
for paso in range(6):
    minima = 0
    for estudiante in range(1, 6):
        if(calif[estudiante] < calif[minima]):
            minima = estudiante
        calif_ord[paso] = calif[minima]
        calif[minima] = 11

print("El orden es: \n")
print(calif_ord)

