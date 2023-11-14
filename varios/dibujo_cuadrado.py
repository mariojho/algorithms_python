''' Este algoritmo dibuja un cuadrado con asteriscos. '''
N = int(input("Escribe la dimesión N >= 2 del cuadrado a dibujar"))

for i in range(N + 1):
    print("* ", end='')

print()

j = 1
while j <= N - 2:
    for k in range(N):
        if k == 0:
            print('*', end = '')
        elif k == N - 1:
            print('  *', end = '')
        else:
            print('  ', end = '')
    print()
    j += 1

i = 0
while i <= N + 1:
    print('* ', end = '')
    i += 1