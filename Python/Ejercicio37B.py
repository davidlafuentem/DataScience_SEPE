##  Ejercicio 37 - Exportar ficheros de datos  ##
##  Se entrega un fichero de datos llamado "alumnos.txt". Importar el fichero a una tabla en Python.
##  A continuación solicitar al operador los siguientes datos:
##  Rango de Edad: dos valores numéricos enteros que nos delimiten el rango de edad.
##  Provincia: dos provincias en la que buscaremos el rango de edad.
##  Se trata de generar un filtro a través de la edad y dos provincias. Si en la tabla existen 
##  registros que cumplan las condiciones, los datos encontrados se copiaran a un fichero de salida 
##  llamado "resultado.csv". En caso de que no haya registros se mostrará por pantalla el mensaje 
##  "No hay registros con ese filtro".
##  Guardar los documento .TXT y el programa .PY en tu carpeta como Ejercicio 36.


import os
import random
from os import system

###############################      FUNCIONES      ###############################
# Get a integer number between min and max
def prompt_int():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca número (entero): ")
        if entrada != "" and entrada.isnumeric():
            return int(entrada)
        else:
            testigo = True

# Get a text
def prompt_text():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca texto: ")
        if entrada != "" and entrada.isalpha():
            return entrada
        else:
            testigo = True

# Ask for an option
def prompt_opcion(a,mensaje_a,b,mensaje_b):
    testigo = True
    while testigo == True:
        testigo = False
        entrada = input(f"Escoja la opción, {mensaje_a} o {mensaje_b} ({a}-{b}): ")
        if (entrada.isalpha() or entrada !=  "") and (entrada == a or entrada == b):
            return entrada
        else:
            testigo = True


##################################      MAIN      ##################################
system("cls")   #Clear shell

print("###############################      Ejercicio37      ###############################")

carpeta = r"C:\Proyectos_David\ficheros"
#carpeta = r"D:\Curso Data Science 2023\ficheros"
#carpeta= "/Users/DLF/Curso Data Science 2023/ficheros"
#carpeta = "C:\Proyectos_David\\ficheros"   #it also works
fichero = "alumnos.txt"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

# Para pasar cada línea de un fichero a un array
datos = list()  # Inicializamos el array de destino

with open(ruta, mode="r",encoding="latin-1") as archivo:   
    contenido=archivo.readlines()
 
    for linea in contenido:
        numcamp = linea.count("\t")
        registro = linea.replace('\n', '')
        datos.append(registro.split("\t"))

longitud = len(contenido)       # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste

keep = True
while(keep):
    keep = False
    
    print("Introduzca un rango de edad para el filtrado")
    print("Rango inferior")
    rango_inferior = str(prompt_int()) 
    print("Rango superior")
    rango_superior = str(prompt_int()) 
    print("Introduzca el nombre de la primera provincia.")
    provincia = prompt_text()
    print("Introduzca el nombre de la segunda provincia.")
    provincia2 = prompt_text()
    

    casos = []  # index of cases that match age range and province
    for i in range(longitud):
        if(datos[i][4]==provincia or datos[i][4]==provincia2):
            if (int(datos[i][2])>=int(rango_inferior) and int(datos[i][2])<=int(rango_superior)):   #3th column is age
                casos.append(i) # Include index position of positive match case

    if len(casos) > 0:  # If exist at least one match case of age and province
        carpeta = r"C:\Proyectos_David\ficheros"
        #carpeta=r"D:\Curso Data Science 2023\ficheros"
        #carpeta="/Users/DLF/Curso Data Science 2023/ficheros/"
        fichero = "resultado.csv"
        ruta = os.path.join(carpeta, fichero)
        ruta = os.path.abspath(ruta)
        
        linea = ""  # Line to be created with array fields and saved into the file 
        try:
            #with open(ruta, mode="x",encoding="latin-1") as salida:
            with open(ruta, mode="x",encoding="latin-1") as salida:
                for caso in casos:    # For each array
                    linea = ""
                    for campo in datos[caso]:   #take each value in array
                        linea = linea + campo + "\t"    #Create a line with tab separated values
                    linea = linea[:-1]+"\n" #Change the las "\t" by "\n" to create the next new line
                    salida.write(linea) # Write into the file
                print(f"Se han escrito en el fichero {len(casos)} registros")
        except (FileExistsError) as error:  # if file already exists
            #print(error)
            with open(ruta, mode="a+",encoding="latin-1") as salida:   #open in append mode
                for caso in casos:    # For each array
                    linea = ""
                    for campo in datos[caso]:   #take each value in array
                        linea = linea + campo + "\t"    #Create a line with tab separated values
                    linea = linea[:-1]+"\n" #Change the las "\t" by "\n" to create the next new line
                    salida.write(linea) # Write into the file
                print(f"Se han escrito en el fichero {len(casos)} registros")
    else:
        print("No hay registros con ese filtro")

    opcion=prompt_opcion("y","volver a filtrar registros (y)","n","salir del programa (n)") #Keep asking new filters?    
    if opcion == "y":
        keep = True
    elif opcion == "n":
        keep = False
    

