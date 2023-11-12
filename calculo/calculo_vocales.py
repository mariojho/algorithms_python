''' Programa: Calcula el número de vocales en una frase. '''

frase = "El perro corre despacio"
base = "aeiouAEIOU"
cuenta = 0

for i in frase: 
    if i in base: 
        cuenta = cuenta + 1

print("El número de vocales es: ", cuenta)