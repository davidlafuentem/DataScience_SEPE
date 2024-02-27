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
import funciones_externas
from funciones_externas import *
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas


#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
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

for i,registro in enumerate(tabla_np):
    if registro[5]=='':
        tabla_np[i][len(registro)-1]='nan' # Set to empty if the value found in column age is not a decimal
    elif registro[5].isdecimal():
        if float(registro[5])>=18:
            tabla_np[i][len(registro)-1]='1' # Set to one in the last column if the age is greater than 18
        else:
            tabla_np[i][len(registro)-1]='0'
    elif registro[5].isalpha:
        tabla_np[i][5]=float(registro[5])
        if float(tabla_np[i][5])>=18:
            tabla_np[i][len(registro)-1]='1' # Set to one in the last column if the age is greater than 18
        elif float(tabla_np[i][5])<18:
            tabla_np[i][len(registro)-1]='0' # Set to one in the last column if the age is greater than 18


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
tabla_salida.append(f"Las dimensiones de la tabla son: {tabla_np.ndim}")
tabla_salida.append(f"El núemro de datos que contine la tabla son: {tabla_np.shape[0]}")

cabeceras=list(cabeceras)
cabeceras.append('legal_age')
tabla_salida.append(f"Los nombres de sus columnas: {cabeceras}")

id_column = tabla_np[:, 0]    # Selection of 'Survived' column
filter_id_column = id_column=='148'
tabla_salida.append(f"Pasajero 148: {tabla_np[filter_id_column]}")
#tabla_salida.append(f"Pasajero 148: {tabla_np[147]}")



survived_column = tabla_np[:, 1]    # Selection of 'Survived' column
muertos = np.count_nonzero(survived_column == '0')  # Count cases that match with '0' (mean that he died)
supervivientes = np.count_nonzero(survived_column == '1') # Count cases that match with '1' (mean that he survived)
tabla_salida.append(["Porcentaje de personas muertas:", round(muertos*100/tabla_np.shape[0],2)])
tabla_salida.append(["Porcentaje de personas que sobrevivieron:", round(supervivientes*100/tabla_np.shape[0],2)])
tabla_salida.append(["Porcentaje de personas que sobrevivieron:", round(supervivientes*100/tabla_np.shape[0],2)])

class_column = tabla_np[:, 2]    # Selection of the 'Pclass' column

supervivientes_primera = np.count_nonzero((survived_column=='1') & (class_column=='1')) # Count cases that match with '1' (mean that he survived)
supervivientes_segunda = np.count_nonzero((survived_column=='1') & (class_column=='2')) # Count cases that match with '1' (mean that he survived)
supervivientes_tercera = np.count_nonzero((survived_column=='1') & (class_column=='3')) # Count cases that match with '1' (mean that he survived)
viajeros_primera = np.count_nonzero(class_column=='1') # Count cases that match with '1' (mean that he survived)
viajeros_segunda = np.count_nonzero(class_column=='2') # Count cases that match with '1' (mean that he survived)
viajeros_tercera = np.count_nonzero(class_column=='3') # Count cases that match with '1' (mean that he survived)

tabla_salida.append(f"Porcentaje de personas que sobrevivieron en primera: {round(supervivientes_primera*100/viajeros_primera,2)}")
tabla_salida.append(f"Porcentaje de personas que sobrevivieron en segunda: {round(supervivientes_segunda*100/viajeros_segunda,2)}")
tabla_salida.append(f"Porcentaje de personas que sobrevivieron en tercera: {round(supervivientes_tercera*100/viajeros_tercera,2)}")



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

tabla_salida.append(f"Media edad de las mujeres de primera clase: {round(suma_mujeres_primera/mujeres_primera,2)}")
tabla_salida.append(f"Media edad de las mujeres de segunda clase: {round(suma_mujeres_segunda/mujeres_segunda,2)}")
tabla_salida.append(f"Media edad de las mujeres de tercera clase: {round(suma_mujeres_tercera/mujeres_tercera,2)}")



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

tabla_salida.append(f"total_filtered_legal_age_colum: {total_filtered_legal_age_colum}")
tabla_salida.append(f"suma_supervivientes_legal_age_primera_clase: {round(suma_supervivientes_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)}")
tabla_salida.append(f"suma_supervivientes_no_legal_age_primera_clase: {round(suma_supervivientes_no_legal_age_primera_clase*100/suma_supervivientes_primera_clase,2)}")
tabla_salida.append(f"suma_supervivientes_legal_age_segunda_clase: {round(suma_supervivientes_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)}")
tabla_salida.append(f"suma_supervivientes_no_legal_age_segunda_clase: {round(suma_supervivientes_no_legal_age_segunda_clase*100/suma_supervivientes_segunda_clase,2)}")
tabla_salida.append(f"suma_supervivientes_legal_age_tercera_clase: {round(suma_supervivientes_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)}")
tabla_salida.append(f"suma_supervivientes_no_legal_age_tercera_clase: {round(suma_supervivientes_no_legal_age_tercera_clase*100/suma_supervivientes_tercera_clase,2)}")

carpeta= r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio57"    # For be used in windows class computer
fichero = "informe_titanic.csv"
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

np.savetxt(ruta, tabla_salida, delimiter=';', fmt=['%s'])


