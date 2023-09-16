cadena = input("Ingresa una frase:")

n = input("Ingresa el caracter a buscar:")

j = 0

for i in cadena:

    if n == i:

        j = j + 1

print(f"El caracter {n} se encuentra {j} veces")