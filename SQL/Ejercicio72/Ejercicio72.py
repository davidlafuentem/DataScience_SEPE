# Ejercicio 72 - Análisis del endeudamiento público por países (actividad de evaluación)
# I. El objetivo de este trabajo es hacer un análisis del endeudamiento público por países de los últimos 25 años antes de la pandemia 
# de COVID-19. Para ello disponemos de un fichero en la siguiente ruta pública de Google Drive:

# Conjunto de datos del banco mundial 1995-2019:


# Deuda pública por países y cuatrimestres 
# El formato de fecha es año (yyyy) + Q + trimestre (1, 2, 3 o 4)

# Procedimientos a realizar:

# Procesar el fichero de deuda pública por países para obtener un dataframe con el ID de país, el ID del tipo de deuda, la fecha y la 
# cantidad de deuda.
# Crear una función que reciba un país y una fecha y devuelva un diccionario con la deuda total interna, externa, en moneda local, en 
# moneda extranjera, a corto plazo y a largo plazo, de ese país en esa fecha.
# Crear una función que reciba un tipo de deuda y una fecha, y devuelva un diccionario con la deuda de ese tipo de todos los países en 
# esa fecha.
# Crear una función que reciba un país y una fecha y dibuje un diagrama de sectores con la deuda interna y la deuda externa de ese país 
# en esa fecha.
# Crear una función que reciba un país y una fecha, y dibuje un diagrama de barras con las cantidades de los distintos tipos de deudas 
# de ese país en esa fecha.
# Crear una función que reciba una lista de 4 países y un tipo de deuda y dibuje un diagrama de líneas con la evolución de ese tipo de 
# deuda de esos países (una línea por país).
# Crear una función que reciba un país y una lista de 3 tipos de deuda y dibuje un diagrama de líneas con la evolución de esos tipos de 
# deuda de ese país (una línea por tipo de deuda).
# Crear una función que reciba una lista de 4 países y una lista de  3 tipos de deuda, y dibuje un diagrama de cajas con las deudas de 
# esos tipos de esos países (una caja por país y tipo de deuda).
# Ficheros a generar:

# La función de creación del dataframe y las llamadas a las funciones de los apartados estarán en un fichero llamado ejercicio_72.py

# Todas las demás funciones deberán estar en un fichero externo, llamado ejercicio_72_funciones.py

# Las funciones 2 y 3 deberán generar automáticamente un fichero .CSV de salida de datos, aparte de mostrarlos en pantalla para su 
# verificación.

# Las funciones 4, 5, 6, 7 y 8 deberán generar automáticamente los ficheros de las imágenes de los diagramas, aparte de mostrarlos en 
# pantalla para su verificación.

# II. Crear un fichero de salida .ZIP con las imágenes de los diagramas, las funciones, los ficheros .CSV de salida y el programa. 
# Guardar el documento en tu carpeta como ejercicio_72.zip y subirlo a la plataforma.



import os
import ssl
import pandas as pd
from os import system
import funciones_externas
from funciones_externas import *
import matplotlib
matplotlib.use('macosx')
# matplotlib.use('qtagg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from urllib.request import urlopen
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio72      ######################################################")

carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio72"
fichero='listado_deudas_paises.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_file=pd.read_csv(ruta,sep=';',dtype="string",encoding='latin-1')

df_file['Cantidad']=df_file['Cantidad'].astype(str).str.replace(',','.')    # Transform to use as a float
df_file['Fecha']=df_file['Fecha'].astype(str).str[:4]   # Clean the quarter

df_debt=df_file


#####################################################################################################################################
# Procesar el fichero de deuda pública por países para obtener un dataframe con el ID de país, el ID del tipo de deuda, la fecha y la 
# cantidad de deuda.
#####################################################################################################################################

df_debt= df_debt[['PaisId','TipoId','Fecha','Cantidad']]
print(df_debt)





#####################################################################################################################################
# Crear una función que reciba un país y una fecha y devuelva un diccionario con la deuda total interna, externa, en moneda local, en 
# moneda extranjera, a corto plazo y a largo plazo, de ese país en esa fecha.
#####################################################################################################################################
def total_debt_in_a_year(country,year):
    


#####################################################################################################################################
# Crear una función que reciba un tipo de deuda y una fecha, y devuelva un diccionario con la deuda de ese tipo de todos los países en 
# esa fecha.
# Las funciones 2 y 3 deberán generar automáticamente un fichero .CSV de salida de datos, aparte de mostrarlos en pantalla para su 
# verificación.
#####################################################################################################################################

