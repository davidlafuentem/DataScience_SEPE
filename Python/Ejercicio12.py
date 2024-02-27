##  Ejercicio 12 - Condición SWITCH (MATCH)     ##

print("\n")

while True:
    momento = input("Introduzca el momento del día (m-t-n): ")
    if momento.isalpha and (momento == "m" or momento == "t" or momento == "n") :
        break

while True:
    genero = input("Introduzca su genero (m-f): ")
    if genero.isalpha and (genero == "m" or genero == "f"):
        break
match momento:
    case "m":
        momento = "Buenos días"
    case "t":
        momento = "Buenas tardes"
    case "n":
        momento = "Buenas noches"

match genero:
    case "m":
        genero = "señor"
    case "f":
        genero = "señora"
        
print("   "+momento+" "+genero+"!!!")

