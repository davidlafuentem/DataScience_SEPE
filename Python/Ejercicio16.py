##   Ejercicio 16 - Calculo de impuestos   ##
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que 
# le corresponde y la cantidad de impuesto que debe pagar. Por ejemplo, si la renta es 10000€ le corresponde 
# un tipo del 15%. El mensaje a mostrar será:
# "Para una renta de 10000€ se le aplica el 15%. 
# El valor del impuesto es 1500€"

###############################      FUNCIONES      ###############################
def prompt_int():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("--- Introduzca número (entero): ")
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


def prompt_opcion(a,mensaje_a,b,mensaje_b):
    testigo = True
    while testigo == True:
        testigo = False
        entrada = input(f"Escoja la opción, {mensaje_a} o {mensaje_b} ({a}-{b}): ")
        if not entrada.isalpha or entrada ==  "" and (entrada != a or entrada != b):
            testigo = True
        else:
            return entrada
###############################      MAIN      ###############################
salary = 0
message = ""
option = ""
flag = True

print("###############################     Ejercicio 16  -- Calculo de impuestos   ###############################")

while flag == True:
    flag == False

    print("Cuál es su renta anual?")
    salary = prompt_int()
    
    if salary == 0 and salary < 10000:
        imposition = salary*0.05
        message = f"   Para una renta de {salary} se le aplica el 5%.\n   El valor del impuesto es {imposition}"
    elif salary >= 10000 and salary < 20000:
        imposition = salary*0.15
        message = f"   Para una renta de {salary} se le aplica el 15%.\n   El valor del impuesto es {imposition}"
    elif salary >= 20000 and salary < 35000:
        imposition = salary*0.20
        message = f"   Para una renta de {salary} se le aplica el 20%.\n   El valor del impuesto es {imposition}"
    elif salary >= 35000 and salary < 60000:
        imposition = salary*0.30
        message = f"   Para una renta de {salary} se le aplica el 30%.\n   El valor del impuesto es {imposition}"
    elif salary >= 60000:
        imposition = salary*0.45
        message = f"   Para una renta de {salary} se le aplica el 45%.\n   El valor del impuesto es {imposition}"

    print(message)

    option = prompt_opcion("y","calcular nueva renta","n","salir del programa de cálculo")
    if option == "y":
        flag = True
    elif option == "n":
        flag = False