''' Algoritmo de Fibonacci.
Genera la secuencia de Fibonacci con 10 iteraciones '''

fib = []
fib[0:1] = [0, 1]
for k in range(2, 10):
    fib.append(fib[k - 1] + fib[k - 2])

print(fib)