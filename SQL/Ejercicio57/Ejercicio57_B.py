# Añadir una nueva columna booleana a la tabla de la base de datos y rellenarla si el pasajero era menor de edad o no.
# Generar una base de datos en el servidor local y una tabla con los datos del fichero. Pasar la tabla desde el fichero a NumPy.
# Generar un fichero de datos con la siguiente información:
# Las dimensiones de la tabla, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las 
# columnas, las 10 primeras filas y las 10 últimas filas.
# Los datos del pasajero con identificador 148.
# Porcentaje de personas que sobrevivieron y murieron.
# Porcentaje de personas que sobrevivieron en cada clase.
# Edad media de las mujeres que viajaban en cada clase.
# Porcentaje de menores y mayores de edad que sobrevivieron en cada clase.


import os
import mysql.connector
import numpy as np
from os import system
from decimal import Decimal
import funciones_externas
from funciones_externas import *
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas


#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
#system("clear")   #Clear shell
print("#################################################     Ejercicio57      ######################################################")



#####################################################################################################################################
# Generar una base de datos en el servidor local y una tabla con los datos del fichero. 
# Pasar la tabla desde el fichero a NumPy.
#####################################################################################################################################
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor_sql=conexion1.cursor()

cursor_sql.execute("drop database if exists titanic;")
cursor_sql.execute("create database titanic character set latin1 collate latin1_spanish_ci;")
cursor_sql.execute("use titanic;")
cursor_sql.execute("create table trip (PassengerId int NOT NULL PRIMARY KEY, Survived boolean, Pclass int, Name varchar(50), Sex varchar(6), Age int, SibSp int, Parch int, Ticket varchar(12),Fare float,Cabin varchar(5),Embarked varchar(1));")

#carpeta= r"C:/Proyectos_David/ficheros"    # For be used in windows class computer
carpeta= r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio57"    # For be used in windows class computer
fichero = "titanic.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
#columnas_a_usar=(0,1,2,5,6,7,8,9,10,11,12)

tabla_np = np.loadtxt(ruta, dtype=str, delimiter=";",skiprows=1)

""" # name and the last name are split by a ',' like the delimiter, so the load create 
# to separated columns that need to be concatenated in just one column
tabla_nombre = np.loadtxt(ruta, dtype=str, usecols=(3,4),delimiter=";",skiprows=1)  # Extract both columns   

# Obtén las columnas que deseas concatenar
columna0 = tabla_nombre[:, 0] # All registers of the first column

for i,valor in enumerate(columna0):
     columna0[i]=valor[1:]+","  # Eliminate '"' at the start, and add ','

columna1 = tabla_nombre[:, 1]   # All register of the last column

columnas_concatenadas = np.core.defchararray.add(columna0, columna1) # Concatenate both columns

indice_columna_nueva = 3  # Position where include 'columnas_concatenadas' in
tabla_np = np.insert(tabla_np, indice_columna_nueva, columnas_concatenadas, axis=1)

 """
cabeceras = np.genfromtxt(ruta, dtype=str, delimiter=";", autostrip=True, skip_header=0, max_rows=1)



#####################################################################################################################################
# Añadir una nueva columna booleana a la tabla de la base de datos y rellenarla si el 
# pasajero era menor de edad o no.
#####################################################################################################################################
num_filas = tabla_np.shape[0]
nuevo_campo_vacio = np.full((num_filas, 1), np.nan) # Create a empty field of type nan
tabla_np = np.concatenate((tabla_np, nuevo_campo_vacio), axis=1)    # Add this empty field in each register
longitud_tabla_np=tabla_np.shape[1]
indice_col_legal_age=longitud_tabla_np-1

for i,registro in enumerate(tabla_np):
    if registro[5]=='':
        tabla_np[i][indice_col_legal_age]='nan' # Set to empty if the value found in column age is empty
    elif registro[5].isdigit():
        if float(registro[5])>=18:
            tabla_np[i][indice_col_legal_age]='1' # Set to one in the last column if the age is greater than 18
        else:
            tabla_np[i][indice_col_legal_age]='0'
    elif es_decimal(registro[5]):
        if float(tabla_np[i][5])>=18:
            tabla_np[i][indice_col_legal_age]='1' # Set to one in the last column if the age is greater than 18
        elif float(tabla_np[i][5])<18:
            tabla_np[i][indice_col_legal_age]='0' # Set to one in the last column if the age is greater than 18


