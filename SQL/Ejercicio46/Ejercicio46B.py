# Ejercicio 46 - Creación de consultas de selección por parámetros desde Python.
# I. Abrir la base de datos del Ejercicio 44 y añadir las siguientes consultas de selección:

# SUBCONTRATADOS APELLIDO: Presentar los campos APELLIDO, NOMBRE, PROVINCIA Y DISPONIBILIDAD. Ordenar la consulta por APELLIDO.
# SUBCONTRATADOS DISPONIBLES: Presentar los campos APELLIDO, NOMBRE, PROVINCIA, CATEGORÍA. Deben aparecer los subcontratados disponibles.
# II. Copiar la consulta SUBCONTRATADOS DISPONIBLES para crear SUBCONTRATADOS DISPONIBLES EN LOS PRÓXIMOS 30 DÍAS. Modificar lo que se crea necesario en la copia para obtener el resultado requerido.

# III. Crear las siguientes consultas nuevas:

# SUBCONTRATADOS POR CATEGORÍA: Debe mostrar los campos que considere de la tabla SUBCONTRATADOS. Deben aparecer los registros de la categoría que nos solicite Python (parámetro), descartando cualquier valor distinto a AD, ET y PR.
# FACTURAS ENTRE FECHAS: Mostrará TODOS los campos de las tablas SUBCONTRATADOS y FACTURACIÓN evitando repeticiones. Debe mostrar los registros de facturas entre 2 fechas que nos solicite por Python.
# FACTURAS DEL MES ACTUAL: Debe mostrar los campos que considere de las tablas SUBCONTRATADOS y FACTURACIÓN evitando repeticiones. Debe mostrar los registros de facturas del mes actual.
# ALTA DE FACTURAS: Debe mostrar todos los campos de la tabla FACTURAS y los campos NOMBRE APELLIDOS de la tabla SUBCONTRATADOS. Crear previamente en la Base de Datos campos calculados con el IVA (TOTAL FAC * 21%) y TOTAL de la factura (TOTAL FAC + IVA).
# SUBCONTRATADOS DISPONIBLES POR FECHA: Debe mostrar los campos que considere de la tabla SUBCONTRATADOS. Debe mostrar los registros con disponibilidad entre 15 días antes y 15 días después de una fecha solicitada por Python.
# IV. Guardar el documento .PY en tu carpeta como Ejercicio 45. Para cada consulta del ejercicio generar un fichero de salida en formato .CSV con el resultado INCLUYENDO ENCABEZADOS DE CAMPO, usando punto y coma como separador de campos. Comprobar que los ficheros se abren correctamente en Excel.

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


# Mask for NIE and NIF
# def mask_nie_nif(identificador =""):
#     salida=""
#     if identificador[0].isalpha() and identificador[8].isalpha() and len(identificador)==9 and (identificador[0].upper()=='X' or identificador[0].upper()=='Y' or identificador[0].upper()=='Z'):   #NIE
#         for i,caracter in enumerate(identificador):
#             if i==0 or i==7:
#                 salida=salida+caracter+"-"
#             elif i==1 or i==4:
#                 salida=salida+caracter+"."
#             else:
#                 salida=salida+caracter 

#     elif identificador[0].isdecimal() and identificador[8].isalpha() and len(identificador)==9: #NIF
#         for i,caracter in enumerate(identificador):
#             if i==7:
#                 salida=salida+caracter+"-"
#             elif i==1 or i==4:
#                 salida=salida+caracter+"."
#             else:
#                 salida=salida+caracter 

#     else:   
#         return "ERROR"

#     return salida


def mask_nie_nif(identificador =""):
    salida=""
    if identificador[0].isalpha() and identificador[8].isalpha() and len(identificador)==9 and (identificador[0].upper()=='X' or identificador[0].upper()=='Y' or identificador[0].upper()=='Z'):   #NIE
        salida=f"{identificador[0]}-{identificador[1]}.{identificador[2:5]}.{identificador[5:8]}-{identificador[8]}"
    elif identificador[0].isdecimal() and identificador[8].isalpha() and len(identificador)==9: #NIF
        salida=f"{identificador[0:2]}.{identificador[2:5]}.{identificador[5:8]}-{identificador[8]}"
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
print("###############################      Ejercicio46B      ###############################")

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",db="financiera")
cursor1=conexion1.cursor()


