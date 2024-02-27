import os
import random
import mysql.connector
from os import system
import urllib
from urllib import request

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
        elif identificador[0:8].isdigit() and identificador[8].isalpha(): # Check if the last character is a letter and the rest is a number
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
print("#################################################     Ejercicio53      ######################################################")

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor_sql=conexion1.cursor()
cursor_sql.execute("USE alumnos_db;")

#carpeta= r"C:/Proyectos_David/ficheros"    # For be used in windows class computer
carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/ficheros"
fichero = "error.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
registers_with_error=[]

with open(ruta, mode="r",encoding="latin-1") as archivo:   
    contenido=archivo.readlines()
 
    for i,linea in enumerate(contenido):
        if i!=0:    # To eliminate the first line that contains the header
            registro = linea.replace('\n', '')
            registers_with_error.append(registro.split(";"))

# Add calculated fields
cursor_sql.execute("ALTER TABLE alumnos ADD COLUMN IF NOT EXISTS Errores varchar (10) default 'NO';")
conexion1.commit()

for register in registers_with_error:
    error = ""
    # Create the error message to store into the field 'Errores' of the table 'alumnos'
    if not nie_nif_is_ok(register[0])[0]:   # There is an error in NIE/NIF field
        error = nie_nif_is_ok(register[0])[1]
    if telephone_is_ok(register[5])== "TELEFONO":
        if error!="":
            error="VARIOS"
        else:
            error="TELEFONO"

    cursor_sql.execute("UPDATE alumnos SET Errores = %s WHERE nif = %s;", (error, register[0]))
    conexion1.commit()



# Store all correct registers with a NIE phone into listado_nie.csv file
cabecera=headers_to_csv("alumnos")
sentence=cabecera

cursor_sql.execute("SELECT * FROM alumnos;")

for registro in cursor_sql:
        for i,value in enumerate(registro):
            if i!=7:    
                sentence=sentence+f"{value};"
            else:   # The 7th field must be changed to be readed in csv as a float
                sentence=sentence+f"{str(value).replace(".",",")};"
        sentence=sentence[:-1]  # To avoid the last ";"
        sentence=sentence+"\n"
        
fichero = "copia.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence) 

