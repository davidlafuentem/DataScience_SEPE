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

coma = 0
cadena = []

testigo = True
while testigo == True:
    testigo = False
    entrada = input("Introduzca la nota de calificación (se admiten decimales): ")

    for i,charac in enumerate(entrada):
        if charac=='.' or charac==',':
            if i == 0:  # Incorrecto: signo decimal en primera posición 
                testigo = True
                break
            elif i > 0: # Correcto: signo decimal no en primera posición
                if coma == 0:
                    coma = i    # Guardo posición del signo decimal
                elif coma != 0:  # Incorrecto: Más de un sigo decimal
                    testigo = True
                    coma = 0
                    break
        #elif ord(charac) < 48  or ord(charac) > 57:
        elif charac < '0'  or charac > '9':            
            testigo = True
            coma = 0
            break
            
    if i == len(entrada)-1 and not testigo:   #Si ha llegado al final de la cadena, esta es correcta
        cadena = list(entrada)
        cadena[coma]='.'   #Asegura que signo decimal es correcto
        entrada = "".join(cadena)
        if float(entrada) < 0 and float(entrada) > 10:  #Si número no está entre 0 y 10
            testigo = True
            coma = 0

numero = float(entrada)
if numero >= 0 and numero <= 2.99:
    print("Muy deficiente chaval!")
elif numero >= 3 and numero <= 4.99:
    print("Insuficiente chaval!")
elif numero >= 5 and numero <= 5.99:
    print("Suficiente!")
elif numero >= 6 and numero <= 7.99:
    print("Bien!")
elif numero >= 8 and numero <= 8.99:
    print("Notable!")
elif numero >= 9 and numero <= 10:
    print("Sobresaliente chaval!")



