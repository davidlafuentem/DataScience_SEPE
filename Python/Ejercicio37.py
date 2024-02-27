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
def prompt_int(minimum,maximum):
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca número (entero): ")
        if entrada != "" and entrada.isnumeric() and int(entrada) >= minimum and int(entrada) <= maximum:
            return int(entrada)
        else:
            testigo = True

# Get a integer text
def prompt_string():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca texto: ")
        if entrada != "" and entrada.isalpha():
            return entrada
        else:
            testigo = True


##################################      MAIN      ##################################
system("clear")   #Clear shell

print("###############################      Ejercicio37      ###############################")

carpeta = r"C:\Proyectos_David\ficheros"
#carpeta = "C:\Proyectos_David\\ficheros"   #it also works
fichero = "alumnos.txt"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

# Para pasar cada línea de un fichero a un array
datos = list()  # Inicializamos el array de destino

with open(ruta, mode="r") as archivo:   
    contenido=archivo.readlines()
 
    for linea in contenido:
        numcamp = linea.count("\t")
        registro = linea.replace('\n', '')
        datos.append(registro.split("\t"))

longitud = len(contenido)       # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste


print("Introduzca un rango de edad para el filtrado")
print("Rango inferior")
rango_inferior = str(prompt_int(20,100)) 
print("Rango superior")
rango_superior = str(prompt_int(20,100)) 
print("Introduzca el nombre de la provincia.")
provincia = prompt_string()

casos = []  # index of cases that match age range and province
for i in range(longitud):
    if (datos[i][2]>=rango_inferior and datos[i][2]<=rango_superior):   #3th column is age
        if(datos[i][4]==provincia):
            casos.append(i) # Include index position of positive match case

if len(casos) > 0:  # If exist at least one match case of age and province
    carpeta = r"C:\Proyectos_David\ficheros"
    fichero = "resultado.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)

    linea = ""  # Line to be created with array fields and saved into the file 
    with open(ruta, mode="w") as salida:
        for caso in casos:    # For each array
            linea = ""
            for campo in datos[caso]:   #take each value in array
                linea = linea + campo + "\t"    #Create a line with tab separated values
            linea = linea[:-1]+"\n" #Change the las "\t" by "\n" to create the next new line
            salida.write(linea)
    

