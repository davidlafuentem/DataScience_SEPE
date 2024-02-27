# Ejercicio 54 - Trabajo con arrays usando NumPy

# I. Se entrega un fichero de datos llamado "ejercicio54.csv". Importar el fichero en una tabla dentro 
# de una base de datos nueva y completar los datos que faltan insertando los campos vacíos. Implementar 
# un programa en Python que mediante sentencias SQL rellene los campos vacíos en la base de datos. El 
# campo fecha deberá ser de tipo DATE, y las temperaturas de tipo FLOAT.

# II. Se muestra un reporte de la temperatura durante el día en 5 ciudades de Madrid en los meses de 
# septiembre y octubre de 2023. Las temperaturas se reportan en grados centígrados.

# a)  Determina para cada uno de los días considerados la Temperatura Promedio (TP) de las 5 Ciudades.

# b)  Clasifica a cada uno de los días en Cálido, Templado y Frío de acuerdo al siguiente criterio:

#                                          Cálido  si   TP > 25

#                                          Templado si    20<= TP <= 25

#                                          Frío si   TP < 20

#       en donde TP denota la "Temperatura Promedio" de las 5 Ciudades.


# c) Crear 3 ficheros de salida .CSV, uno por cada criterio de clasificación (cálido, templado o frio). 
# Obtener todos los datos solicitados a la base de datos mediante tablas usando los métodos de la librería NumPy.

# d) Crear un fichero de salida datos.csv que muestre los siguientes datos por cada ciudad analizada:
# Media Temperatura Septiembre
# Media Temperatura Octubre
# Nº de Días Con Temperaturas Frías
# Nº de Días Con Temperaturas Templadas
# Nº de Días Con Temperaturas Cálidas


import os
import random
import mysql.connector
import numpy as np
from os import system
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

#####################################################################################################################################
########################################################      FUNCTIONS      ########################################################
#####################################################################################################################################

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
def headers(table,plus=""):
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};") # Show headers
    for campo in cursor_sql:
        print(campo[0]+"  ",end="")
    for campo in plus:
        print(campo+"  ",end="")
    print("\n")



# Return all headers of a table for being used in a csv file
def headers_to_csv(table,plus=""):
    linea=""
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};")
    #cursor_sql.execute("SHOW COLUMNS FROM %s;"(table)) # Show headers

    # Fields of the query
    for campo in cursor_sql:
        linea=linea+f"{campo[0]};"
    # Fields of the list gived
    for campo in plus:
        linea=linea+f"{campo};"
    linea=linea[:-1]    # Erase the last ";"
    linea = f"{linea}\n"  # End of the line
    return linea
    


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



# Detect wether a NIE or NIF are correct
def nie_nif_is_ok(identificador =""):
    lista=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    
    if len(identificador)==9:   # Check for the correct lenght
        # Detect if it is a NIE
        if identificador[0].isalpha() and identificador[8].isalpha():   # First and last position must be an alphabetic character
            if identificador[1:8].isdigit():    # Check characters are all figurs without first and last position 
                if identificador[0].upper()=='X':   # Add 0
                    numero=int(identificador[1:-1]) # For using only figures
                elif identificador[0].upper()=='Y': # Add 1
                    ident_temp=identificador
                    ident_temp=f"1{identificador[1:-1]}" # Work with only figures
                    numero=int(ident_temp) # For using only figures
                elif identificador[0].upper()=='Z': # Add 2
                    ident_temp=identificador
                    ident_temp=f"2{identificador[1:-1]}"
                    numero=int(ident_temp) # For using only figures
                else:   # Bad first letter
                    return False,"NIE"
            else:   # It's not a number between first and last alphabetic character
                return False,"NIE"
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list
                return True,"NIE"
            else:
                return False,"NIE"
            
        # Detect if it is a NIF
        elif identificador[0:8].isdecimal() and identificador[8].isalpha(): # Check if the last character is a letter and the rest is a number
            numero = int(identificador[:-1])
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list   
                return True,"NIF"
            else:
                return False,"NIF"
        else:   # It's not a NIE or a NIF
            return False,"NIF"
    else:   # Length not correct
        return False,"NOT_NIE_OR_NIF"   



# Get a dni
def prompt_dni():
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca número de documento de identidad: ")
        if nie_nif_is_ok(entrada):
            return entrada
        else:
            print("El número introducido no es un documento de identidad valido.  Vuelva introducir otro identificador.")
            testigo = True