# SUBCONTRATADOS APELLIDO: Presentar los campos APELLIDO, NOMBRE, PROVINCIA Y DISPONIBILIDAD. 
# Ordenar la consulta por APELLIDO.
cabecera="APELLIDOS;NOMBRE;PROVINCIA;DISPONIBILIDAD\n"
cursor1.execute("SELECT subcontratados.apellidos_sub, subcontratados.nombre_sub, subcontratados.provincia_sub, subcontratados.disponibilidad_sub FROM subcontratados ORDER BY subcontratados.apellidos_sub;")
show_registers(cursor1)
cursor1.execute("SELECT subcontratados.apellidos_sub, subcontratados.nombre_sub, subcontratados.provincia_sub, subcontratados.disponibilidad_sub FROM subcontratados ORDER BY subcontratados.apellidos_sub;")
linea= cabecera+all_registers_to_csv(cursor1,[])
#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_1.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    
print("\n")



# SUBCONTRATADOS DISPONIBLES: Presentar los campos APELLIDO, NOMBRE, PROVINCIA, CATEGORÍA. 
# Deben aparecer los subcontratados disponibles.
cabecera="APELLIDOS;NOMBRE;PROVINCIA;CATEGORIA\n"
cursor1.execute("SELECT subcontratados.apellidos_sub, subcontratados.nombre_sub, subcontratados.provincia_sub, subcontratados.categoria_sub FROM subcontratados WHERE subcontratados.disponibilidad_sub IS NOT NULL;")
show_registers(cursor1)
cursor1.execute("SELECT subcontratados.apellidos_sub, subcontratados.nombre_sub, subcontratados.provincia_sub, subcontratados.categoria_sub FROM subcontratados WHERE subcontratados.disponibilidad_sub IS NOT NULL;")
linea= cabecera+all_registers_to_csv(cursor1,[])   
#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros/"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_2.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    
print("\n")




# II. Copiar la consulta SUBCONTRATADOS DISPONIBLES para crear SUBCONTRATADOS DISPONIBLES EN LOS PRÓXIMOS 30 DÍAS.
# Modificar lo que se crea necesario en la copia para obtener el resultado requerido.
cabecera="APELLIDOS;NOMBRE;PROVINCIA;CATEGORIA;DISPONIBILIDAD\n"    # Set the header fields
cursor1.execute("SELECT subcontratados.apellidos_sub,subcontratados.nombre_sub,subcontratados.provincia_sub,subcontratados.categoria_sub,subcontratados.disponibilidad_sub FROM subcontratados WHERE subcontratados.disponibilidad_sub IS NOT NULL;")
today = date.today()    
limit_date = today + timedelta(days=30) #The time range for searching the worker ability is 30 days 
linea=""    # This line will contain the registers to be wrote into the csv file
linea=cabecera  # Put the header fields in the first row
testigo = False

for registro in cursor1:
    linea_draft=""  # Register to store
    for i,campo in enumerate(registro):
        if i != 4:  # All fields except fourth need to be stored
            linea_draft=linea_draft+f"{campo};" # Construction of the register to store
        else:    #4th field is where there is the date
            hability_date=datetime.strptime(campo, "%d/%m/%Y").date() # Tranformation text to date
            if hability_date >= today and hability_date <= limit_date:
                testigo = True
                linea_draft=linea_draft+f"{campo}\n" # Construction of the register to store in csv
                linea=linea+linea_draft # add this line to the final sentence

if testigo: #if there is at least one record to be stored in a file
    #carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
    carpeta= r"C:/Proyectos_David/ficheros"
    fichero = "exercice46_query_3.csv"
    ruta = os.path.join(carpeta, fichero)
    ruta = os.path.abspath(ruta)
    with open(ruta, mode="w",encoding="latin-1") as archivo:   
        archivo.writelines(linea)    
print("\n")



# SUBCONTRATADOS POR CATEGORÍA: Debe mostrar los campos que considere de la tabla SUBCONTRATADOS. 
# Deben aparecer los registros de la categoría que nos solicite Python (parámetro), descartando cualquier valor distinto a AD, ET y PR.
cabecera="NIF;NOMBRE;APELLIDOS;DIRECCION;POBLACION;PROVINCIA;COD_POSTAL;CATEGORIA;DISPONIBILIDAD;HORAS_EXTRAS\n"
categorias=['AD','ET','PR'] #Set the only ones values possible
print(f"Mostrar registros por categoria ({categorias})")
categoria=prompt_opciones(categorias)   # Take values by keyboard with a list of only possible values 