#####################################################################################################################################
# Generar un fichero de datos con la siguiente información:
# Las dimensiones de la tabla, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las 
# columnas, las 10 primeras filas y las 10 últimas filas.
# Los datos del pasajero con identificador 148.
# Porcentaje de personas que sobrevivieron y murieron.
# Porcentaje de personas que sobrevivieron en cada clase.
# Edad media de las mujeres que viajaban en cada clase.
# Porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
#####################################################################################################################################
tabla_salida=[]
tabla_salida.append(["Las dimensiones de la tabla son:",tabla_np.ndim,'','','','','','','','','','','',''])
tabla_salida.append(["El núemro de datos que contine la tabla son:",tabla_np.shape[0],'','','','','','','','','','','',''])

# array_con_nueva_columna = np.insert(cabeceras, 11, 'lega_age', axis=1)
# print(cabeceras)


cabeceras=cabeceras.tolist()
cabeceras.append('legal_age')
linea=""
for value in cabeceras:
    linea=linea+value+","
linea=linea[:-1]

tabla_salida.append(["Los nombres de sus columnas:", linea,'','','','','','','','','','','',''])

id_column = tabla_np[:, 0]    # Selection of identification column column
filter_id_column = (id_column=='148')   # Specific selection
linea=""
register=tabla_np[filter_id_column]

for value in register[0]:  # Transform each field into a string
    linea=linea+value+","
linea=linea[:-1]    #Eliminate last coma
tabla_salida.append(["Pasajero 148:",linea,'','','','','','','','','','','',''])

#tabla_salida.append(f"Pasajero 148: {tabla_np[147])



# Porcentaje de personas que sobrevivieron y murieron.
survived_column = tabla_np[:, 1]    # Selection of 'Survived' column
tabla_salida.append(["Porcentaje de supervivientes:", round((survived_column=='1').mean()*100,2)])
tabla_salida.append(["Porcentaje de muertos:", round((survived_column=='0').mean()*100,2)])



# Porcentaje de personas que sobrevivieron en cada clase.
class_column = tabla_np[:, 2]    # Selection of the 'Pclass' column
legal_age_column = tabla_np[:, (len(tabla_np[0])-1)]    # Selection of the last column, 'legal_age'

filter_survivors_primera= ((survived_column=='1') & (class_column=='1'))
filter_no_survivors_primera= ((survived_column=='0') & (class_column=='1'))

proporcion_supervivientes_primera = np.mean(np.sum((class_column[filter_survivors_primera]).dtype(float)))
proporcion_no_supervivientes_primera = round(np.mean(filter_no_survivors_primera),2)
viajeros_primera=np.count_nonzero(class_column=='1')

print(f"proporcion_supervivientes_primera: {proporcion_supervivientes_primera}")
print(f"proporcion_no_supervivientes_primera: {proporcion_no_supervivientes_primera}")
print(f"casos_supervivientes_primera: {np.count_nonzero(filter_survivors_primera)}")
print(f"casos_no_supervivientes_primera: {np.count_nonzero(filter_no_survivors_primera)}")


supervivientes_primera=np.count_nonzero(filter_survivors_primera)
no_supervivientes_primera=np.count_nonzero(filter_no_survivors_primera)

print(f"supervivientes_primera: {supervivientes_primera}")
print(f"no_supervivientes_primera: {no_supervivientes_primera}")
print(f"total_primera: {viajeros_primera}")
#cantidad supervivientes primera clase	136casos	62,96%
#cantidad muertos primera clase			80casos	    37,04%
#total personas en primera 			    216casos	






# Edad media de las mujeres que viajaban en cada clase.
age_column = tabla_np[:, 5]    # Selection of the 'Age' column

filter_decimals = np.char.find(age_column, ',') != -1   # Detect csv decimals by the coma, and creat a filter
age_column[filter_decimals] = np.char.replace(age_column[filter_decimals], ',', '.')    # Convert all of them in python decimal

sex_column = tabla_np[:,4]   # Selection of the 'Sex' column
filter_mujer_primera = (sex_column == 'female') & (class_column == '1') & (age_column != 'nan') & (age_column !='') # Filter for female of first class
filter_mujer_segunda = (sex_column == 'female') & (class_column == '2') & (age_column != 'nan') & (age_column !='') # Filter for female of first class
filter_mujer_tercera = (sex_column == 'female') & (class_column == '3') & (age_column != 'nan') & (age_column !='') # Filter for female of first class

