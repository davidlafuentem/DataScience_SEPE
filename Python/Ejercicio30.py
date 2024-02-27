##   Ejercicio 30 - Array de cuadrados perfectos   ##
# Realizar un programa que genere un array de N posiciones. Pedirá un primer número N para saber que tamaño debe tener. 
# Rellenarlo con los N primeros números enteros que formen la serie numérica de cuadrados perfectos (1, 4, 9, 16, 25, 36, ...). 
# A continuación el programa pedirá un segundo número y deberá ofrecer los siguientes resultados:
# Si el segundo número es menor de 1 o mayor del número máximo que hay en el array, el programa mostrará el mensaje 
# "Ese número esta fuera del array".  Si el número está dentro del rango de los números del array habrá que determinar 
# si es un cuadrado perfecto o no. Si es un cuadrado perfecto el programa mostrará el mensaje “El número es un cuadrado perfecto”.
# Si el número NO es un cuadrado perfecto el programa mostrará el mensaje “El número NO es un cuadrado perfecto”.
# Una vez generado el array imprimir su contenido EN HORIZONTAL para comprobar que los números que contiene son correctos.

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
length = 0
number = 0
collection = []
message = ""
flag = True

print("###############################     Ejercicio 30  -- Array de cuadrados perfectos   ###############################")

while flag == True:
    flag = False
    length = 0

    while length == 0 or length < 2:
        print("Introducir longitud del array. Mínimo 2")
        length = prompt_int()   

    collection.clear()  #Asegurar array limpio

    for i in range(length+1): 
        if i:   #Asegurar no guardar el 0
            collection.append(i**2)

    print("Introducir el número a detectar dentro del array.")
    number = prompt_int() ##Introducir el número a detectar dentro del array

    if number == 0 or number > max(collection):
        message = "Ese número esta fuera del array"
    else: 
        if number > 0 and number <= max(collection):
            message = "   El número está dentro del rango del array"
            if number in collection:
                message = message + "\n   El número es un cuadrado perfecto"
            else:
                message = message + "\n   El número NO es un cuadrado perfecto"

    print(f"{message}\n   ",end="")
    print(", ".join(map(str,collection)))

    if not flag:
        option = prompt_opcion("y","Cálcular el cuadrado perfecto","n","Salir del programa")
        if option == "y":
            flag = True
        elif option == "n":
            flag = False

