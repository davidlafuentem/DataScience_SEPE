import os
import random
import mysql.connector
from os import system

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
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};") # Show headers
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
                    return False,"NIE_FIRST_CHARACTER"
            else:   # It's not a number between first and last alphabetic character
                return False,"NIE_BAD_NUMBER"
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list
                return True,"NIE"
            else:
                return False,"NIE_BAD_ALPHABETICS_CHARACTERS"
            
        # Detect if it is a NIF
        elif identificador[0:8].isdecimal() and identificador[8].isalpha(): # Check if the last character is a letter and the rest is a number
            numero = int(identificador[:-1])
            resto = numero % 23
            if identificador[8].upper() == lista[resto]:    # checks the letter corresponds to the letter in the list   
                return True,"NIF"
            else:
                return False,"NIF_LETTER_MISMATCH"
        else:   # It's not a NIE or a NIF
            return False,"NIF_BAD_STRUCTURE",
    
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
                return "BAD_PHONE"
        else:   # It's not a number
            return "PHONE_NOT_A_NUMBER"
    else:   # Length is not correct
        return "BAD_PHONE_LENGTH"



#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio52?      ######################################################")

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor_sql=conexion1.cursor()

# Creation of the DB and its table
cursor_sql.execute("DROP DATABASE IF EXISTS alumnos_db;")
cursor_sql.execute("CREATE DATABASE alumnos_db character set latin1 collate latin1_spanish_ci;")
cursor_sql.execute("USE alumnos_db;")
cursor_sql.execute("CREATE TABLE alumnos (nif varchar(12) NOT NULL PRIMARY KEY, nombre varchar(15), apellidos varchar(20), direccion varchar(30), poblacion varchar(30),telefono varchar(9), provincia varchar (20), calificacion_final float);")
conexion1.commit()

# Insert values into DB from data extracted of the file Ejercicio51.csv
""" for registro in alumnos_fichero:  
    query=""
    for campo in registro:
        query=query+f"'{campo}',"
    query=query[:-1]    #to eliminate the last coma
    cursor_sql.execute(f"insert into alumnos values ({query});") """

#carpeta= r"C:/Proyectos_David/ficheros"    # For be used in windows class computer
carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/ficheros"
fichero = "Ejercicio51.csv"

cursor_sql.execute(f"LOAD DATA LOCAL INFILE '{carpeta}/{fichero}' INTO TABLE alumnos FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n';")
conexion1.commit()

# Add calculated fields
cursor_sql.execute("ALTER TABLE alumnos ADD COLUMN IF NOT EXISTS porcentaje_beca int default 0, ADD COLUMN IF NOT EXISTS precio_matricula int default 0, ADD COLUMN IF NOT EXISTS tasas int default 0, ADD COLUMN IF NOT EXISTS precio_final int default 0;")

# Scholarship percentage
cabecera=['nif','nombre','apellidos','direccion','poblacion','telefono','provincia','calificacion_final','porcentaje_beca','precio_matricula','tasas' ,'precio_final' ]
cursor_sql.execute(f"UPDATE alumnos SET porcentaje_beca=80 WHERE calificacion_final >= 9 AND calificacion_final <=10;")
cursor_sql.execute(f"UPDATE alumnos SET porcentaje_beca=40 WHERE calificacion_final >= 7 AND calificacion_final < 9;")
cursor_sql.execute(f"UPDATE alumnos SET porcentaje_beca=25 WHERE calificacion_final >= 5 AND calificacion_final < 7;")
cursor_sql.execute(f"UPDATE alumnos SET porcentaje_beca=0 WHERE calificacion_final < 5;")
conexion1.commit()

# Price matriculation
cursor_sql.execute(f"UPDATE alumnos SET precio_matricula=1200 WHERE poblacion='Madrid';")
cursor_sql.execute(f"UPDATE alumnos SET precio_matricula=1000 WHERE poblacion='Jaen' OR poblacion='Malaga';")
cursor_sql.execute(f"UPDATE alumnos SET precio_matricula=1100 WHERE poblacion='Salamanca' OR poblacion='Soria';")
cursor_sql.execute(f"UPDATE alumnos SET precio_matricula=900 WHERE poblacion='Guadalajara' OR poblacion='Toledo';")
cursor_sql.execute(f"UPDATE alumnos SET precio_matricula=1150 WHERE poblacion<>'Guadalajara' OR poblacion<>'Toledo' OR poblacion<>'Salamanca' OR poblacion<>'Soria' OR poblacion<>'Jaén' OR poblacion<>'Málaga' OR poblacion<>'Madrid';")
conexion1.commit()

