##  Ejercicio 38 - Análisis de datos en tablas grandes (actividad de evaluación)
# Se entrega un fichero CSV llamado "poblacion.csv". Importar los datos (salvo el encabezado) a una
# tabla en Python y realizar el siguiente análisis de datos:
# Número de municipios de la provincia con mar (mun_mar)
# Número de municipios con más de 15.000 habitantes (mun_15k)
# Suma total de playas de la provincia (sum_playas)
# Suma total de habitantes que viven en municipios costeros (poblacion_mar)
# Suma total de los habitantes que viven en municipios de menos de 5.000 habitantes (poblacion_5k)
# Suma total de kilómetros de costa de la provincia (kilometros_mar)
# Suma total de viviendas en pueblos costeros. (viviendas_mar)
# Densidad de población en costa (Viviendas en costa / habitantes en costa) (den_costa)
# Densidad de población en no costeros (Viviendas en no costeros / habitantes en no costeros) (den_no_mar)
# Diseñar el programa necesario para realizar los cálculos que se piden y los guarde en un fichero 
# llamado "resultados.txt"
# Guardar los documentos .TXT y el programa .PY en tu carpeta como Ejercicio 38.



import os
import random
from os import system

###############################      FUNCIONES      ###############################
##################################      MAIN      ##################################
system("cls")   #Clear shell

print("###############################      Ejercicio38      ###############################")

#carpeta = r"C:\Proyectos_David\ficheros"
carpeta = r"D:\Curso Data Science 2023\ficheros"
#carpeta= "/Users/DLF/Curso Data Science 2023/ficheros"
#carpeta = "C:\Proyectos_David\\ficheros"   #it also works
fichero = "poblacion.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

# Para pasar cada línea de un fichero a un array
datos = list()  # Inicializamos el array de destino
longitud = 0
numcamp = 0

try:
    with open(ruta, mode="r",encoding="latin-1") as archivo:   
        contenido=archivo.readlines()
 
        for linea in contenido:
            numcamp = linea.count(";")
            registro = linea.replace('\n', '')
            datos.append(registro.split(";"))
        longitud = len(contenido)       # Numero de filas
        numcamp += 1                    # Numero de columnas con ajuste
except(FileNotFoundError) as error:
    print(error)
    print("Compruebe si el fichero existe en la ruta")
    os._exit()

# Transformación de los datos
# Eliminiar primer registro (encabezados)
#datos.pop(0)
datos.remove(datos[0])
longitud = len(datos)
   
# Cambiar las columnas a tipo numéricas
for i in range(longitud):
        datos[i][2] = float((datos[i][2]).replace(",","."))
        datos[i][3] = int(datos[i][3])
        datos[i][4] = int(datos[i][4])
        datos[i][5] = int(datos[i][5])
        datos[i][6] = int(datos[i][6])
        datos[i][7] = int(datos[i][7])


 # Número de municipios de la provincia con mar (num_mar)
num_mar = 0
for i in range(longitud):
    if datos[i][2]>0:
        num_mar += 1

# Número de municipios con más de 15.000 habitantes (mun_15k)
num_15k = 0
for i in range(longitud):
    if datos[i][7]> 15000:
        num_15k += 1

# Suma total de playas de la provincia (sum_playas)
sum_playas = 0
for i in range(longitud):
    if datos[i][3]> 0:
        sum_playas = sum_playas + datos[i][3]

# Suma total de habitantes que viven en municipios costeros (poblacion_mar)
poblacion_mar = 0
for i in range(longitud):
    if datos[i][2]>0:
        poblacion_mar = poblacion_mar + datos[i][7]

# Suma total de los habitantes que viven en municipios de menos de 5.000 habitantes (poblacion_5k)
poblacion_5k = 0
for i in range(longitud):
    if datos[i][7]< 5000:
        poblacion_5k = poblacion_5k + datos[i][7]

# Suma total de kilómetros de costa de la provincia (kilometros_mar)
kilometros_mar = 0
for i in range(longitud):
    if datos[i][2]> 0:
        kilometros_mar = kilometros_mar + datos[i][2]

# Suma total de viviendas en pueblos costeros. (viviendas_mar)
viviendas_mar = 0
for i in range(longitud):
    if datos[i][2]> 0:
        viviendas_mar = viviendas_mar + datos[i][4]

# Densidad de población en costa (Viviendas en costa / habitantes en costa) (den_costa)
den_costa = viviendas_mar / poblacion_mar

# Densidad de población en no costeros (Viviendas en no costeros / habitantes en no costeros) (den_no_mar)
poblacion = 0
viviendas = 0
for i in range(longitud):
    poblacion = poblacion + datos[i][7]
    viviendas = viviendas + datos[i][4]

den_no_mar = (viviendas-viviendas_mar) / (poblacion - poblacion_mar)

print(f"##DATOS A GUARDAR EN EL FICHERO {fichero}##")
print(f"    Municipios costeros: {num_mar}")
print(f"    Municipios +15K: {num_15k}")
print(f"    Total playas: {sum_playas}")
print(f"    Población costera: {poblacion_mar}")
print(f"    Población municipios -5K: {poblacion_5k}")
print(f"    Total kilometros costa: {kilometros_mar}")
print(f"    Total viviendas costeras: {viviendas_mar}")
print(f"    Densidad población costera: {den_costa}")
print(f"    Densidad población no costera: {den_no_mar}")

#carpeta = r"C:\Proyectos_David\ficheros"
carpeta=r"D:\Curso Data Science 2023\ficheros"
#carpeta="/Users/DLF/Curso Data Science 2023/ficheros/"
fichero = "resultado.txt"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

try:
    with open(ruta, mode="x",encoding="latin-1") as salida:
        linea = ""
        #linea =  f" Municipios costeros: {num_mar}\n"+f"    Total kilometros costa: {kilometros_mar}\n"+f"  Municipios +15K: {num_15k}\n"+f"    Total playas: {sum_playas}\n"+f"    Población costera: {poblacion_mar}\n"+f"    Población municipios -5K: {poblacion_5k}\n"+f"    Total kilometros costa: {kilometros_mar}\n"+f"    Total kilometros costa: {kilometros_mar}\n"+f"    Total viviendas costeras: {viviendas_mar}\n"+f"    Densidad población costera: {den_costa}\n"+f"    Densidad población no costera: {den_no_mar}\n"
        linea = f"   Municipios costeros: {num_mar}\n    Total kilometros costa: {kilometros_mar}\n"\
        f"    Municipios +15K: {num_15k}\n    Total playas: {sum_playas}\n"\
        f"    Población costera: {poblacion_mar}\n    Población municipios -5K: {poblacion_5k}\n"\
        f"    Total kilometros costa: {kilometros_mar}\n    Total viviendas costeras: {viviendas_mar}\n"\
        f"    Densidad población costera: {den_costa}\n    Densidad población no costera: {den_no_mar}\n"
        salida.write(linea)

except (FileExistsError) as error:  # if file already exists
    #print(error)
    with open(ruta, mode="a+",encoding="latin-1") as salida:   #open in append mode
        linea = ""
        linea = f"    Municipios costeros: {num_mar}\n    Total kilometros costa: {kilometros_mar}\n"\
        f"    Municipios +15K: {num_15k}\n    Total playas: {sum_playas}\n"\
        f"    Población costera: {poblacion_mar}\n    Población municipios -5K: {poblacion_5k}\n"\
        f"    Total kilometros costa: {kilometros_mar}\n    Total viviendas costeras: {viviendas_mar}\n"\
        f"    Densidad población costera: {den_costa}\n    Densidad población no costera: {den_no_mar}\n"
        salida.write(linea)