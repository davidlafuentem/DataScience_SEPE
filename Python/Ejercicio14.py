##   Ejercicio 14 - Cambio de datos  ##
# Realizar un programa que pida por pantalla un nombre de usuario y una contraseña. 
# A continuación se le preguntará qué datos quiere cambiar mediante una letra. 
# Si elige la letra n se cambiará el nombre, si elige la letra c se cambiará la contraseña, 
# y si elige la letra t se cambiará tanto el nombre como la contraseña. 
# Al final del programa se mostrarán tanto el nombre y la contraseña originales como los cambiados.



###############################      FUNCIONES      ###############################
def prompt_name():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("Introduzca su nombre: ")
        if entrada != "":
            if entrada.isalpha:
                return entrada
        else:
            testigo = True

def prompt_contraseña():
    testigo = True
    while(testigo == True):
        testigo = False
        entrada = input("Introduzca una contraseña: ")
        if entrada != "":
            testigo = False
            return entrada
        else:
            testigo = True

def prompt_opcion(a,mensaje_a,b,mensaje_b,c,mensaje_c):
    testigo = True
    while testigo == True:
        testigo = False
        #print(f"Escoja la opción, {mensaje_a} o {mensaje_b} o {mensaje_c} ({a}-{b}-{c})")
        entrada = input(f"Escoja la opción, {mensaje_a} o {mensaje_b} o {mensaje_c} ({a}-{b}-{c}): ")
        if not entrada.isalpha or entrada ==  "" and (entrada != a or entrada != b or entrada != c):
            testigo = True
        else:
            return entrada


###############################      MAIN      ###############################
nombre = ""
contraseña = ""
nombre_def = ""
contraseña_def = ""
opcion = ""

 
nombre = prompt_name()
contraseña = prompt_contraseña()
opcion = prompt_opcion("n","cambiar nombre","c","cambiar contraseña","t","cambiar ambos")

if opcion == "n":
    nombre_def = prompt_name()
    print(f"Nombre original: {nombre}\nNombre definitivo: {nombre_def}")
elif opcion == "c":
    contraseña_def = prompt_contraseña()
    print(f"Contraseña original: {contraseña}\nContraseña definitiva: {contraseña_def}")
elif opcion == "t":
    nombre_def = prompt_name()
    contraseña_def = prompt_contraseña()
    print(f"Nombre original: {nombre}\nNombre definitivo: {nombre_def}")
    print(f"Contraseña original: {contraseña}\nContraseña definitiva: {contraseña_def}")
