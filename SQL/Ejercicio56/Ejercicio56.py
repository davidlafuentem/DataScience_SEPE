# II. Crear los siguientes procedimientos mostrando la salida de cada uno en un fichero .csv. 
# Obtener todos los datos solicitados a la base de datos mediante tablas usando los métodos 
# de la librería NumPy.

# FACTURACIÓN CLIENTES PENDIENTES: Mostrará la información del nombre y apellidos de la 
# tabla CLIENTES, el nombre del artículo de la tabla ALMACEN y todos los campos de la 
# tabla PEDIDOS ordenados y separados por CÓDIGO DE CLIENTE. La consulta mostrará solamente 
# aquellos pedidos QUE ESTÉN PENDIENTES DE ENTREGA.
# FACTURACIÓN CLIENTES ENTREGADOS: Mostrará la información del nombre y apellidos de la 
# tabla CLIENTES, el nombre del artículo de la tabla ALMACEN y todos los campos de la 
# tabla PEDIDOS ordenados y separados por CÓDIGO DE CLIENTE. La consulta mostrará solamente 
# aquellos pedidos QUE ESTÉN ENTREGADOS.
# TODOS LOS FICHEROS SERAN CSV Y CON ENCABEZADOS.

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
print("#################################################     Ejercicio56      ######################################################")

##############################################################################################################################
# FACTURACIÓN CLIENTES PENDIENTES: Mostrará la información del nombre y apellidos de la 
# tabla CLIENTES, el nombre del artículo de la tabla ALMACEN y todos los campos de la 
# tabla PEDIDOS ordenados y separados por CÓDIGO DE CLIENTE. La consulta mostrará solamente 
# aquellos pedidos QUE ESTÉN PENDIENTES DE ENTREGA.
##############################################################################################################################
conexion1=mysql.connector.connect(host="192.168.1.190", user="alumno", passwd="mipassword")
cursor_sql=conexion1.cursor()
cursor_sql.execute("USE ejercicio55;")

print("Clientes que aún no han recibido su pedido:")
facturacion_clientes_to_csv(conexion1,1)
conexion1.close()

##############################################################################################################################
# FACTURACIÓN CLIENTES ENTREGADOS: Mostrará la información del nombre y apellidos de la 
# tabla CLIENTES, el nombre del artículo de la tabla ALMACEN y todos los campos de la 
# tabla PEDIDOS ordenados y separados por CÓDIGO DE CLIENTE. La consulta mostrará solamente 
# aquellos pedidos QUE ESTÉN ENTREGADOS.
##############################################################################################################################
conexion2=mysql.connector.connect(host="192.168.1.190", user="alumno", passwd="mipassword")
cursor_sql=conexion2.cursor()
cursor_sql.execute("USE ejercicio55;")

print("Clientes que ya han recibido su pedido:")
facturacion_clientes_to_csv(conexion2,0)
conexion2.close()
