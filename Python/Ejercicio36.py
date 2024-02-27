##  Ejercicio 36 - Importar ficheros de datos   ###
##  Se entrega un fichero de datos llamado "alumnos.txt". Importar el fichero a una tabla
##  en Python y realizar los siguientes  cálculos:
##  Edad media de los alumnos mayores de 18 años y menores de 65 (incluyendo 18 y 65).
##  Número de alumnos de Madrid, Guadalajara y Soria, indicando cada valor por separado.
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


##################################      MAIN      ##################################
system("clear")   #Clear shell

print("###############################      Ejercicio36      ###############################")

carpeta = r"C:\Proyectos DLafuente\ficheros"
#carpeta = "C:\Proyectos DLafuente\\ficheros"   #it also works
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


for i in range(longitud):       # Podemos dibujar asi el contenido del array
    linea = "\t"
    for j in range(numcamp):
        if(j == 2):
            datos[i][j] = int(datos[i][j])
        linea = linea + str(datos[i][j]) + "\t"
    print(linea + "\n")


edad_media= 0
casos = 0
for i in range(longitud):
    if (datos[i][2]>=18 and datos[i][2]<=65):
        edad_media = edad_media + datos[i][2]
        casos += 1

edad_media = round(edad_media / casos,2)
print(f"La edad media es: {edad_media}")


casos = 0
alumnos_madrid = 0
alumnos_guadalajara = 0
alumnos_soria = 0

for i in range(longitud):
    if (datos[i][4]=="Madrid"):
        alumnos_madrid += 1
    elif (datos[i][4]=="Guadalajara"):
        alumnos_guadalajara += 1
    elif (datos[i][4]=="Soria"):
        alumnos_soria += 1

print(f"Hay {alumnos_madrid} alumnos de Madrid")
print(f"Hay {alumnos_guadalajara} alumnos de Guadalaja")
print(f"Hay {alumnos_soria} alumnos de Soria")


