##  Ejercicio 25 - Bucles FOR  ##
# Realizar un programa USANDO LA SENTENCIA FOR que imprima por pantalla tantos asteriscos 
# como diga el usuario, siendo un numero entero positivo distinto de 0. 
# Al ejecutarse debe preguntar “Cuantos asteriscos desea imprimir?”, 
# leer el número que introduce el usuario e imprimir los asteriscos en HORIZONTAL en el terminal.

entrada = 0
indice = 0

while (entrada <= 0):
    entrada = int(input("Cuántos asteriscos quiere imprimir: "))

for i in range(entrada):
    print("* ",end="")

print("\n")