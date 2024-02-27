# II. Crear las siguientes consultas mostrando la salida de cada una en un fichero .csv. 
# Obtener todos los datos solicitados a la base de datos mediante tablas usando los métodos de la librería NumPy.

# NOMBRES: Mostrar los datos de los clientes llamados “Manuel” ó “Antonio” que hayan hecho algún pedido, ordenados 
# por apellidos.
# ORENSANOS: Mostrar nombre, apellidos , teléfono, dirección y población de los clientes de Orense, con edades de 
# entre 25 y 35 años, ordenados por edad.
# SIN_TLF: Mostrar nombre y apellidos de los clientes que no tengan teléfono y hayan realizado pedidos
# CUANTOS: Contar la cantidad total de artículos que hay en el almacén, listado de los artículos donde se deben 
# realizar pedidos para reponer, y la suma total del stock.
# VALOR ALMACÉN: Valor total del stock del almacén descontando el valor de los stock de seguridad.
# PEDIDOS CLIENTES: Mostrará la información del nombre y apellidos de la tabla CLIENTES, el nombre del artículo 
# de la tabla ALMACEN y todos los campos de la tabla PEDIDOS en función del código de cliente solicitado. La 
# consulta mostrará solamente aquellos pedidos QUE ESTÉN PENDIENTES DE ENTREGA.
# TODOS LOS FICHEROS SERAN CSV Y CON ENCABEZADOS.

# III. Guardar el documento en tu carpeta como ejercicio_55.py

import os
import mysql.connector
import numpy as np
from os import system
import funciones_externas
from funciones_externas import *
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas


#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("cls")   #Clear shell
print("#################################################     Ejercicio55      ######################################################")

conexion1=mysql.connector.connect(host="192.168.1.190", user="alumno", passwd="mipassword")
cursor_sql=conexion1.cursor()
cursor_sql.execute("USE ejercicio55;")


# NOMBRES: Mostrar los datos de los clientes llamados “Manuel” ó “Antonio” que hayan hecho algún pedido, ordenados por apellidos.
cabecera=headers_to_csv('clientes',conexion1,cursor_sql)
cabecera=cabecera[:-1]+";"+headers_to_csv('pedidos',conexion1,cursor_sql)
linea=cabecera

cursor_sql.execute("SELECT * FROM clientes INNER JOIN pedidos WHERE (nombre='Manuel' OR nombre='Antonio') AND (codigo_cli=pedido_cod_cli);")

for register in cursor_sql:
    print(register)
    linea=linea+register
    
carpeta= r"C:/Proyectos_David/ficheros"    # For be used in windows class computer
fichero = "nombres.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(linea) 



# ORENSANOS: Mostrar nombre, apellidos , teléfono, dirección y población de los clientes de Orense, con edades de 
# entre 25 y 35 años, ordenados por edad.
# cabecera=["nombre;apellidos;teléfono;dirección;población\n"]
# linea=cabecera
cabecera=['nombre','apellidos','telefono','direccion','poblacion']
cursor_sql.execute("SELECT nombre,apellidos,telefono,direccion,poblacion,fecha_nac FROM clientes WHERE poblacion='Ourense';")
tabla=[]

for register in cursor_sql: # Read the information from the query
    tabla.append(register)
tabla=np.array(tabla)

hoy = date.today()  # Select the date of today for calculating the deltatimes
hoy_35 = hoy - relativedelta(years=35)  # Delta time of 35 years ago
hoy_25 = hoy - relativedelta(years=25)  # Delta time of 25 years ago

seleccion=[]
seleccion.append(cabecera)
for registro in tabla:
    if registro[5]<=hoy_25 and registro[5]>=hoy_35: # Check birthdate between 25 and 35 years
        seleccion.append(registro[:-1]) # Eliminate the last field, birth date, that it is not required

seleccion=np.array(seleccion)

fichero = "orensanos.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

np.savetxt(ruta, seleccion, delimiter=';', fmt=['%s','%s','%s', '%s','%s'])  



# SIN_TLF: Mostrar nombre y apellidos de los clientes que no tengan teléfono y hayan realizado pedidos
tabla=[]
tabla.append(['nombre','apellidos'])
cursor_sql.execute("SELECT clientes.nombre,clientes.apellidos FROM clientes INNER JOIN pedidos WHERE clientes.codigo_cli=pedidos.pedido_cod_cli AND (clientes.telefono='' OR clientes.telefono IS NULL);")
for register in cursor_sql: # Read the information from the query
    tabla.append(register)
