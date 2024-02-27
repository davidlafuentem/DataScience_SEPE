##  Ejercicio 28 - Listado de números pares o impares  ##
# Realizar un programa que pida al usuario dos números y una letra: “i” ó “p”. 
# El programa presentará los números pares (si se pulsó la “p”) ó impares (si se pulsó la “i”) 
# que hay desde el primer número al segundo que introdujo el usuario. 
# Si se pulsa alguna tecla distinta de “p” ó “i”, el programa no imprime ningún número.


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

testigo = True
while testigo == True:
    testigo = False
    entrada = input("Escoja el tipo de números a mostrar, par o impar (p-i): ")
    if not entrada.isalpha or entrada ==  "" and (entrada != 'p' or entrada != 'i'):
        testigo = True
    else:
        opcion = entrada


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
    if opcion == 'p':
        if indice %2 == 0:  ##  Este es par
            print(indice,", ",end="")
    elif opcion == 'i':
        if indice %2 !=0:
            print(indice,", ",end="")       
    indice += 1

print("\b\b",end="")    #Borra últimos 2 carácteres
