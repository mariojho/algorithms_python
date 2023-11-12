''' Calculadora simple en Python'''

from math import log 

bandera = False 

x = float(input("Dame el valor del número x: \n"))
y = float(input("Dame el valor del número y: \n"))

print("Dame la opción que deseas realizar: \n")

print("1) Sumar (El primero más el segundo)")
print("2) Restar (El primero menos el segundo)")
print("3) Multiplicar (El primero por el segundo)")
print("4) Dividir (El primero sobre el segundo)")
print("5) Potencia (El primero a la potencia del segundo)")
print("6) Logaritmo (El logaritmo del primero")

opcion = int(input("Dame la opción: "))

if (opcion == 1):
    z = x + y
    print(x, "+", y)
elif (opcion == 2):
    z = x - y
    print(x, "-", y)
elif(opcion == 3):
    z = x * y
    print(x, "*", y)
elif(opcion == 4 and y != 0):
    z = x / y
    print(x, "/", y)
elif(opcion == 4 and y == 0):
    print("El denominador es igual a cero y")
    print("NO se puede realizar la división")
    bandera = True 
elif(opcion == 5):
    z = pow(x, y)
    print(x, "^", y)
elif(opcion == 6 and x > 0):
    z = log(x)
    print("logaritmo de", x) 
elif(opcion == 6 and x <= 0):
    print("El valor de x es <= a cero y")
    print("NO  se puede calcular el logaritmo.")
    bandera = True 
else:
    print("Opción desconocida")

if (opcion < 7 and bandera == False):
    z = ""
    print("Resultado = ", z)