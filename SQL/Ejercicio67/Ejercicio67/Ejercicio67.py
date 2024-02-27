# Ejercicio 67 - Estudio de utilización de Airbnb en Madrid desde GitHub (actividad de evaluación)
# I. El objetivo de este trabajo es comprobar si se está utilizando la plataforma Airbnb por parte de empresas, 
# en lugar de particulares, para alquiler turístico en el centro de Madrid.

# Los datos detallados acerca del alojamiento se encuentran en varios ficheros alojados en GitHub.

# Fichero para crear la tabla a usar desde el Apartado 1:


# https://gitfront.io/r/inboxdatascience/aE9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado1.csv

# Extraer del fichero de alojamientos una lista con todos los alojamientos, donde cada alojamiento sea un 
# diccionario que contenga el identificador del alojamiento, el identificador del anfitrión, el distrito, el 
# precio y las plazas.
# Crear una función que reciba la lista de alojamientos y devuelva el número de alojamientos en cada distrito.
# Crear una función que reciba la lista de alojamientos y un número de ocupantes y devuelva la lista de 
# alojamientos con un número de plazas mayor o igual que el número de ocupantes.
# Crear una función que reciba la lista de alojamientos, un distrito, y devuelva los 10 alojamientos más 
# baratos del distrito.
# Crear una función que reciba la lista de alojamientos y devuelva un diccionario con los anfitriones y el 
# número de alojamientos que posee cada uno.

# Fichero para crear la tabla a usar desde el Apartado 6:
# https://gitfront.io/r/inboxdatascience/aE9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado6.csv

# Extraer el fichero de alojamientos para crear un data frame con los campos id, anfitrión, url, tipo_alojamiento, 
# distrito, precio, gastos_limpieza, plazas, noches_minimas, puntuacion y precio_persona (incluye los gastos 
# de limpieza).
# Crear una función que reciba una lista de distritos y devuelva un diccionario con los tipos de alojamiento en 
# ese distrito y el porcentaje de alojamientos de ese tipo.

# Crear una función que reciba una lista de distritos y devuelva un diccionario con el número de alojamientos 
# que cada anfitrión ofrece en esos distrito, ordenado de más a menos alojamientos.

# Crear una función que reciba una lista de distritos y devuelva un diccionario con el número medio de 
# alojamientos por anfitrión de cada distrito.

# II. Crear un fichero de salida .CSV para cada apartado. Guardar el documento en tu carpeta como ejercicio_67.py



import os
import csv
import operator
from os import system
import pandas as pd
import funciones_externas
from funciones_externas import *
import ssl                                          # For work with GitHub
from urllib.request import urlopen                  # For work with GitHub
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio67      ######################################################")


#####################################################################################################################################
# https://gitfront.io/r/inboxdatascience/aE9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado1.csv
# Extraer del fichero de alojamientos una lista con todos los alojamientos, donde cada alojamiento sea un 
# diccionario que contenga el identificador del alojamiento, el identificador del anfitrión, el distrito, el 
# precio y las plazas.
#####################################################################################################################################
ssl._create_default_https_context = ssl._create_unverified_context #Set off SSL certify certification

df_file= pd.read_csv('https://gitfront.io/r/inboxdatascience/aE9DCzQ7R1Sc/pythonfiles/raw/madrid-airbnb-listings-apartado1.csv', sep=';', decimal=',',index_col='id')

df_file['precio']=df_file['precio'].astype('string').str[1:]  # Eliminate the symbol '$' in 'precio' column
df_inmuebles=df_file
print(df_inmuebles)

dic_file=df_file.to_dict(orient='index')    # Transform into a dictionary
print(f"{dic_file}\n")



#####################################################################################################################################
# Crear una función que reciba una lista de distritos y devuelva un diccionario con los tipos de alojamiento en 
# ese distrito y el porcentaje de alojamientos de ese tipo.
#####################################################################################################################################
print("Porcentaje de tipos de alojamientos por distrito")
lista_distritos=['Chamartín','Arganzuela','Centro']