tabla=np.array(tabla)

fichero = "sin_tlf.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

np.savetxt(ruta, tabla, delimiter=';', fmt=['%s','%s'])  



# CUANTOS: Contar la cantidad total de artículos que hay en el almacén, listado de los artículos donde se deben 
# realizar pedidos para reponer, y la suma total del stock.
table=[]
comprar=[]
stock=0

cursor_sql.execute("SELECT * FROM almacen;")
for register in cursor_sql: # Read the information from the query
    table.append(register)
table=np.array(table)

for register in table:
    if int(register[4])<int(register[5]):   # Check for the products that need  replenishment
        comprar.append(register)
        stock=stock+0    # if above security replenishment line, set stock as 0 because logistic 
    else:
        stock=stock+int(register[4])-int(register[5])    # Calculating the total stock
diferentes_productos=len(table)

lista=""
for elemento in comprar:
    lista=lista+"   "+str(elemento)+"\n"

line=f"Cantidad de productos diferentes en el almacén: {diferentes_productos}\n\
Stock total en almacén: {stock}\n\
Productos que hay que reponer: \n{lista}"

fichero = "cuantos.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(line)



# VALOR ALMACÉN: Valor total del stock del almacén descontando el valor de los stock de seguridad.
table=[]
total_dinero=0

cursor_sql.execute("SELECT * FROM almacen;")
for register in cursor_sql: # Read the information from the query
    if int(register[4])>int(register[5]):   # Check for the products that don't need replenishment
        total_dinero=total_dinero+(float(register[3])*(int(register[4])-int(register[5]))) # Substract

line=f"Total monetario inventariado: {total_dinero}"

fichero = "valor_almacen.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
with open(ruta, mode="w",encoding="latin-1") as archivo:   
    archivo.writelines(line)



# PEDIDOS CLIENTES: Mostrará la información del nombre y apellidos de la tabla CLIENTES, el nombre del artículo 
# de la tabla ALMACEN y todos los campos de la tabla PEDIDOS en función del código de cliente solicitado. La 
# consulta mostrará solamente aquellos pedidos QUE ESTÉN PENDIENTES DE ENTREGA.
flag=True
cliente=0

print("Introduzca el identificador de cliente (XXXXX) para buscar los pedidos pendientes")
    
while flag:
    flag=False
    cliente=prompt_int()
    
    if len(str(cliente))<=5:    # Check for correct length
        cliente = list(str(cliente))    # Transform into a list of the characters

        longitud = 5-len(cliente)
        for i in range(longitud):
            cliente.insert(0,'0')   # Refill with '0'
        
        cliente=''.join(cliente)    # Transform into a string
    else:
        print("Número incorrecto")
        flag=True   # Ask again a correct number

cursor_sql.execute(f"SELECT * FROM clientes WHERE codigo_cli='CLI{cliente}';")  # Check wharever exists the client
tabla=[]

for register in cursor_sql:
    tabla.append(register)       

if tabla:   # 'cliente' exists into the DB
    tabla=[]
    tabla.append(['nombre','apellidos','codigo_alm','codigo_ped','numero_ped','pedido_cod_cli','fecha_hora','vendedor','cantidad','precio_total'])
    
    cursor_sql.execute(f"SELECT \
                clientes.nombre,\
                clientes.apellidos,\
                almacen.codigo_alm,\
                pedidos.codigo_ped,\
                pedidos.numero_ped,\
                pedidos.pedido_cod_cli,\
                pedidos.fecha_hora,\
                pedidos.vendedor,\
                pedidos.cantidad,\
                pedidos.precio_total \
                FROM clientes \
                INNER JOIN pedidos ON clientes.codigo_cli = pedidos.pedido_cod_cli \
                INNER JOIN almacen ON pedidos.pedido_cod_alm = almacen.codigo_alm \
                WHERE pedidos.entregado=1 AND pedidos.pedido_cod_cli='CLI{cliente}';")   # Query of non delivered purchased order 
                
    for register in cursor_sql: # Read the information from the query
        tabla.append(register)    

    if len(tabla)>1:    # Check the quantity of records regardless of the header
        tabla=np.array(tabla)
        fichero = "pedidos_clientes.csv"
        ruta = os.path.join(carpeta, fichero)
        ruta = os.path.abspath(ruta)

        np.savetxt(ruta, tabla, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'])
    else:
        print(f"El cliente CLI{cliente} no tiene ningún pedido pendiente de entrega.")
else:
    print(f"El cliente CLI{cliente} no exite.")

                       

conexion1.close()