# Mask the field NIE or NIF of the BD
def mask_nie_nif(identificador =""):
    salida=""
    if identificador[0].isalpha() and identificador[8].isalpha() and len(identificador)==9 \
        and (identificador[0].upper()=='X' or identificador[0].upper()=='Y' or identificador[0].upper()=='Z'):   #NIE
        salida=f"{identificador[0]}-{identificador[1]}.{identificador[2:5]}.{identificador[5:8]}-{identificador[8]}"    # Mask
    elif identificador[0].isdecimal() and identificador[8].isalpha() and len(identificador)==9: #NIF
        salida=f"{identificador[0:2]}.{identificador[2:5]}.{identificador[5:8]}-{identificador[8]}" # Mask
    else:   
        return "ERROR"
    return salida



# Show all records of a gived table by variable cursor1
# Mask is a list with all positions where the field need a mask
def all_registers_to_csv(cursor,mask=[]):
    flag = True
    sentence = ""
    for registro in cursor:
        flag = False    #there is almost one record
        for i,campo in enumerate(registro):  #show values for each field of the record
            if i in mask:
                if mask_nie_nif(campo)!="ERROR":
                    sentence = sentence+f"{mask_nie_nif(campo)};"
            else:
                if  isinstance(campo, float):   
                    campo=str(campo).replace(".",",")
                sentence = sentence+f"{campo};"
        sentence=sentence[:-1] # Eliminate the la ";"
        sentence=sentence+"\n" 
    if flag:    #There isn't any record
        return False
    else:       #There is almost one record
        return sentence


# Get a date
def prompt_date():
    import datetime

    testigo = True
    fecha = ""

    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca fecha (día[xx]/mes[xx]/año[xxxx]): ")
        try:
            fecha = datetime.strptime(entrada, "%d/%m/%Y").date() # Tranformation text to date
        except(ValueError):
            print("Formato de fecha incorrecto")
            entrada = ""

        if entrada != "":
            return fecha
        else:
            testigo = True

# Check if the given parameter is a correct telephone number
def telephone_is_ok(telephone=""):
    if len(telephone)==9:   # Correct length
        if telephone.isdigit():   # It's a number
            if (telephone[0]=='6' or telephone[0]=='7'):    # Correct first mobil number and not a landline
                return "movil"
            elif telephone[0]=='9' or telephone[0]=='8':  # Correct first landline number
                return "fijo"
            else:
                return "TELEFONO"
        else:   # It's not a number
            return "TELEFONO"
    else:   # Length is not correct
        return "TELEFONO"



#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio54      ######################################################")


# Creation of the DB and its table
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor_sql=conexion1.cursor()
cursor_sql.execute("drop database if exists temperaturas_DB;")
cursor_sql.execute("create database temperaturas_DB character set latin1 collate latin1_spanish_ci;")
cursor_sql.execute("use temperaturas_DB;")
cursor_sql.execute("create table temperaturas (fecha date NOT NULL PRIMARY KEY, dia varchar(10), alcorcon float, mostoles float, leganes float, fuenlabrada float, getafe float, temperatura_promedio float, clasificacion varchar(10));")
conexion1.commit()

#carpeta= r"C:/Proyectos_David/ficheros/"
carpeta=r'/Users/dlf/Documents/Curso_Data_Science_2023/ficheros'
fichero = "Ejercicio54.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
#cursor_sql.execute(f"LOAD DATA INFILE 'C:/Proyectos_David/ficheros/Ejercicio54.csv' INTO TABLE temperaturas FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n';")
cursor_sql.execute(f"LOAD DATA LOCAL INFILE '{ruta}' INTO TABLE temperaturas FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n';")
conexion1.commit()


# II. Se muestra un reporte de la temperatura durante el día en 5 ciudades de Madrid en los meses de 
# septiembre y octubre de 2023. Las temperaturas se reportan en grados centígrados.
# a) y c)
cursor_sql.execute("SELECT * FROM temperaturas")
np_temperaturas = []
temp= []
for i,registro in enumerate(cursor_sql):
    temp=[]
    for j,campo in enumerate(registro):
        temp.append(campo)
    np_temperaturas.append(temp)

np_temperaturas=np.array(np_temperaturas)


