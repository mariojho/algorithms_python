''' División diferente de cero 2 '''

checar = False
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

if (b != 0):
    checar = True

if (checar):
    c = a / b 
    print("Resultado: ", c)
