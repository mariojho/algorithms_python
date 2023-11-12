''' Ecuación de primer grado 2 '''

a = float(input("Dame a: "))
b = float(input("Dame b: "))
if (a != 0):
    x = -b / a
    print(x)
else:
    if (b == 0):
        print("a = 0 y b = 0")
    else:
        print("No hay solución.")