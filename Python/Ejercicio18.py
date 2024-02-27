##   Ejercicio 18 - Condicionales con caracteres  ###

while True:
    nombre = input("Introduzca su nombre: ").lower()
    if nombre.isalpha and len(nombre) > 0:
        inicial = nombre[0]    
        break

while True:
    genero = input("Introduzca su género, másculino o femenino (m-f): ").lower()
    if genero.isalpha and len(genero) == 1 and (genero == "m" or genero == "f"):
        break

print("Nombre es ",nombre.capitalize()," y su género es",genero.capitalize())

if (inicial >= "n" and nombre == "f") or (inicial <= "m" and nombre == "m"):
    print("Su grupo es el A")
else:
    print("Su grupo es el B")