cursor1.execute(f"SELECT subcontratados.* FROM subcontratados WHERE subcontratados.categoria_sub = '{categoria}';")
show_registers(cursor1)
print("\n")

cursor1.execute(f"SELECT subcontratados.* FROM subcontratados WHERE subcontratados.categoria_sub = '{categoria}';")
linea=cabecera
linea=linea+all_registers_to_csv(cursor1,[0]) # Return all the fields of all registers and put them in a string separated by ";"
#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_4B.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    



# FACTURAS ENTRE FECHAS: Mostrará TODOS los campos de las tablas SUBCONTRATADOS y FACTURACIÓN evitando repeticiones. 
# Debe mostrar los registros de facturas entre 2 fechas que nos solicite por Python.
print("Seleccione las facturas emitidas entre dos fechas.")
print("Fecha menor:")
fecha_menor=prompt_date()
print("Fecha mayor:")
fecha_mayor=prompt_date()

cabecera="NIF;NOMBRE;APELLIDOS;DIRECCION;POBLACION;PROVINCIA;COD_POSTAL;CATEGORIA;DISPONIBILIDAD;HORAS_EXTRAS;COD_FACTURA;FECHA_FACTURA;NIF_FACTURA;PRECIO_HORA;HORAS;FACTURACION_HORAS\n"
#Select of all the fields of tables "subcontratados" and "facturacion"
cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
show_registers(cursor1)
print("\n")
cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
linea_draft=""  # Temporal line may be wrote to the file
linea=cabecera    # Final line that will be wrote to the file.  We add the first row that contains headers
flag=False  # Variable to show if the register meets the conditions

for registro in cursor1:    # Read register after register
    flag=False
    linea_draft=""
    fecha=""
    for i,campo in enumerate(registro):
        if i==0 or i==12: # Positions where there are NIEs or NIFs
            if mask_nie_nif(campo)!="ERROR":
                linea_draft=linea_draft+f"{mask_nie_nif(campo)};" # Construction of the register that may be stored in file        
        elif  i == 11:    # Field 11 is the date we need to work with
            fecha=datetime.strptime(campo, "%d/%m/%Y").date() # Tranformation text to date 
            if fecha >=fecha_menor and fecha <= fecha_mayor:    # Comparation between dates
               flag=True    # Date_fac is beetween limits, register should be wrote
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file
        else:
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file
    if flag:    # Date_fac is beetween limits and should be set to be a correct csv line
        linea_draft=linea_draft[:-1]
        linea_draft=linea_draft+"\n"
        linea=linea+linea_draft # Store the temporal line in the final line to be wrote in csv file


#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_5B.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    

    
    
# FACTURAS DEL MES ACTUAL: Debe mostrar los campos que considere de las tablas SUBCONTRATADOS y FACTURACIÓN evitando repeticiones. 
# Debe mostrar los registros de facturas del mes actual.
cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
show_registers(cursor1)

cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
linea_draft=""  # Temporal line may be wrote to the file
cabecera="NIF;NOMBRE;APELLIDOS;DIRECCION;POBLACION;PROVINCIA;COD_POSTAL;CATEGORIA;DISPONIBILIDAD;HORAS_EXTRAS;CODIGO_FACTURA;FECHA_FACTURA;NIF_FACTURA;PRECIO_HORA;HORAS;FACTURACION\n"
linea=cabecera    # Final line that will be wrote to the file. Put the 1st row of headers
flag=False  # Variable that shows if it meets the condition
actual_month = date.today().month

for registro in cursor1:    # Read register after register
    flag=False
    linea_draft=""  # Line that may be wrote to the file
    for i,campo in enumerate(registro):
        if i==0 or i==12: # Positions where there are NIEs or NIFs
            if mask_nie_nif(campo)!="ERROR":
                linea_draft=linea_draft+f"{mask_nie_nif(campo)};" # Construction of the register that may be stored in file   
        elif  i == 11:    # Field 11 is the date we need to work with
            campo=datetime.strptime(campo, "%d/%m/%Y").date() # Tranformation text to date 
            if campo.month == actual_month:    # Comparation between dates
               flag=True    # Date_fac is beetween limits, register should be wrote
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file
        else:
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file
    if flag:    # Date_fac is beetween limits and should be set to be a correct csv line
        linea_draft=linea_draft[:-1]
        linea_draft=linea_draft+"\n"
        linea=linea+linea_draft # Stor the temporal line in the final line to be wrote in csv file

