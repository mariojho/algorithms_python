''' Ordenamiento de burbuja '''
precio = []

for articulo in range (5):
    print("Dame el precio de un artículo: \n")
    precio.append(float(input()))

hay_cambio = True

while (hay_cambio == True):
    hay_cambio = False 
    for articulo in range(len(precio) - 1):
        if (precio[articulo] > precio[articulo + 1]):
            temp = precio[articulo]
            precio[articulo] = precio[articulo + 1]
            precio[articulo + 1] = temp 
            hay_cambio = True 

print("\n El vector ordenado es: \n")
for articulo in range(5):
    print(precio[articulo], "\n")
