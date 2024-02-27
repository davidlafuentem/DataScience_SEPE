# Ejercicio 63 - Primer análisis de emisiones contaminantes
# I. Los ficheros emisiones-2016.csv, emisiones-2017.csv, emisiones-2018.csv y emisiones-2019.csv, contienen 
# datos sobre las emisiones contaminantes en la ciudad de Madrid en los años 2016, 2017, 2018 y 2019 
# respectivamente. Los campos tienen la siguiente descripción:

# PROVINCIA: Indicador de la provincia de estudio (Madrid es el 28).
# MUNICIPIO: Indicador del municipio de estudio (Madrid capital es el 79).
# ESTACION: Indicador de la estación de la toma de datos.
# MAGNITUD: Tipo de contaminante detectado.
# PUNTO_MUESTREO: Código que define provincia, municipio, estación y lugar de muestreo.
# ANO: Año de muestreo
# MES: Mes de muestreo
# D01..D31: Día de muestreo
# V01..V31: Valor de contaminación diario
# Escribir un programa en Python con los siguientes requisitos:

# Generar un DataFrame con los datos de los cuatro ficheros.
# Generar un nuevo DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las 
# correspondientes a los días (D01..D31)
# Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo DATETIME).
# Ordenar el DataFrame por estaciones contaminantes y fecha.
# Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
# Crear una función que reciba el DataFrame, una estación, un contaminante y un rango de fechas y devuelva una 
# serie con las emisiones del contaminante dado en la estación y rango de fechas dado.


# III. Imprimir por pantalla todos los resultados. Guardar el documento en tu carpeta como ejercicio_63.py



import os
from os import system
import pandas as pd
import funciones_externas
from funciones_externas import *
import ssl
from urllib.request import urlopen
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
#system("clear")   #Clear shell
print("#################################################     Ejercicio63      ######################################################")


#####################################################################################################################################
# Generar un DataFrame con los datos de los cuatro ficheros.
#####################################################################################################################################
carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio63"
fichero='emisiones-2016.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2016 = pd.read_csv(ruta, sep=";", dtype="string")

fichero='emisiones-2017.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2017 = pd.read_csv(ruta, sep=";", dtype="string")

fichero='emisiones-2018.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2018 = pd.read_csv(ruta, sep=";", dtype="string")

fichero='emisiones-2019.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2019 = pd.read_csv(ruta, sep=";", dtype="string")

