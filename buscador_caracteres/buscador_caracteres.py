''' Buscador de caracteres. 
Busca cuántas veces el caracter o se encuentra en la palabra colombiano '''

suma = 0
for k in "colombiano":
    if 'o' in k:
        suma = suma + 1
        print("Ganador")

print("Se encuentra", end = "")
print("%5.0f veces " %suma)