''' Cálculo de la resistencia total de dos resistores conectados en paralelo '''

resistencia1 = 0; resistencia2 = 0; resistencia_total = 0

resistencia1 = float(input("Ingrese el valor de la resistencia 1: "))
resistencia2 = float(input("Ingrese el valor de la resistencia 2: "))

if resistencia1 > 0 and resistencia2 > 0:
    resistencia_total = 1 / ((1 / resistencia1) + (1 / resistencia2))
    print("La resistencia total de dos resistores conectados en paralelo es: ", resistencia_total)