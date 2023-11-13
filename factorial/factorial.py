''' Encontrar el factorial de un número entero positivo'''

factorial_de_n = 1
print("Dame el valor del entero n: \n")
n = int(input())

for k in range(2, n + 1):
    factorial_de_n = factorial_de_n * k
    print(factorial_de_n)
    print("\n")
    
print("El factorial es: ", factorial_de_n)