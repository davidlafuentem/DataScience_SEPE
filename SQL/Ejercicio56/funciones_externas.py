import os
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
def headers(table,conexion1,plus=""):
    cursor_sql=conexion1.cursor()
    
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};") # Show headers
    for campo in cursor_sql:
        print(campo[0]+"  ",end="")
    for campo in plus:
        print(campo+"  ",end="")
    print("\n")



# Return all headers of a table for being used in a csv file
def headers_to_csv(table,conexion1,plus=""):
    linea=""
    
    cursor_sql=conexion1.cursor()
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};")
    #cursor_sql.execute("SHOW COLUMNS FROM %s;",(table)) # Show headers
    
    # Fields of the query
    for campo in cursor_sql:
        linea=linea+f"{campo[0]};"
    # Fields of the gived list
    for campo in plus:
        linea=linea+f"{campo};"
    linea=linea[:-1]    # Erase the last ";"
    linea = f"{linea}\n"  # End of the line
    return linea


# Return all headers of a table for being used in a csv file
def headers_to_array(table,conexion,plus=""):
    tabla=[]
    
    cursor_sql=conexion.cursor()
    cursor_sql.execute(f"SHOW COLUMNS FROM {table};")
    #cursor_sql.execute("SHOW COLUMNS FROM %s;",(table)) # Show headers
    
    # Fields of the query
    for campo in cursor_sql:
        tabla.append(campo)
    # Fields of the gived list
    for campo in plus:
        tabla.append(campo)
    
    return tabla
    


# Show all records of a gived table by variable cursor1
def show_registers(conexion1,cursor_sql):
    flag = True
    cursor_sql=conexion1.cursor()
    for registro in cursor_sql:
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
def all_registers_to_csv(conexion1,cursor_sql,mask=[]):
    flag = True
    sentence = ""

    cursor_sql=conexion1.cursor()

    for registro in cursor_sql:
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



# Create a csv file to store the clients with its purchase records, depending on the status of the delivery
# The delivery status depends on the variable 'entregado'
# 'entregado' is 1, will show clients with purchases non yet delivered  (by default)
# 'entregado' is 0, will show clients with purchases already delivered  
def facturacion_clientes_to_csv(conexion_sql,entregado: int=1):
    if entregado==0 or entregado==1:
        cursor_sql=conexion_sql.cursor()

        cursor_sql.execute(f"SELECT \
                            clientes.nombre,\
                            clientes.apellidos,\
                            almacen.codigo_alm,\
                            pedidos.codigo_ped,\
                            pedidos.numero_ped,\
                            pedidos.pedido_cod_cli,\
                            pedidos.pedido_cod_alm, \
                            pedidos.fecha_hora,\
                            pedidos.vendedor,\
                            pedidos.cantidad,\
                            pedidos.precio_total, \
                            pedidos.entregado \
                            FROM clientes \
                            INNER JOIN pedidos ON clientes.codigo_cli = pedidos.pedido_cod_cli \
                            INNER JOIN almacen ON pedidos.pedido_cod_alm = almacen.codigo_alm \
                            WHERE pedidos.entregado={entregado} \
                            ORDER BY pedidos.pedido_cod_cli ASC;")   # Query of delivered purchase orders 
        
        tabla_np=[] # To store que query
        for register in cursor_sql: # Read all the query into 'tabla_np'
            tabla_np.append(register)
        tabla_np=np.array(tabla_np)
        
        if len(tabla_np)>0: # if at least there is one record 
            cabecera=np.array([['','NOMBRE','APELLIDOS','CODIGO_ALM','CODIGO_PED','NUMERO_PED','PEDIDO_COD_CLI','PEDIDO_COD_ALM','FECHA_HORA','VENDEDOR','CANTIDAD','PRECIO_TOTAL','ENTREGADO']])

            clientes=[] #Array of unique clients from the query
            for registro in tabla_np:   # Creating the list of all clients with a non delivered purchase order
                if registro[5] not in clientes: # Check field 6 where is the client ID. Only store unique values
                    clientes.append(registro[5])

            tabla_salida=[]
            for cliente in clientes:    # Creating a list of clients with their orders
                print(cliente)
                tabla_salida.append([cliente,'','','','','','','','','','','',''])    # The index is set by the cliente ID
                for registro in tabla_np:
                    if registro[5]==cliente:    # Check for the purchases owned by the client ID of the list
                        registro = np.insert(registro, 0,'')    # Insert a new column at the start
                        tabla_salida.append(registro)
                        print(registro)
                tabla_salida.append(['','','','','','','','','','','','',''])   # Add a empty line between clients

            
            tabla_salida_np=np.array(tabla_salida)

            tabla_salida_np=np.concatenate((cabecera, tabla_salida_np), axis=0)
            
            carpeta= r"C:/Proyectos_David/ficheros"    # For be used in windows class computer
            if entregado==0:
                fichero = "facturacion_clientes_entregados.csv"
            else:
                fichero = "facturacion_clientes_pendientes.csv"
            ruta = os.path.join(carpeta, fichero)
            ruta = os.path.abspath(ruta)

            np.savetxt(ruta, tabla_salida_np, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'])
        else:
            if entregado==0:
                print("No hay registros de clientes con pedidos entregados")
            else: 
                print("No hay registros de clientes con pedidos pendientes")        
            
    else:
        print("Error en la llamada de la función.  Revise los parámetros")