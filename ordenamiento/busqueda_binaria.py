''' Búsqueda binaria 
TODO: Hacerlo funcional
'''

vector = [] * 100

n = int(input("Dame el número de elementos en la lista "))
print("Dame n enteros ")
for c in range(n):
    vector.append(int(input()))

numero_buscado = int(input("Dame el valor a buscar: \n"))

primero = 1
ultimo = n 
print("primero", primero, "ultimo", ultimo)
medio = int((primero + ultimo) / 2)
print("medio", medio)

while( primero <= ultimo):
    print("Entrada while")
    if (vector[medio] < numero_buscado):
        print("if")
        primero = medio + 1
        print("Vector[medio]", vector[medio], "numero_buscado", numero_buscado)
        print("primero", primero)
        
    elif(vector[medio] == numero_buscado):
        print("elif")
        print(numero_buscado, " encontrado en la posición")
        print(medio)
        primero = 2 * ultimo
        print("Elif") 
    else:
        print("else")
        ultimo = medio 
        medio = (primero + ultimo) / 2
        print("else")

if(primero > ultimo):
    print("Número no encontrado en la lista \n")