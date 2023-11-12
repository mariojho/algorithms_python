''' Programa: Promedio de calificaciones. Este programa calcula
el promedio de calificaciones de tres alumnos
durante un semestre.'''

No_est = int(input("Dame el número de alumnos: \n"))
No_califs = int(input("Dame el No. de calificaciones por alumno: \n"))

for cont_est in range(No_est):
    print("Dame el nombre del estudiante: ")
    Nombre_est = input()
    contador_calificacion = 1
    suma = 0.0

    while (contador_calificacion <= No_califs):
        print("Dame una calificación: ")
        calificacion = float(input())
        suma = suma + calificacion
        contador_calificacion += 1

    promedio = suma / No_califs
    print("Promedio del estudiate: ", Nombre_est, "es: ", promedio)