# Ejercicio 66 - Análisis de ventas de automóviles
# I. El fichero coches.csv contiene información sobre los modelos de automóviles vendidos en Estados Unidos 
# en un determinado año. Se pide:

# Crear un DataFrame a partir del fichero anterior.
# Eliminar las filas con valores desconocidos y mostrar el número de filas del dataframe resultante.
# Crear una columna con el precio en euros (cambio 1$ = 0.94€)
# Mostrar por pantalla las 10 últimas filas del DataFrame.
# Mostrar por pantalla el número de marcas que contiene el DataFrame.
# Mostrar por pantalla el número de modelos de cada marca que hay en el DataFrame, de mayor a menor frecuencia.
# Mostrar por pantalla la marca y el modelo del coche más caro.
# Mostrar por pantalla el precio medio en euros de los coches agrupando por marca y ordenando de menor a mayor precio.

# II. Imprimir por pantalla todos los resultados. Guardar el documento en tu carpeta como ejercicio_66.py


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
system("clear")   #Clear shell
print("#################################################     Ejercicio66      ######################################################")


#####################################################################################################################################
# Crear un DataFrame a partir del fichero anterior.
#####################################################################################################################################
carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio66"
fichero='coches.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df = pd.read_csv(ruta, sep=";", dtype="string")
print(df)


#####################################################################################################################################
# Eliminar las filas con valores desconocidos y mostrar el número de filas del dataframe resultante.
#####################################################################################################################################
df_coches = df.dropna(how='any')


#####################################################################################################################################
# Crear una columna con el precio en euros (cambio 1$ = 0.94€)
#####################################################################################################################################
df_coches['Precio_euros'] = df_coches['Precio'].astype(float) * 0.94


#####################################################################################################################################
# Mostrar por pantalla las 10 últimas filas del DataFrame.
#####################################################################################################################################
print(df_coches.tail(10),"\n")


#####################################################################################################################################
# Mostrar por pantalla el número de marcas que contiene el DataFrame.
#####################################################################################################################################
brands=df['Marca'].unique().tolist()
print(f"La cantidad de marcas de este dataframe es: {len(brands)}\n")


#####################################################################################################################################
# Mostrar por pantalla el número de modelos de cada marca que hay en el DataFrame, de mayor a menor frecuencia.
#####################################################################################################################################
count_models = df_coches.groupby('Marca')['Modelo'].nunique().sort_values(ascending=False)
print(count_models)


#####################################################################################################################################
# Mostrar por pantalla la marca y el modelo del coche más caro.
#####################################################################################################################################
max_price_index = df_coches['Precio'].idxmax()  #Get the index of the most expensive car
expensive = df_coches.loc[max_price_index]  # Get the information of that car
print(f"El coche más caro es: \n   {expensive}\n")


#####################################################################################################################################
# Mostrar por pantalla el precio medio en euros de los coches agrupando por marca y ordenando de menor a mayor precio.
#####################################################################################################################################
frequency_price = df_coches.groupby('Marca')['Precio_euros'].mean().round(2).sort_values(ascending=True)
print(frequency_price)

