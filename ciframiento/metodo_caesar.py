''' Método de ciframiento Caesar '''
digito = 0; desplazamiento = 0; 

digito = int(input("Ingrese el dígito a cifrar: "))
desplazamiento = int(input("Ingrese el desplazamiento: "))

if digito >= 0 and desplazamiento >= 0:
    digito_cifrado = (digito + desplazamiento) % 10
    print("El dígito cifrado es: ", digito_cifrado)
else:
    print("El dígito y el desplazamiento deben ser mayores o iguales a cero")
    