# Deled rows with invalid values, checking validation columns in 'row_validation'
# Select only rows where there is a 'V' tellings that its the god one
row_validation = ['V01', 'V02', 'V03', 'V04', 'V05', 'V06', 'V07', 'V08', 'V09', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31']
df_2016 = df_2016[df_2016[row_validation].eq('V').all(axis=1)]
df_2017 = df_2017[df_2017[row_validation].eq('V').all(axis=1)]
df_2018 = df_2018[df_2018[row_validation].eq('V').all(axis=1)]
df_2019 = df_2019[df_2019[row_validation].eq('V').all(axis=1)]

# After eliminate rows with 'N' values, confirmation columns are no longer needed
indices_a_eliminar = [0, 1, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
df_2016 = df_2016.drop(df_2016.columns[indices_a_eliminar], axis='columns')
df_2017 = df_2017.drop(df_2017.columns[indices_a_eliminar], axis='columns')
df_2018 = df_2018.drop(df_2018.columns[indices_a_eliminar], axis='columns')
df_2019 = df_2019.drop(df_2019.columns[indices_a_eliminar], axis='columns')

df=pd.concat([df_2016,df_2017,df_2018,df_2019]) # Concatenate all clean dataframes in just one
print(f"Concatenar los 4 dataFrames provenientes de los ficheros csv:\n {df.head()}\n")



#####################################################################################################################################
# Generar un nuevo DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES y las 
# correspondientes a los días (D01..D31)
#####################################################################################################################################
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
print(f"Selección columnas 'ESTACION', 'MAGNITUD', 'ANO', 'MES y pivotar por 'DIA':\n {df.head()}\n")



#####################################################################################################################################
# Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo DATETIME).
#####################################################################################################################################
#df['FECHA'] = date(int(df.loc[0,'ANO']), int(df.loc[0,'MES']), int(df.loc[0,'DIA'][1:]))

# for i in range(len(df)):  ## FUNCIONA PERO ES MUY INEFICIENTE EN CÁLCULO!!! ####
#     df.loc[i,'FECHA']=date(int(df.loc[i,'ANO']), int(df.loc[i,'MES']), int(df.loc[i,'DIA'][1:]))



df['DIA'] = df['DIA'].astype(str).str[1:]  # Elimnate the first character 'D' to use as a number
#df['DIA'] = df['DIA'].str.replace('D', '')  # Elimnate the first character 'D' to use as a number
fechas_str = (df['ANO'].astype(str) + '-' + df['MES'].astype(str) + '-' + df['DIA'].astype(str))

# Convertir las cadenas combinadas a objetos de fecha de Pandas
df['FECHA'] = pd.to_datetime(fechas_str, format="%Y-%m-%d", errors='coerce')



# Crear la nueva columna 'FECHA' usando las columnas 'ANO', 'MES' y 'DIA' convertidas a enteros
#df['FECHA'] = df.apply(lambda row: date(int(row['ANO']), int(row['MES']), row['DIA']), axis=1)



print(f"Añadir la columna 'FECHA':\n {df.head()}\n")



#####################################################################################################################################
# Ordenar el DataFrame por estaciones contaminantes y fecha.
#####################################################################################################################################
print(df.sort_values('ESTACION'))
print(f"Ordenación por columna 'ESTACION':\n {df.head()}\n")


print(df.sort_values('FECHA'))
print(f"Ordenación por columna 'FECHA':\n {df.head()}\n")


#####################################################################################################################################
# Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
#####################################################################################################################################
abailable_stations=df['ESTACION'].unique().tolist()
print(f"Estaciones disponibles: {abailable_stations}\n")

pollutants=df['MAGNITUD'].unique().tolist()
print(f"Contaminantes contrastados: {pollutants}\n")



#####################################################################################################################################
# Crear una función que reciba el DataFrame, una estación, un contaminante y un rango de fechas y devuelva una 
# serie con las emisiones del contaminante dado en la estación y rango de fechas dado.
#####################################################################################################################################
print("Escoja una estación, un contaminante y un rango de fechas (entre 01/01/2016 y 31/12/2019) para consultar")
flag=True
while flag:
    flag=False

    print(f"Posibles estaciones: {abailable_stations}")
    station=input("Escoja estación \n")
    station=station.lower().strip()
    if (station in abailable_stations):
        print(f"La estación escogida es: {station}")
        flag=False
    else:
        print("La estación escogida no es correcta.  Vuelva a intentarlo")
        flag=True    

flag=True
while flag:
    flag=False

    print(f"Posibles contaminantes: {pollutants}")
    contaminant=input("Escoja contaminante \n")
    contaminant=contaminant.lower().strip()
    if (contaminant in pollutants):
        print(f"El contaminante escogido es: {contaminant}")
        flag=False
    else:
        print("El contaminante escogido no es correcto.  Vuelva a intentarlo")
        flag=True  


min_date=pd.to_datetime("2016-1-1",format="%Y-%m-%d", errors='coerce')
max_date=pd.to_datetime("2019-12-31",format="%Y-%m-%d", errors='coerce')


flag=True
while flag:
    flag=False

    print("Escoja fecha de inicio. \n")
    start_date=prompt_date()

    if ((start_date>= min_date) and (start_date<=max_date)):
        print(f"La fecha escogida es: {start_date.date()}")
        flag=False
    else:
        print("La fecha es incorrecta o está fuera de rango ([2016-01-01 y 2019-12-31]).  Vuelva a intentarlo")
        flag=True  


flag=True
while flag:
    flag=False

    print("Escoja la fecha final. \n")
    final_date=prompt_date()

    if ((final_date>= min_date) and (final_date<=max_date)):
        print(f"La fecha escogida es: {final_date.date()}")
        flag=False
    else:
        print("La fecha es incorrecta o está fuera de rango ([2016-01-01 y 2019-12-31]).  Vuelva a intentarlo")
        flag=True  


result= report_estacion_magnitud_rango_periodo(df,station,contaminant,start_date,final_date)

if not result.empty:
    print(result.head(31))

