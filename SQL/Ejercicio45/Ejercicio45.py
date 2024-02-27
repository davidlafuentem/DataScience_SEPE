# Ejercicio 45 - Uso de SQL desde Python usando tablas y ficheros
# I. Repetir las siguientes consultas del ejercicio anterior:

# CONSULTA TOTAL: Muestra TODOS los datos de los trabajadores DE LAS DOS TABLAS, salvo el NIF de Facturación. Ordenar la consulta por APELLIDOS Y HORAS EXTRAS (orden ascendente).
# HORAS MAX: Muestra los datos NIF, NOMBRE, APELLIDOS, CP, POBLACIÓN, HORAS Y FACTURACIÓN de las personas que hayan relizado mas de 100 euros de facturación, ordenados por POBLACIÓN Y FACTURACIÓN (orden ascendente).
# II. Para cada consulta del ejercicio generar un fichero de salida en formato .CSV con el resultado, usando punto y coma como separador de campos. Comprobar que los ficheros se abren correctamente en Excel.

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
        print(f"{registro}")
        # for campo in registro:  #show values for each field of the record
        #     print(f"{campo}       ",end="")
    if flag:    #There isn't any record
        return 1
    else:       #There is almost one record
        return 0


# Show all records of a gived table by variable cursor1
def all_registers_to_csv(cursor):
    flag = True
    sentence = ""
    for registro in cursor:
        flag = False    #there is almost one record
        for campo in registro:  #show values for each field of the record
            sentence = sentence+f"{campo};"
        sentence=sentence[:-1] # Eliminate the la ";"
        sentence=sentence+"\n" 
    if flag:    #There isn't any record
        return 1
    else:       #There is almost one record
        return sentence

##################################      MAIN      ##################################
system("cls")   #Clear shell
print("###############################      Ejercicio45      ###############################")

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="financiera")
cursor1=conexion1.cursor()

# CONSULTA TOTAL: Muestra TODOS los datos de los trabajadores DE LAS DOS TABLAS, salvo el NIF de 
# Facturación. Ordenar la consulta por APELLIDOS Y HORAS EXTRAS (orden ascendente).
cursor1.execute("SELECT subcontratados.*, facturacion.fecha_fac, facturacion.precio_hora_fac, facturacion.numero_horas_fac, facturacion.facturacion_fac FROM subcontratados INNER JOIN facturacion ON subcontratados.nif_sub = facturacion.nif_sub_fac ORDER BY subcontratados.apellidos_sub,facturacion.facturacion_fac ASC;")
query=all_registers_to_csv(cursor1)
#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "query1.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(query)



# HORAS MAX: Muestra los datos NIF, NOMBRE, APELLIDOS, CP, POBLACIÓN, HORAS Y FACTURACIÓN de las 
# personas que hayan relizado mas de 100 euros de facturación, ordenados por POBLACIÓN Y FACTURACIÓN 
# (orden ascendente).
cursor1.execute("SELECT subcontratados.nif_sub, subcontratados.nombre_sub,subcontratados.apellidos_sub,subcontratados.cp_sub,subcontratados.poblacion_sub, facturacion.numero_horas_fac, facturacion.facturacion_fac FROM subcontratados INNER JOIN facturacion ON subcontratados.nif_sub = facturacion.nif_sub_fac AND facturacion.facturacion_fac > 100 ORDER BY facturacion.facturacion_fac, subcontratados.poblacion_sub;")
query=all_registers_to_csv(cursor1)
#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "query2.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(query)

conexion1.close()
