##   Ejercicio 27 - Juego del Oráculo y el Adivino   ###
""" Realizar un programa en el cual un usuario Oráculo introduzca un número entero al azar entre 1 y 20. 
Si no cumple los requisitos el programa seguirá pidiendo un número. A continuación otro usuario 
Adivino deberá averiguar cuál es ese número, teniendo 5 oportunidades para acertarlo.
Si el Adivino mete un número menor el programa responderá “El número que buscas es mayor”. 
Si mete un número mayor el programa responderá “El número que buscas es menor”. 
Si averigua el número saldrá el mensaje “¡Enhorabuena, acertaste, es el número X!”. 
Si no lo averigua después de 5 intentos saldrá el mensaje “¡Oh, lo siento, era el número X!”. """
import random

numero = 0
oraculo = 0
testigo = True
oraculo = random.randint(1,20)

print("\n   ",oraculo)

for i in range(5):
    print("Tienes",5-i,"oportunidades de encontrar el número aleatorio entre 1 y 20")
    while (testigo == True):
        testigo = False
        entrada = input("Introduzca un número entero entre 1 y 20, y mucha suerte: ")
        if entrada != "":
            if entrada.isalnum:
                numero = int(entrada)
                if numero < 1 or numero > 20:
                    testigo = True
                else:
                    testigo = False
        else:
            testigo = True
        
    if(numero == oraculo):
        print("   HA GANADO!!!")
        testigo = False
        break
    elif(numero > oraculo):
        print("   Su número es mayor.  Vuelva a intentarlo")        
        testigo = True
    elif(numero < oraculo):
        print("   Su número es menor.  Vuelva a intentarlo")
        testigo = True

if testigo:
    print("HAS PERDIDO!!!  MUAHAHAHA")    