#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_6B.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    

    

# ALTA DE FACTURAS: Debe mostrar todos los campos de la tabla FACTURAS y los campos NOMBRE APELLIDOS de la tabla SUBCONTRATADOS. 
# Crear previamente en la Base de Datos campos calculados con el IVA (TOTAL FAC * 21%) y TOTAL de la factura (TOTAL FAC + IVA).

# Creation of the news fields that will permit to calculate the price with IVA
cursor1.execute("ALTER TABLE facturacion ADD COLUMN IF NOT EXISTS iva_factura FLOAT, ADD COLUMN IF NOT EXISTS total_factura FLOAT;")
conexion1.commit()
cursor1.execute(f"UPDATE facturacion SET facturacion.iva_factura=facturacion.facturacion_fac*0.21,facturacion.total_factura=facturacion.facturacion_fac+facturacion.iva_factura;")
conexion1.commit()

cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
show_registers(cursor1)
print("\n")

cursor1.execute(f"SELECT subcontratados.*,facturacion.* FROM subcontratados INNER JOIN facturacion WHERE subcontratados.nif_sub = facturacion.nif_sub_fac;")
cabecera="NIF;NOMBRE;APELLIDOS;DIRECCION;POBLACION;PROVINCIA;COD_POSTAL;CATEGORIA;DISPONIBILIDAD;HORAS_EXTRAS;COD_FACTURA;FECHA_FACTURA;NIF_FACTURA;PRECIO_HORA;HORAS;FACTURACION_HORAS;IVA_FACTURA;TOTAL_CON_IVA\n"
linea=cabecera+all_registers_to_csv(cursor1,[0,12])

#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_7B.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    



# SUBCONTRATADOS DISPONIBLES POR FECHA: Debe mostrar los campos que considere de la tabla SUBCONTRATADOS. 
# Debe mostrar los registros con disponibilidad entre 15 días antes y 15 días después de una fecha solicitada 
# por Python.   
print("Seleccione la fecha para revisar disponibilidad.")
fecha_teclado=prompt_date()
fecha_menor= fecha_teclado + timedelta(days=-15) #The time range for searching the worker ability 
fecha_mayor= fecha_teclado + timedelta(days=15) #The time range for searching the worker ability   

#Select of all the fields of tables "subcontratados" and "facturacion"
cursor1.execute(f"SELECT subcontratados.* FROM subcontratados WHERE disponibilidad_sub IS NOT NULL;")
linea_draft=""  # Temporal line may be wrote to the file
cabecera="NIF;NOMBRE;APELLIDOS;DIRECCION;POBLACION;PROVINCIA;COD_POSTAL;CATEGORIA;DISPONIBILIDAD;HORAS_EXTRAS\n"
linea=cabecera    # Final line that will be wrote to the file. Put the headers at first row
flag=False  # Variable to know if it meets the conditions
show_something=[]

for registro in cursor1:    # Read register after register
    flag=False
    linea_draft=""
    for i,campo in enumerate(registro):
        if i==0:
            if mask_nie_nif(campo)!="ERROR":
                linea_draft=linea_draft+f"{mask_nie_nif(campo)};" # Construction of the register that may be stored in file   
        elif  i == 8:    # Field 11 is the date we need to work with
            campo=datetime.strptime(campo, "%d/%m/%Y").date() # Tranformation text to date 
            if campo >=fecha_menor and campo <= fecha_mayor:    # Comparation between dates
               flag=True    # Date_fac is beetween limits, register should be wrote
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file
        else:
            linea_draft=linea_draft+f"{campo};" # Construction of the register that may be stored in file

    if flag:    # Date_fac is beetween limits and should be set to be a correct csv line
        linea_draft=linea_draft[:-1]
        linea_draft=linea_draft+"\n"
        linea=linea+linea_draft # Stor the temporal line in the final line to be wrote in csv file
        show_something.append(registro)

for something in show_something:
    print(something)

#carpeta= "/Users/DLF/Curso_Data_Science_2023/ficheros"
carpeta= r"C:/Proyectos_David/ficheros"
fichero = "exercice46_query_8B.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea)    



conexion1.close()
            

        

    
