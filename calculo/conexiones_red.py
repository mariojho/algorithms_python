''' Cálculo número total de conexiones entre los servidores de una red '''
n = 0; conexiones = 0

n = int(input("Dame el número de servidores de la red: "))
conexiones = (n * (n - 1)) / 2

print("El número total de conexiones entre los servidores de la red es: ", conexiones, "\n")