''' Promedio de calificaciones 1 '''

suma = 0; notas = [None] * 20 

print("¿Número de alumnos?: ")
N = int(input())
for i in range(N):
    print("Alumno", i + 1, "Nota: ")
    notas[i] = float(input())

for i in range(N):
    suma = suma + notas[i]

media = suma / N
print("Nota media: ", media)
print("Notas superiores")
for i in range(N):
    if(notas[i] > media):
        print("Alumno número: ", i + 1)
        print("Nota: ", notas[i])