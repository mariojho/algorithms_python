''' Calificaciones con condición múltiple '''

calificacion = float(input("Dame una calificación: \n"))
print("Dame la asistencia: 1 si asistió ó 0 si no asistió")
asistencia = int(input())

if (calificacion > 9.0 and asistencia == 1):
    print("La calificación es A excelente con Mención Honorífica.")
elif(calificacion > 9.0 and asistencia != 1):
    print("La calificación es A excelente.")
elif(calificacion > 8.0 and asistencia == 1):
    print("La calificación B Muy bien con Mención.")
elif(calificacion > 8.0 and asistencia != 1):
    print("La calificación es B Muy bien.")
elif(calificacion == 7.5):
    print("La calificación es C Bien.")
else:
    print("La calificación es R Reprobado. Lo siento mucho.")