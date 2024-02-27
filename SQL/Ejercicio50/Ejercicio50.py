# Ejercicio 50 - Función de verificación de NIF y NIE
# I. A partir de los ejercicios 47 y 48 realizar una función a la que se le pase por parámetro un NIF o un NIE completos y devuelva "true" 
# si es correcto y "false" si no es correcto.

import os
import random
import mysql.connector
import dateutil
from os import system
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

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
    import mysql

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
                    return False
            else:   # It's not a number between first and last alphabetic character
                return False
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list
                return True
            else:
                return False
            
        # Detect if it is a NIF
        elif identificador[0:8].isdecimal() and identificador[8].isalpha(): # Check if the last character is a letter and the rest is a number
            numero = int(identificador[:-1])
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list   
                return True
            else:
                return False
        else:   # It's not a NIE or a NIF
            return False
    
    else:   # Length not correct
        return False    



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
                sentence = sentence+f"{campo};"
        sentence=sentence[:-1] # Eliminate the la ";"
        sentence=sentence+"\n" 
    if flag:    #There isn't any record
        return 1
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





##################################      MAIN      ##################################
system("clear")   #Clear shell
print("###############################      Ejercicio50      ###############################")
dni=""

dni = prompt_dni()

print(f"El número de documento de introducido es correcto: {dni}")