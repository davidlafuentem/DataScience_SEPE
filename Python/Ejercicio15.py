##   Ejercicio 15 - Control de errores   ##
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división redondeada
# a dos decimales. los números podrán ser decimales. Si el divisor es cero el programa debe mostrar
# un mensaje de error.

###############################      FUNCIONES      ###############################
def prompt_int():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("Introduzca número (entero): ")
        if entrada != "":
            if entrada.isalnum:
                return int(entrada)
        else:
            testigo = True


def prompt_float():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("Introduzca número (decimal): ")
        if entrada != "":
            if entrada.isalnum:
                return float(entrada)
        else:
            testigo = True



###############################      MAIN      ###############################
numero1 = prompt_float()
numero2 = prompt_float()

if numero2 == 0:
    print("ERROR!!!  ERROR!!!")
else:
    print(round(numero1/numero2,2))