#####################################################################################################################################
# Crear una función que reciba un país y una fecha y dibuje un diagrama de sectores con la deuda interna y la deuda externa de ese país 
# en esa fecha.
# Las funciones 2 y 3 deberán generar automáticamente un fichero .CSV de salida de datos, aparte de mostrarlos en pantalla para su 
# verificación.
#####################################################################################################################################
# Crear una función que reciba un país y una fecha, y dibuje un diagrama de barras con las cantidades de los distintos tipos de deudas 
# de ese país en esa fecha.
# Crear una función que reciba una lista de 4 países y un tipo de deuda y dibuje un diagrama de líneas con la evolución de ese tipo de 
# deuda de esos países (una línea por país).
# Crear una función que reciba un país y una lista de 3 tipos de deuda y dibuje un diagrama de líneas con la evolución de esos tipos de 
# deuda de ese país (una línea por tipo de deuda).
# Crear una función que reciba una lista de 4 países y una lista de  3 tipos de deuda, y dibuje un diagrama de cajas con las deudas de 
# esos tipos de esos países (una caja por país y tipo de deuda).
# Ficheros a generar:

# La función de creación del dataframe y las llamadas a las funciones de los apartados estarán en un fichero llamado ejercicio_72.py

# Todas las demás funciones deberán estar en un fichero externo, llamado ejercicio_72_funciones.py

# Las funciones 2 y 3 deberán generar automáticamente un fichero .CSV de salida de datos, aparte de mostrarlos en pantalla para su 
# verificación.

# Las funciones 4, 5, 6, 7 y 8 deberán generar automáticamente los ficheros de las imágenes de los diagramas, aparte de mostrarlos en 
# pantalla para su verificación.