tabla_salida.append(["Media edad de las mujeres de primera clase:", str(round(np.mean(age_column[filter_mujer_primera].astype(float)),2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Media edad de las mujeres de segunda clase:", str(round(np.mean(age_column[filter_mujer_segunda].astype(float)),2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Media edad de las mujeres de tercera clase:", str(round(np.mean(age_column[filter_mujer_tercera].astype(float)),2)).replace('.',','),'','','','','','','','','','','',''])



# Porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
id_column = tabla_np[:, 0]    # Selection of the 'PassengerId' column

filter_legal_age_colum = ((legal_age_column != 'nan') & (legal_age_column !='')) # Eliminate bad values
filtered_legal_age_colum = id_column[filter_legal_age_colum]
total_filtered_legal_age_colum = np.count_nonzero(filtered_legal_age_colum)

filter_legal_age_primera_clase=((legal_age_column == '1')  & (survived_column == '1') & (class_column=='1')) # Eliminate bad values)
filter_no_legal_age_primera_clase=((legal_age_column == '0') & (survived_column == '1') & (class_column=='1')) # Eliminate bad values)
filter_legal_age_segunda_clase=((legal_age_column == '1') & (survived_column == '1') & (class_column=='2')) # Eliminate bad values)
filter_no_legal_age_segunda_clase=((legal_age_column == '0') & (survived_column == '1') & (class_column=='2')) # Eliminate bad values)
filter_legal_age_tercera_clase=((legal_age_column == '1') & (survived_column == '1') & (class_column=='3')) # Eliminate bad values)
filter_no_legal_age_tercera_clase=((legal_age_column == '0') & (survived_column == '1') & (class_column=='3')) # Eliminate bad values)


suma_supervivientes_legal_age_primera_clase=np.count_nonzero(id_column[filter_legal_age_primera_clase])
suma_supervivientes_no_legal_age_primera_clase=np.count_nonzero(id_column[filter_no_legal_age_primera_clase])
suma_supervivientes_primera_clase=suma_supervivientes_legal_age_primera_clase+suma_supervivientes_no_legal_age_primera_clase

print(f"Porcentaje de mayores supervivientes de primera: {str(round(np.mean(legal_age_column[filter_legal_age_primera_clase].astype(float)),2))}")
print(f"Porcentaje de mayores supervivientes de primera: {str(round(np.mean(legal_age_column[filter_no_legal_age_primera_clase].astype(float)),2))}")


suma_supervivientes_legal_age_segunda_clase=np.count_nonzero(id_column[filter_legal_age_segunda_clase])
suma_supervivientes_no_legal_age_segunda_clase=np.count_nonzero(id_column[filter_no_legal_age_segunda_clase])
suma_supervivientes_segunda_clase=suma_supervivientes_legal_age_segunda_clase+suma_supervivientes_no_legal_age_segunda_clase

suma_supervivientes_legal_age_tercera_clase=np.count_nonzero(id_column[filter_legal_age_tercera_clase])
suma_supervivientes_no_legal_age_tercera_clase=np.count_nonzero(id_column[filter_no_legal_age_tercera_clase])
suma_supervivientes_tercera_clase=suma_supervivientes_legal_age_tercera_clase+suma_supervivientes_no_legal_age_tercera_clase


tabla_salida.append(["Porcentaje_supervivientes_legal_age_primera_clase:", str(round(suma_supervivientes_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje_supervivientes_no_legal_age_primera_clase:", str(round(suma_supervivientes_no_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje_supervivientes_legal_age_segunda_clase:", str(round(suma_supervivientes_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje_supervivientes_no_legal_age_segunda_clase:", str(round(suma_supervivientes_no_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje_supervivientes_legal_age_tercera_clase:", str(round(suma_supervivientes_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje_supervivientes_no_legal_age_tercera_clase:", str(round(suma_supervivientes_no_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)).replace('.',','),'','','','','','','','','','','',''])


# First 10 lines + last 10 lines of the BD titanic
array_diez_primeras_filas=tabla_np[:10]
array_diez_ultimas_filas=tabla_np[-10:]
num_filas = 10

#tabla_salida.append(np.concatenate((array_diez_primeras_filas, nuevo_campo_vacios), axis=1))
#tabla_salida.append(np.concatenate((array_diez_ultimas_filas, nuevo_campo_vacios), axis=1))

tabla_salida=np.array(tabla_salida)
nuevo_campo_vacios = np.full((num_filas, 1), '')    #Add an empty column for 10 registers

temporal=np.concatenate((array_diez_primeras_filas, nuevo_campo_vacios), axis=1) # Concatenate with the empty column
tabla_salida=np.concatenate((tabla_salida,temporal), axis=0)  # Add this table below the last line

temporal=np.concatenate((array_diez_ultimas_filas, nuevo_campo_vacios), axis=1)
tabla_salida=np.concatenate((tabla_salida,temporal), axis=0)  # Add this empty field in each register

for registro in tabla_salida:
    print(registro)




carpeta= r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio57"    # For be used in windows class computer
fichero = "informe_titanic.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

np.savetxt(ruta, tabla_salida, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'])

