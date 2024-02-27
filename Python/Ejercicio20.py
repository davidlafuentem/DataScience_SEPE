##   Ejercicio 20 - Manipular cadenas de caracteres   ##
nombre = ""
apellidos = ""


while not(nombre.isalpha()) and len(nombre) == 0:
    nombre = input("Introduzca su nombre: ").lower()

while not(apellidos.isalpha()) and len(apellidos) == 0:
    apellidos = input("Introduzca sus apellidos: ").lower()


print(nombre + " " + apellidos)
print(nombre.upper() + " " + apellidos.upper())

# apellidos = apellidos.capitalize()
# posicion = apellidos.find(" ")
# apellidos = apellidos[:posicion+1] + apellidos[posicion+1].upper() + apellidos[posicion+2:]

apellidos = apellidos.split(" ")
apellidos = apellidos[0].capitalize() + " " + apellidos[1].capitalize()

print(nombre.capitalize() + " " + apellidos)