def percentage_of_house_types (district_list):
    dic_districts={}

    for district in district_list:
        dic_districts[district] = {}

        houses_quantity=df_inmuebles[df_inmuebles['distrito']==district].count()['distrito']
        df_distrito=df_inmuebles[df_inmuebles['distrito']==district]    # Dataframe of the houses in the given 'district'
        type_houses=df_distrito.groupby('plazas')['distrito'].count()   # Group by 'plazas' and them count them
        type_houses_percentage=round(type_houses*100/houses_quantity,2)
        
        dic_type_houses_percentage=type_houses_percentage.to_dict()
        dic_districts[district] = dic_type_houses_percentage
 
    # As 'dic_districts' is a dictionary of dictionaries, it's necessary to create a row for every key, and
    # them transmorf the value that it is a dictionary into a column for each sub_key and its value in the key row  
    with open('percentage_houses_by_host.csv', 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for key, value in dic_districts.items():    # 'value' is a dictionary
            list_sub_key=["Distrito"]   # Creating an empty position to align type of houses with its percentage
            list_sub_value=[]
            for sub_key, sub_value in value.items():    # Run along keys and values of the gived dictionary 
                list_sub_key.append(sub_key)
                list_sub_value.append(sub_value)

            writer.writerow(list_sub_key)   # Head of the fichero
            list_sub_value.insert(0,key)    # Add 'key' (district) to readed values of the dictionary
            writer.writerow(list_sub_value) # Write district and its values

    return dic_districts

print(f"{percentage_of_house_types(lista_distritos)}")
print("\n")



#####################################################################################################################################
# Crear una función que reciba una lista de distritos y devuelva un diccionario con el número de alojamientos 
# que cada anfitrión ofrece en esos distrito, ordenado de más a menos alojamientos.
#####################################################################################################################################
print("Número de alojamientos por anfitrión de cada distrito")
output_list=[]

def houses_of_host(lista_distritos):
    dic_districts={}
    houses_of_host_list=[]

    for district in lista_distritos:
        host_list=df_inmuebles[df_inmuebles['distrito']==district]['anfitrion'].unique()    # List of hosts within 'distrito'
        for host in host_list:
            houses_of_host=df_inmuebles[(df_inmuebles['distrito']==district) & (df_inmuebles['anfitrion']==host)].count()['distrito']
            houses_of_host_list.append([host,houses_of_host])
        
        houses_of_host_list.sort(key=operator.itemgetter(1))    # Sort by the second possition
        dic_houses_of_host=dict(houses_of_host_list)
        dic_districts[district] = dic_houses_of_host

    # As 'dic_districts' is a dictionary of dictionaries, it's necessary to create a row for every key, and
    # them transmorf the value that it is a dictionary into a column for each sub_key and its value in the key row  
    with open('houses_of_host.csv', 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for key, value in dic_districts.items():    # 'value' is a dictionary
            list_sub_key=["Distrito"]   # Creating an empty position to align type of houses with its percentage
            list_sub_value=[]
            for sub_key, sub_value in value.items():    # Run along keys and values of the gived dictionary 
                list_sub_key.append(sub_key)
                list_sub_value.append(sub_value)

            writer.writerow(list_sub_key)   # Head of the fichero
            list_sub_value.insert(0,key)    # Add 'key' (district) to readed values of the dictionary
            writer.writerow(list_sub_value) # Write district and its values

    return dic_districts

print(houses_of_host(lista_distritos))
print("\n")



#####################################################################################################################################
# Crear una función que reciba una lista de distritos y devuelva un diccionario con el número medio de 
# alojamientos por anfitrión de cada distrito.
#####################################################################################################################################
print("Media de alojamientos por anfitrión en cada distrito")

def mean_houses_per_host(lista_distritos):
    output_list=[]

    for district in lista_distritos:
        houses_quantity=df_inmuebles[df_inmuebles['distrito']==district].count()['distrito']
        host_list=df_inmuebles[df_inmuebles['distrito']==district]['anfitrion'].unique()    # List of hosts within 'distrito'
        quantity_hosts=len(host_list)
        mean= round(houses_quantity/quantity_hosts,2)
        output_list.append([district,mean])

    dic_output=dict(output_list)

    with open('mean_houses_by_host.csv', 'w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for key, value in dic_output.items():
            writer.writerow([key, value])

    return dic_output

print(mean_houses_per_host(lista_distritos))

# II. Crear un fichero de salida .CSV para cada apartado. Guardar el documento en tu carpeta como ejercicio_67.py