"""

#####################################################################################################################################
# Crear una función que dibuje un diagrama de barras con el número de alojamientos por distritos.
#####################################################################################################################################

def houses_by_district(district_list):
    outputy=[]

    for district in district_list:
        houses_quantity=df_inmuebles[df_inmuebles['distrito']==district]['distrito'].count()
        outputy.append(houses_quantity)

    return outputy


def plot_houses_by_district(district_list):
    houses_by_district_list=[]
    houses_by_district_list=houses_by_district(district_list)

    plt.figure(figsize=(10, 6))
    plt.bar(district_list,houses_by_district_list, color='#0dbb75',edgecolor='#df7312')
    for i,n in enumerate(houses_by_district_list):
            plt.text(i,n,n,ha='center',va='bottom')

    plt.xlabel('Distrito')
    plt.ylabel('Cantidad de casas')
    plt.title('Cantidad de Casas por Distrito')
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    plt.get_backend() 
    plt.savefig('plot_houses_by_district.png')
    plt.show()

plot_houses_by_district(lista_distritos)


#####################################################################################################################################
# Crear una función que dibuje un diagrama de barras con los porcentajes acumulados de tipos de 
# alojamientos por distritos.
#####################################################################################################################################
def plot_percentage_of_house_types(district_list):
    for district in district_list:
        houses_quantity=df_inmuebles[df_inmuebles['distrito']==district].count()['distrito']
        df_distrito=df_inmuebles[df_inmuebles['distrito']==district]    # Dataframe of the houses in the given 'district'
        type_houses=df_distrito.groupby('plazas')['distrito'].count()   # Group by 'plazas' and them count them
        type_houses_percentage=round(type_houses*100/houses_quantity,2)
        outputx= type_houses_percentage.index.tolist()
        outputy = type_houses_percentage.values.tolist()

        plt.figure(figsize=(10, 6))
        plt.legend(district_list,loc='upper right')
        plt.bar(outputx,outputy, color='#0dbb75',edgecolor='#df7312')
        flag=True
        re_index=0
        for i,n in enumerate(outputy):
            if flag:
                if  (i+1) in outputx:
                    plt.text(i+1,n,n,ha='center',va='bottom') # Put the value number on the top of each bar
                else:
                    flag=False
                    re_index=i+2
                    plt.text(re_index,n,n,ha='center',va='bottom') # Put the value number on the top of each bar
                    re_index+=1
            else:
                while (re_index not in outputx):
                    re_index += 1
                plt.text(re_index,n,n,ha='center',va='bottom') # Put the value number on the top of each bar
                                
        plt.xlabel('Número de plazas')
        plt.ylabel('Porcentaje de tipo de inmueble')
        plt.title(f'Porcentaje de tipo de Casas por Distrito ({district})')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.get_backend() 
        plt.savefig(f'plot_percentage_of_house_types_{district}.png')
        plt.show()

plot_percentage_of_house_types(lista_distritos)


#####################################################################################################################################
# Crear una función que reciba una lista de distritos y una lista de tipos de alojamientos, y dibuje un 
# diagrama de sectores con la distribución del número de alojamientos de ese tipo por anfitrión en un distrito 
# de la lista.
#####################################################################################################################################
def pie_plot_house_types_per_district (district_list):
    for district in district_list:
        type_houses=df_inmuebles.groupby('plazas')['distrito'].count()   # Group by 'plazas' and them count them

        labels= type_houses.index.tolist()
        sizes = type_houses.values.tolist()

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Set to be a circular plot
        plt.title(f'Tipo de inmuebles por distrito ({district})')
        plt.get_backend() 
        plt.savefig(f'pie_plot_house_types_per_district_{district}.png')
        plt.show(block=True)

        # Group in '7 o más habitaciones' beyond 7 rooms
        otros = sum(sizes[6:])
        sizes = sizes[:6]
        sizes.append(otros)
        labels = labels[:6]
        labels.append('7 o más habitaciones')
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')  # Set to be a circular plot
        plt.title(f'Tipo de inmuebles por distrito ({district})')
        plt.get_backend() 
        plt.savefig(f'pie_plot_house_types_per_district_{district}_bundle_7_rooms.png')
        plt.show(block=True)

pie_plot_house_types_per_district(lista_distritos)


#####################################################################################################################################
# Crear una función que dibuje un diagrama de barras con los precios medios por persona y 
# día de cada distrito.
#####################################################################################################################################
def plot_price_per_vacancie_and_district(district_list):
    outputy=[]
    for district in district_list:
        total_vacancies=df_inmuebles[df_inmuebles['distrito']==district]['plazas'].astype(int).sum()
        total_price_per_day = df_inmuebles[df_inmuebles['distrito']==district]['precio'].astype(float).sum()
        mean_price_per_vacancy = round(total_price_per_day / total_vacancies,2)
        outputy.append(mean_price_per_vacancy)

    plt.figure(figsize=(10, 6))
    plt.legend(district_list,loc='upper right')
    plt.bar(district_list,outputy, color='#0dbb75',edgecolor='#df7312')
    for i,n in enumerate(outputy):
        plt.text(i,n,n,ha='center',va='bottom') # Put the value number on the top of each bar
    plt.xlabel('Distrito')
    plt.ylabel('Valor medio precio por cada plaza')
    plt.title(f'Precio medio de cada plaza por Distrito)')
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.get_backend() 
    plt.savefig(f'plot_price_per_vacancie_and_district.png')
    plt.show(block=True)

plot_price_per_vacancie_and_district(lista_distritos)


#####################################################################################################################################
# Crear una función que reciba una lista de distritos y dibuje un gráfico de dispersión por distritos con el 
# coste mínimo por noche / persona y la puntuación en esos distritos.
#####################################################################################################################################
df_file2= pd.read_csv('https://gitfront.io/r/davidlafuentem/ggoRNVtWaeuu/DataScience-SEPE/raw/madrid-airbnb-listings-apartado6.csv', sep=';', decimal=',',index_col='id')
df_file2['precio_persona']=df_file2['precio_persona'].astype(str).replace(',','.')  # Transform to be used as float
df_file2['precio_persona']=df_file2['precio_persona'].astype(float) # Transform into float
df_file2['puntuacion']=df_file2['puntuacion'].astype(int)   # Transform into int

df_inmuebles=df_file2

lista_distritos=['Centro','Fuencarral - El Pardo','Chamberi']

def plot_min_price_per_vacancie_and_district(district_list):
    outputx=[]
    outputy=[]
    for district in district_list:
        min_price_person_and_day=df_inmuebles[df_inmuebles['distrito']==district]['precio_persona'].min()
        rating_for_min_price_person_and_day=df_inmuebles[(df_inmuebles['distrito']==district) & (df_inmuebles['precio_persona']==min_price_person_and_day)]['puntuacion']
        outputy.append(min_price_person_and_day.round(2))
        outputx.append(rating_for_min_price_person_and_day.to_list()[0])

    plt.figure(figsize=(10, 6))
    plt.scatter(outputx,outputy, color='#0dbb75',edgecolor='#df7312')
    
    for i,n in enumerate(outputy):  #outputx and n are x and y coordinates, lista_distro are the labels to be showed
        plt.text(outputx[i],n-0.3,lista_distritos[i],ha='center',va='top',rotation=0) # Put the value number on the top of each point
    plt.xlabel('Establecimientos')
    plt.ylabel('Valor por dia y persona')
    plt.title(f'Precio Mínimo y puntuación por Distrito')
    plt.xticks(rotation=90, ha='right')
    plt.legend(district_list,loc='upper right')
    plt.tight_layout()
    plt.get_backend() 
    plt.savefig(f'plot_price_per_day.png')
    plt.show(block=True)

plot_min_price_per_vacancie_and_district(lista_distritos)


#####################################################################################################################################
# Crear una función que reciba una lista de distritos y dibuje un diagrama de barras con la distribución de 
# precios por persona y día.
#####################################################################################################################################
def plot_price_per_day_and_district(district_list):
    outputy=[]
    for district in district_list:
        price_person_and_day=df_inmuebles[df_inmuebles['distrito']==district]['precio_persona'].round(2)
        outputy=price_person_and_day.sort_values(ascending=False).tolist()
        outputx= np.arange(1, len(outputy)+1)

        plt.figure(figsize=(10, 6))
        plt.legend(district_list,loc='upper right')
        plt.bar(outputx,outputy, color='#0dbb75',edgecolor='#df7312')
        for i,n in enumerate(outputy):
            plt.text(i+1,n,n,ha='center',va='bottom',rotation=90) # Put the value number on the top of each bar
        plt.xlabel('Establecimientos')
        plt.ylabel('Valor precio por dia y persona')
        plt.title(f'Precio medio de cada plaza por Distrito ({district}))')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.get_backend() 
        plt.savefig(f'plot_price_per_day_{district}.png')
        plt.show(block=True)

plot_price_per_day_and_district(lista_distritos)

"""