# Taxes
cursor_sql.execute(f"UPDATE alumnos SET tasas=100 WHERE poblacion='Madrid';")
cursor_sql.execute(f"UPDATE alumnos SET tasas=50 WHERE poblacion='Valencia' OR poblacion='Asturias' OR poblacion='Teruel';")
cursor_sql.execute(f"UPDATE alumnos SET tasas=150 WHERE poblacion<>'Valencia' OR poblacion<>'Asturias' OR poblacion<>'Teruel' OR poblacion<>'Madrid';")
conexion1.commit()

# Calculate the final price
cursor_sql.execute(f"UPDATE alumnos SET precio_final=precio_matricula-(precio_matricula*porcentaje_beca/100)+tasas;")
conexion1.commit()
cabecera=headers_to_csv("alumnos")  # Extract all the headers of the table

# Check for errors in fields NIF/NIE and telephone too, and store the kind of error into each register
cabecera=headers_to_csv("alumnos") # Read headers of table "alumnos_erroneos"
sentence=f"{cabecera[:-1]};tipo_error\n"    # Add the field "tipo_error" to the headers line

cursor_sql.execute("SELECT * FROM alumnos;")

for registro in cursor_sql:
    error=""    # line where to create a summary of the different errors that can occur in a record
    coma=False  # Flag to know if there is a prior error message from NIE or NIF
    if not nie_nif_is_ok(registro[0])[0]:   # 0 return position shows if nie or nif is correct
        error=nie_nif_is_ok(registro[0])[1] # 1 return position shows which kind of ID is incorrect
        coma=True   # Flag to know that there is a previous error
    if telephone_is_ok(registro[5]) != 'movil' and telephone_is_ok(registro[5]) != 'fijo': # Bouth values are corrects
        if coma:
            error=f"{error},{telephone_is_ok(registro[5])}" # The two types of errors are added together
        else:
            error=f"{telephone_is_ok(registro[5])}" 
    if error != "": # At least there is one type of error
        for i,value in enumerate(registro): # Creation of a line for the csv file with all necessary fields
            if i!=7:    
                sentence=sentence+f"{value};"   # For all fields that they are not float
            if i==7:   # The 7th field must be changed to be readed in csv
                sentence=sentence+f"{str(value).replace(".",",")};" # Transformation into a float to be readed in csv file
        sentence=f"{sentence}{error}\n" # Add to the line in the last field, the error message

fichero = "alumnos_erroneos.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence)    
        

# Store all correct registers with a landline into fijos.csv file
cursor_sql.execute("SELECT * FROM alumnos;")
sentence=cabecera
for registro in cursor_sql:
    if nie_nif_is_ok(registro[0])[0] and telephone_is_ok(registro[5]) == 'fijo':
        for i,value in enumerate(registro):
            if i!=7:    
                sentence=sentence+f"{value};"
            else:   # The 7th field must be changed to be readed in csv
                sentence=sentence+f"{str(value).replace(".",",")};"
        sentence=sentence[:-1]  # To avoid the last ";"
        sentence=sentence+"\n"

fichero = "fijos.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence)    
    


# Store all correct registers with a mobil phone into movil.csv file
cursor_sql.execute("SELECT * FROM alumnos;")
sentence=cabecera
for registro in cursor_sql:
    if nie_nif_is_ok(registro[0])[0] and telephone_is_ok(registro[5]) == 'movil':
        for i,value in enumerate(registro):
            if i!=7:    
                sentence=sentence+f"{value};"
            else:   # The 7th field must be changed to be readed in csv
                sentence=sentence+f"{str(value).replace(".",",")};"
        sentence=sentence[:-1]  # To avoid the last ";"
        sentence=sentence+"\n"

fichero = "movil.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence) 

# Store all correct registers with a NIF phone into listado_nif.csv file
cursor_sql.execute("SELECT * FROM alumnos;")
sentence=cabecera
for registro in cursor_sql:
    if nie_nif_is_ok(registro[0])[1]=='NIF':
        for i,value in enumerate(registro):
            if i!=7:    
                sentence=sentence+f"{value};"
            else:   # The 7th field must be changed to be readed in csv
                sentence=sentence+f"{str(value).replace(".",",")};"
        sentence=sentence[:-1]  # To avoid the last ";"
        sentence=sentence+"\n"

fichero = "listado_nif.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence) 


# Store all correct registers with a NIE phone into listado_nie.csv file
cursor_sql.execute("SELECT * FROM alumnos;")
sentence=cabecera
for registro in cursor_sql:
    if nie_nif_is_ok(registro[0])[1]=='NIE':
        for i,value in enumerate(registro):
            if i!=7:    
                sentence=sentence+f"{value};"
            else:   # The 7th field must be changed to be readed in csv
                sentence=sentence+f"{str(value).replace(".",",")};"
        sentence=sentence[:-1]  # To avoid the last ";"
        sentence=sentence+"\n"
        
fichero = "listado_nie.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(sentence) 