##   Ejercicio 22 - Bucles WHILE   ##
""" I. Realizar un programa que pida al usuario dos números enteros positivos distintos,
e imprima EN HORIZONTAL los números del número mas pequeño al número más alto que introdujo el usuario. """

testigo = True
while testigo == True:
    testigo = False
    numero1 = input("Introduzca el primer número: ")
    if not numero1.isalnum or numero1 == 48:
        testigo = True

testigo = True
while testigo == True:
    testigo = False
    numero2 = input("Introduzca un segundo número, diferente al primero: ")
    if not numero1.isalnum or numero2 == 48 or numero2 == numero1:
        testigo = True

numero1 = int(numero1)
numero2 = int(numero2)

#Delimita el bucle según magnitud de los números
if numero1 < numero2:
    indice = numero1
    final = numero2
else:
    indice = numero2
    final = numero1

while (indice <= final):
    print(indice,", ",end="")
    indice += 1

print("\b\b",end="")    #Borra últimos 2 carácteres
