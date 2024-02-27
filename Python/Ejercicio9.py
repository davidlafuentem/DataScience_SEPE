##  Ejercicio 09 - Condición IF básica          ##
##  Realizar un programa que pida al            ##
##  usuario tres números y diga cuál            ##
##  es el mayor y cuál el menor, y              ##
##  además cuáles son pares y cuáles impares.   ##

while True:
    numero1 = input("Introduzca el primer número: ")
    if numero1.isdigit():
        numero1 = int(numero1)
        break

while True:
    numero2 = input("Introduzca el segundo número: ")
    if numero2.isdigit():
        numero2 = int(numero2)
        break

while True:
    numero3 = input("Introduzca el tercer número: ")
    if numero3.isdigit():
        numero3 = int(numero3)
        break

#Sólo puede haber un único mayor número
if numero2 != numero1 and numero2 != numero3:
    if numero1 > numero2 and numero1 > numero3:
        print("   El primer número es el mayor")
    elif numero2 > numero1 and numero2 > numero3:
        print("   El segundo número es el mayor")
    elif numero3 > numero1 and numero3 > numero2:
        print("   El tercer número es el mayor")

#Algún numero es idéntico a otro
elif numero1 == numero2:
    if numero1 > numero3:
        print("   El primero y el segundo número son mayores que el tercero número")
    elif numero1 < numero3:
        print("   El tercer número es mayor que el primer y el segundo número")
elif numero2 == numero3:
    if numero1 > numero3:
        print("   El primer número es mayor que el segundo y el tercer número")
    elif numero1 < numero3:
        print("   El segundo y el tercer número son mayores que el primero")
elif numero1 == numero3:
    if numero1 > numero2:
        print("   El primero y el tercer número son mayores que el segundo número")
elif numero1 < numero2:
        print("   El segundo número es mayor que el primer y el tercer número")


if not(numero1 % 2):
    print("   El primer número es par")
else:
    print("   El primer número es inpar")
if not(numero2 % 2):
    print("   El segundo número es par")
else:
    print("   El segundo número es inpar")    
if not(numero3 % 2):
    print("   El tercer número es par")
else:
    print("   El tercer número es inpar")