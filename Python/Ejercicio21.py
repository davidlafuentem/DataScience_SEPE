##  Ejercicio 21 - Bucles WHILE   ##

entrada = 0
indice = 0

while (entrada <= 0):
    entrada = int(input("Cuántos asteriscos quiere imprimir: "))

while (indice < entrada):
    print("* ",end="")
    indice += 1
print("\n")