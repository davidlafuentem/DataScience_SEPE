##  Ejercicio 23 - Mostrar calificación WHILE con IF  ##
""" Escribir un programa que pida por teclado una nota de evaluación admitiendo decimales. 
La nota podrá ser decimal, no inferior a 0 ni superior a 10, redondeada a dos decimales. 
Si no cumple los requisitos el programa seguirá pidiendo una nota. 
Cuando se introduzca un valor entre 0 y 10 se mostrará la calificación según la nota:

0 - 2,99: Muy deficiente
3 - 4,99: Insuficiente
5 - 5,99: Suficiente
6 - 7’99: Bien
8 - 8,99: Notable
9 - 10: Sobresaliente """

testigo = True
while testigo == True:
    testigo = False
    numero1 = float(input("Introduzca la nota de calificación (se admiten decimales): "))
    if numero1 < 0 and numero1 > 10:
        testigo = True

if numero1 >= 0 and numero1 <= 2.99:
    print("Muy deficiente chaval!")
elif numero1 >= 3 and numero1 <= 4.99:
    print("Insuficiente chaval!")
elif numero1 >= 5 and numero1 <= 5.99:
    print("Suficiente!")
elif numero1 >= 6 and numero1 <= 7.99:
    print("Bien!")
elif numero1 >= 8 and numero1 <= 8.99:
    print("Notable!")
elif numero1 >= 9 and numero1 <= 10:
    print("Sobresaliente chaval!")



