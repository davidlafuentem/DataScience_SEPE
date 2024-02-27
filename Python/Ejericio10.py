##  Ejercicio 10 - Condición IF anidada         ##
##  Realizar un programa que pida al            ##
##  usuario el momento del día con una letra    ##
##  (m-mañana, t-tarde, n-noche), el sexo       ##
##  (m-masculino, f-femenino).                  ##
##  dirá: buenos días, tardes, o noches         ##
##  (según el momento) señor o señora           ##
##  (según el sexo).                            ##

print("\n")

while True:
    momento = input("Introduzca el momento del día (m-t-n): ")
    if momento.isalpha and (momento == "m" or momento == "t" or momento == "n") :
        break

while True:
    genero = input("Introduzca su genero (m-f): ")
    if genero.isalpha and (genero == "m" or genero == "f"):
        break

if momento == "m":
    momento = "Buenos días"
elif momento == "t":
    momento = "Buenas tardes"
elif momento == "n":
    momento = "Buenas noches"

if genero == "m":
    genero = "señor"
elif genero == "f":
    genero = "señora"

print("   "+momento+" "+genero+"!!!")

