# Ejercicio 44 - Uso de SQL desde Python
# I. Nuestra empresa es una compañía de desarrollo de software. Tiene periodos de sobrecarga de trabajo
# en los que es necesario subcontratar a determinado personal. Las categorías de trabajadores son: 
# Programadores, escritores técnicos y administrativos. De cada una de las personas debemos registrar 
# sus datos básicos (Nombre, dirección…) así como la categoría a la que pertenecen. Como estos 
# colaboradores no están siempre disponibles cuando los necesitemos, incluiremos un campo que registre
# la fecha a partir de la cual el sujeto está disponible para contratarlo. Tendremos que especificar 
# si un contratado está dispuesto a trabajar horas extras y finalmente incluiremos campos que registren
# el precio por hora y las horas trabajadas por cada subcontratado en cada acción para controlar los 
# pagos. Debemos crear las siguiente tablas en MySQL usando un programa de Python:
# Indicar NIF SUB como campo clave.
# II. Crear una segunda tabla con el nombre de Facturación, con las siguientes características:
# El campo CODIGO FAC es el campo clave.
# Crear la siguiente relación:
#                 NIF SUB 1 --> ∞ NIF SUB FAC
# III. Importar del fichero subcontratados.csv los datos que debe contener la tabla SUBCONTRATADOS, 
# y del fichero facturación.csv los datos que debe contener la tabla FACTURACIÓN.
# IV. Realizar las siguientes consultas:
# CONSULTA TOTAL: Muestra TODOS los datos de los trabajadores DE LAS DOS TABLAS, salvo el NIF de 
# Facturación. Ordenar la consulta por APELLIDOS Y HORAS EXTRAS (orden ascendente).
# HORAS MAX: Muestra los datos NIF, NOMBRE, APELLIDOS, CP, POBLACIÓN, HORAS Y FACTURACIÓN de las 
# personas que hayan relizado mas de 100 euros de facturación, ordenados por POBLACIÓN Y FACTURACIÓN 
# (orden ascendente).
# V. Guardar el documento .PY en tu carpeta como Ejercicio 44.

import os
import random
import mysql.connector
from os import system


###############################      FUNCTIONS      ###############################
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



# Get a dni
def prompt_dni():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca texto: ")
        entrada = entrada[:-1]+entrada[-1].upper()
        if entrada != "" and entrada.isalnum and len(entrada)==9:
            return str(entrada)
        else:
            testigo = True



# Ask for an option
def prompt_opcion(a,mensaje_a,b,mensaje_b):
    testigo = True
    while testigo == True:
        testigo = False
        entrada = input(f"Escoja la opción, {mensaje_a} o {mensaje_b} ({a}-{b}): ")
        if not entrada.isalpha or entrada ==  "" and (entrada != a or entrada != b):
            testigo = True
        else:
            return entrada



def prompt_opciones(registro_opciones):
    testigo = True
    while testigo == True:
        testigo = False
        entrada = input(f"Escoja la opción, {registro_opciones} ")
        entrada = entrada.upper()

        if entrada not in registro_opciones:
            testigo = True
        else:
            return entrada



# Show all headers of a table
def headers(table,plus):
    cursor1.execute(f"SHOW COLUMNS FROM {table};") # Show headers
    for campo in cursor1:
        print(campo[0]+"  ",end="")
    for campo in plus:
        print(campo+"  ",end="")
    print("\n")



# Show all records of a gived table by variable cursor1
def show_registers(cursor):
    flag = True
    for registro in cursor:
        flag = False    #there is almost one record
        for campo in registro:  #show values for each field of the record
            print(f"{campo}       ",end="")
        print("\n")

    if flag:    #There isn't any record
        return 1
    else:       #There is almost one record
        return 0

##################################      MAIN      ##################################
system("clear")   #Clear shell
print("###############################      Ejercicio44      ###############################")

#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"

fichero = "subcontratados.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

# Para pasar cada línea de un fichero a un registro
datos = list()  # Inicializamos el registro de destino
subcontratados=[]
with open(ruta, mode="r",encoding="latin-1") as archivo:   
    contenido=archivo.readlines()
 
    for linea in contenido:
        numcamp = linea.count(";")
        registro = linea.replace('\n', '')
        datos.append(registro.split(";"))
    subcontratados = datos

longitud_subcontratados = len(contenido)       # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste
numcamp_subcontratados = numcamp


#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "facturacion.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

datos=list()
numcamp = 0
facturacion=[]
with open(ruta, mode="r",encoding="latin-1") as archivo:   
    contenido=archivo.readlines()
    contenido[0]=contenido[0][3:] #Cleaning the 3 first bad characters on the first element in the array contenido
    
    for i,linea in enumerate(contenido):
        numcamp = linea.count(";")
        registro = linea.replace('\n', '')
        datos.append(registro.split(";"))

        datos[i][3]=float(datos[i][3].replace(',','.')) # Convert text into float
        datos[i][4]=float(datos[i][4].replace(',','.')) # Convert text into float
        datos[i][5]=float(datos[i][5].replace(',','.')) # Convert text into float
    facturacion=datos    

longitud_facturacion = len(contenido)       # Numero de filas
numcamp += 1                    # Numero de columnas con ajuste
numcamp_facturacion=numcamp


conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1=conexion1.cursor()

cursor1.execute("drop database if exists financiera;")
cursor1.execute("create database financiera character set latin1 collate latin1_spanish_ci;")
cursor1.execute("use financiera;")
cursor1.execute("create table subcontratados (nif_sub varchar(12) NOT NULL PRIMARY KEY, nombre_sub varchar(15), apellidos_sub varchar(20), direccion_sub varchar(30), poblacion_sub varchar(20), provincia_sub varchar (20), cp_sub varchar(10), categoria_sub varchar(2), disponibilidad_sub varchar(10),horas_extras_sub varchar(7));")
# nif_sub
# nombre_sub 
# apellidos_sub 
# direccion_sub 
# poblacion_sub
# provincia_sub 
# cp_sub 
# categoria_sub 
# disponibilidad_sub 
# horas_extras_sub 
# notas_sub 
cursor1.execute("create table facturacion(codigo_fac INT NOT NULL UNIQUE AUTO_INCREMENT, fecha_fac varchar(10), nif_sub_fac varchar(12), precio_hora_fac int, numero_horas_fac int, facturacion_fac int,FOREIGN KEY(nif_sub_fac) REFERENCES subcontratados(nif_sub));")


for registro in subcontratados:
    print(registro)
    query=""
    for campo in registro:
        query=query+f"'{campo}',"
    query=query[:-1]    #to eliminate the last coma
    print(query)
    cursor1.execute(f"insert into subcontratados values ({query});")



for registro in facturacion:
    #query="NULL,"
    query=""
    for index,campo in enumerate(registro):
        if index > 0:   # to avoid the first field, the old id
            query=query+f"'{campo}',"
    query=query[:-1]    #to eliminate the last coma
    print(query)
    cursor1.execute(f"insert into facturacion (fecha_fac, nif_sub_fac, precio_hora_fac, numero_horas_fac, facturacion_fac) values ({query});")


#cursor1.execute("LOAD DATA INFILE 'C:/proyectos/base_coches.csv' INTO TABLE datos FIELDS TERMINATED BY  '\t' LINES TERMINATED BY '\n'")
print("CORRECTA CREACIÓN DE LA BASE DE DATOS")
conexion1.commit()
conexion1.close()