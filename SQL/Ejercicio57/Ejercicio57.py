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
columnas_a_usar=(0,1,2,5,6,7,8,9,10,11,12)
tabla_np = np.loadtxt(ruta, dtype=str, usecols=columnas_a_usar,delimiter=";",skiprows=1)
# name and the last name are split by a ',' like the delimiter, so the load create 
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

cabeceras = np.genfromtxt(ruta, dtype=str, delimiter=",", autostrip=True, skip_header=0, max_rows=1)



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
    elif registro[5].isdecimal():
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

cabeceras=list(cabeceras)
cabeceras.append('legal_age')


lista=""
for value in cabeceras:
    lista=lista+value+","
lista=lista[:-1]

tabla_salida.append(["Los nombres de sus columnas:", lista,'','','','','','','','','','','',''])

id_column = tabla_np[:, 0]    # Selection of 'Survived' column
filter_id_column = id_column=='148'

lista=""
for register in tabla_np[filter_id_column]:
    for value in register:
        lista=lista+value+","

lista=lista[:-1]    #Eliminate last coma
tabla_salida.append(["Pasajero 148:",lista,'','','','','','','','','','','',''])

#tabla_salida.append(f"Pasajero 148: {tabla_np[147])



survived_column = tabla_np[:, 1]    # Selection of 'Survived' column
muertos = np.count_nonzero(survived_column == '0')  # Count cases that match with '0' (mean that he died)
supervivientes = np.count_nonzero(survived_column == '1') # Count cases that match with '1' (mean that he survived)
tabla_salida.append(["Porcentaje de personas muertas:", str(round(muertos*100/tabla_np.shape[0],2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje de personas que sobrevivieron:", str(round(supervivientes*100/tabla_np.shape[0],2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje de personas que sobrevivieron:", str(round(supervivientes*100/tabla_np.shape[0],2)).replace('.',','),'','','','','','','','','','','',''])

class_column = tabla_np[:, 2]    # Selection of the 'Pclass' column

supervivientes_primera = np.count_nonzero((survived_column=='1') & (class_column=='1')) # Count cases that match with '1' (mean that he survived)
supervivientes_segunda = np.count_nonzero((survived_column=='1') & (class_column=='2')) # Count cases that match with '1' (mean that he survived)
supervivientes_tercera = np.count_nonzero((survived_column=='1') & (class_column=='3')) # Count cases that match with '1' (mean that he survived)
viajeros_primera = np.count_nonzero(class_column=='1') # Count cases that match with '1' (mean that he survived)
viajeros_segunda = np.count_nonzero(class_column=='2') # Count cases that match with '1' (mean that he survived)
viajeros_tercera = np.count_nonzero(class_column=='3') # Count cases that match with '1' (mean that he survived)

tabla_salida.append(["Porcentaje de personas que sobrevivieron en primera:", str(round(supervivientes_primera*100/viajeros_primera,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje de personas que sobrevivieron en segunda:", str(round(supervivientes_segunda*100/viajeros_segunda,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Porcentaje de personas que sobrevivieron en tercera:", str(round(supervivientes_tercera*100/viajeros_tercera,2)).replace('.',','),'','','','','','','','','','','',''])



# Edad media de las mujeres que viajaban en cada clase.
age_column = tabla_np[:, 5]    # Selection of the 'Age' column
filter_age_column_number = ((age_column != 'nan') & (age_column !='')) # Eliminate bad values
age_column_filtered = age_column[filter_age_column_number]  # Execute filter to get only numeric values

age_column_filtered_as_float=age_column_filtered.astype(float)   # Casting all ages to float type

sex_column = tabla_np[:,4]   # Selection of the 'Sex' column

filter_mujer = (sex_column == 'female') & filter_age_column_number # Filter for female 
filter_mujer_primera = filter_mujer & (class_column == '1') # Filter for female of first class
filter_mujer_segunda = filter_mujer & (class_column == '2') # Filter for female of second class
filter_mujer_tercera = filter_mujer & (class_column == '3') # Filter for female of third class

mujeres_primera = np.count_nonzero(age_column[filter_mujer_primera]) # Number of womans in 1st 
mujeres_segunda = np.count_nonzero(age_column[filter_mujer_segunda]) # Number of womans in 2nd
mujeres_tercera = np.count_nonzero(age_column[filter_mujer_tercera]) # Number of womans in 3th

age_column_floats_primera = age_column[filter_mujer_primera].astype(float) # Female 1st casting
age_column_floats_segunda = age_column[filter_mujer_segunda].astype(float) # Female 2nd casting
age_column_floats_tercera = age_column[filter_mujer_tercera].astype(float) # Female 3th casting

suma_mujeres_primera = np.sum(age_column_floats_primera) # Sum of ages of female 1st class
suma_mujeres_segunda = np.sum(age_column_floats_segunda) # Sum of ages of female 2nd class
suma_mujeres_tercera = np.sum(age_column_floats_tercera) # Sum of ages of female 3th class

tabla_salida.append(["Media edad de las mujeres de primera clase:", str(round(suma_mujeres_primera/mujeres_primera,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Media edad de las mujeres de segunda clase:", str(round(suma_mujeres_segunda/mujeres_segunda,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["Media edad de las mujeres de tercera clase:", str(round(suma_mujeres_tercera/mujeres_tercera,2)).replace('.',','),'','','','','','','','','','','',''])



# Porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
legal_age_column = tabla_np[:, (len(tabla_np[0])-1)]    # Selection of the 'legal_age' column
id_column = tabla_np[:, 0]    # Selection of the 'PassengerId' column
filter_legal_age_colum = ((legal_age_column != 'nan') & (legal_age_column !='')) # Eliminate bad values)
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

suma_supervivientes_legal_age_segunda_clase=np.count_nonzero(id_column[filter_legal_age_segunda_clase])
suma_supervivientes_no_legal_age_segunda_clase=np.count_nonzero(id_column[filter_no_legal_age_segunda_clase])
suma_supervivientes_segunda_clase=suma_supervivientes_legal_age_segunda_clase+suma_supervivientes_no_legal_age_segunda_clase

suma_supervivientes_legal_age_tercera_clase=np.count_nonzero(id_column[filter_legal_age_tercera_clase])
suma_supervivientes_no_legal_age_tercera_clase=np.count_nonzero(id_column[filter_no_legal_age_tercera_clase])
suma_supervivientes_tercera_clase=suma_supervivientes_legal_age_tercera_clase+suma_supervivientes_no_legal_age_tercera_clase


tabla_salida.append(["suma_supervivientes_legal_age_primera_clase:", str(round(suma_supervivientes_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["suma_supervivientes_no_legal_age_primera_clase:", str(round(suma_supervivientes_no_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["suma_supervivientes_legal_age_segunda_clase:", str(round(suma_supervivientes_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["suma_supervivientes_no_legal_age_segunda_clase:", str(round(suma_supervivientes_no_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["suma_supervivientes_legal_age_tercera_clase:", str(round(suma_supervivientes_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)).replace('.',','),'','','','','','','','','','','',''])
tabla_salida.append(["suma_supervivientes_no_legal_age_tercera_clase:", str(round(suma_supervivientes_no_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)).replace('.',','),'','','','','','','','','','','',''])


# First 10 lines + last 10 lines of the BD titanic
array_diez_primeras_filas=tabla_np[:10]
array_diez_ultimas_filas=tabla_np[-10:]
num_filas = 10



#tabla_salida.append(np.concatenate((array_diez_primeras_filas, nuevo_campo_vacios), axis=1))
#tabla_salida.append(np.concatenate((array_diez_ultimas_filas, nuevo_campo_vacios), axis=1))

tabla_salida=np.array(tabla_salida)
nuevo_campo_vacios = np.full((num_filas, 1), '')

temporal=np.concatenate((array_diez_primeras_filas, nuevo_campo_vacios), axis=1)
tabla_salida=np.concatenate((tabla_salida,temporal), axis=0)  # Add this empty field in each register

temporal=np.concatenate((array_diez_ultimas_filas, nuevo_campo_vacios), axis=1)
tabla_salida=np.concatenate((tabla_salida,temporal), axis=0)  # Add this empty field in each register

for registro in tabla_salida:
    print(registro)




carpeta= r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio57"    # For be used in windows class computer
fichero = "informe_titanic.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

np.savetxt(ruta, tabla_salida, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'])


