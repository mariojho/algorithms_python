''' Cálculo del número de metros cúbicos contaminados por una pila '''

millones_usuarios = 0; millones_cubicos_contaminadoos = 0; pilas = 4; metros_cubicos = 175

millones_usuarios = int(input("Ingrese el número de millones de usuarios: "))

if millones_usuarios > 0:
    millones_cubicos_contaminadoos = millones_usuarios * metros_cubicos * pilas
    print("El número de metros cúbicos contaminados por una pila es: ", metros_cubicos)
else:
    print("El número de millones de usuarios debe ser mayor a cero")