for i,registro in enumerate(np_temperaturas):  
    np_temperaturas[i][7]=round(np.mean(registro[2:7],dtype=np.float64),2)  # Mean by row
    #registro[7]=registro[2:7].mean()
    
    if np_temperaturas[i][7] > 25:
        np_temperaturas[i][8] = "Calido"
    elif np_temperaturas[i][7]>=20 and np_temperaturas[i][7]<=25:
        np_temperaturas[i][8] = "Templado"
    elif np_temperaturas[i][7]<20:
        np_temperaturas[8]="Frío"
    
    cursor_sql.execute(f"UPDATE temperaturas SET temperatura_promedio={np_temperaturas[i][7]}, clasificacion='{np_temperaturas[i][8]}' WHERE fecha='{np_temperaturas[i][0]}';")
conexion1.commit()

# c) Crear 3 ficheros de salida .CSV, uno por cada criterio de clasificación (cálido, templado o frio). Obtener todos los datos solicitados a la base de datos mediante tablas usando los métodos de la librería NumPy
sentence=headers_to_csv("temperaturas")
cursor_sql.execute("SELECT * FROM temperaturas WHERE clasificacion='calido';")
registers=all_registers_to_csv(cursor_sql)
if registers:
    sentence=sentence+registers
    fichero = "calido.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)
    with open(ruta, mode="w",encoding="latin-1") as archivo:   
        archivo.writelines(sentence) 
else:
    print("No hay registros que escribir en el fichero 'calido.csv'")    

sentence=headers_to_csv("temperaturas")
cursor_sql.execute("SELECT * FROM temperaturas WHERE clasificacion='templado';")
registers=all_registers_to_csv(cursor_sql)
if registers:
    sentence=sentence+registers
    fichero = "templado.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)
    with open(ruta, mode="w",encoding="latin-1") as archivo:   
        archivo.writelines(sentence) 
else:
    print("No hay registros que escribir en el fichero 'templado.csv'")    


sentence=headers_to_csv("temperaturas")
cursor_sql.execute("SELECT * FROM temperaturas WHERE clasificacion='frio';")
registers=all_registers_to_csv(cursor_sql)
if registers:
    sentence=sentence+registers
    fichero = "frio.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)
    with open(ruta, mode="w",encoding="latin-1") as archivo:   
        archivo.writelines(sentence)
else:
    print("No hay registros que escribir en el fichero 'frio.csv'")    


# d) Crear un fichero de salida datos.csv que muestre los siguientes datos por cada ciudad analizada:


# Media Temperatura Septiembre Alcorcón
ciudades=headers_to_csv("temperaturas").split(';')
ciudades=ciudades[2:7]  # Select the fields that contain the name of the cities to work with

for ciudad in ciudades:
    registers = list()
    cursor_sql.execute(f"SELECT {ciudad} FROM temperaturas WHERE (fecha>=20230901 AND fecha<=20230931);")
    for register in cursor_sql:
        registers.append(register[0])   # Return 2 fields, but we need the first

    np_temperaturas=np.array(registers)
    media_septiembre=round(np_temperaturas.mean(),2)

    # Media Temperatura Octubre Alcorcón
    registers = list()
    cursor_sql.execute(f"SELECT {ciudad} FROM temperaturas WHERE (fecha>=20231001 AND fecha<=20231031);")
    for register in cursor_sql:
        registers.append(register[0])

    np_temperaturas=np.array(registers)
    media_octubre=round(np_temperaturas.mean(),2)

    # Nº de Días Con Temperaturas Frías, Templadas, Cálidas
    frio=0
    templado=0
    calido=0

    cursor_sql.execute(f"SELECT {ciudad} FROM temperaturas;")
    for register in cursor_sql:
        if register[0]<20:
            frio+=1
        elif register[0] >=20 and register[0]<=25:
            templado+=1
        elif register[0]>25:
            calido+=1

    sentence=f"Media Temperatura Septiembre;{str(media_septiembre).replace('.',',')}\nMedia Temperatura Octubre;{str(media_octubre).replace('.',',')}\nNº de Días Con Temperaturas Frías;{frio}\nNº de Días Con Temperaturas Templadas;{templado}\nNº de Días Con Temperaturas Cálidas;{calido}"
    fichero = f"{ciudad}.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)
    with open(ruta, mode="w",encoding="latin-1") as archivo:   
        archivo.writelines(sentence)
