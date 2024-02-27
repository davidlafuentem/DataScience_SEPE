# Ejercicio 64 - Segundo análisis de emisiones contaminantes
# I. Completar el ejercicio anterior escribiendo un programa en Python con los siguientes requisitos:

# Mostrar y guardar en un fichero .CSV un resumen descriptivo por año (mínimo, máximo, media, etc.) 
# para cada contaminante.
# Mostrar y guardar en un fichero .CSV un resumen descriptivo por año para cada distrito (estaciones).
# Crear una función que reciba el DataFrame, una estación y un contaminante y devuelva un resumen 
# descriptivo de las emisiones del contaminante indicado en la estación indicada.
# Crear una función que reciba el DataFrame, un contaminante y un año, y que devuelva las emisiones 
# medias mensuales para todas las estaciones.
# Crear un función que reciba el DataFrame y una estación de medición, y devuelva un DataFrame con las 
# medias mensuales de los distintos tipos de contaminantes.

# III. Imprimir por pantalla todos los resultados. Guardar el documento en tu carpeta como ejercicio_64.py


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
print("#################################################     Ejercicio64      ######################################################")


#####################################################################################################################################
# Generar un DataFrame con los datos de los cuatro ficheros.
#####################################################################################################################################
dataframes=list()

carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio64"
fichero='emisiones-2016.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2016 = pd.read_csv(ruta, sep=";", dtype="string")
dataframes.append(df_2016)

fichero='emisiones-2017.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2017 = pd.read_csv(ruta, sep=";", dtype="string")
dataframes.append(df_2017)

fichero='emisiones-2018.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2018 = pd.read_csv(ruta, sep=";", dtype="string")
dataframes.append(df_2018)

fichero='emisiones-2019.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df_2019 = pd.read_csv(ruta, sep=";", dtype="string")
dataframes.append(df_2019)

# All files have a problem, columns 'VXX' confirm if the column of the day corresponding to the same numeric identificator 'XX' 
# has a correct value by an 'V' or not with a 'N'.
# It's not possible to erase a row because in the same correct row, there are incorrect values from other day columns
# So it's necessary to create the dataframe, day by day, and then, erase the bad rows
row_validation = ['D01', 'V01', 'D02', 'V02', 'D03', 'V03', 'D04', 'V04', 'D05', 'V05', 'D06', 'V06', 'D07', 'V07', 'D08', 'V08', 'D09', 'V09', 'D10', 'V10', 'D11', 'V11', 'D12', 'V12', 'D13', 'V13', 'D14', 'V14', 'D15', 'V15', 'D16', 'V16', 'D17', 'V17', 'D18', 'V18', 'D19', 'V19', 'D20', 'V20', 'D21', 'V21', 'D22', 'V22', 'D23', 'V23', 'D24', 'V24', 'D25', 'V25', 'D26', 'V26', 'D27', 'V27', 'D28', 'V28', 'D29', 'V29', 'D30', 'V30', 'D31', 'V31']
base_columns=['ESTACION', 'MAGNITUD', 'ANO', 'MES']
df_final=list()

for dataframe in dataframes:    # Run thought the different dataframes
    columns_dataframe=dataframe.columns
    columns_to_keep=row_validation
    delete_columns=list()
    df=dataframe
    
    indice1=0
    indice2=1
    for i,value in enumerate(row_validation):   # Take 2 possitions, keeping columns corresponding to the same number 'DXX' and 'VXX'
        indice1=indice1+i
        indice2=indice2+i

        columns_to_study=base_columns
        columns_to_study.append(row_validation[indice1])    # Create columns for the study dataframe, 'DXX'
        columns_to_study.append(row_validation[indice2])    # Create columns for the study dataframe, 'VXX'

        for column in columns_dataframe:    # Create a list of the columns to be deleted, substracting the 'columns_to_study'
            if column not in columns_to_study:
                delete_columns.append(column)

        # After keep just the necessaries columns, correponding to the day values its validation column, incorrect rows can be deleted
        #df = df.drop(df.columns(delete_columns), axis='columns')  # Only have rows for each day and its validation column
        df = df.drop(delete_columns, axis='columns')

        df = df[df[].eq('V').all(axis=1)] # Erase rows with bad values, 'N' in its corresponding 'V' column

        df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
        df_final.concat(df_final,df)    # Concatenate each dataframe created for each day

print(df_final)


# After eliminate rows with 'N' values, confirmation columns are no longer needed
indices_a_eliminar = [0, 1, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
df_2016 = df_2016.drop(df_2016.columns[indices_a_eliminar], axis='columns')
df_2017 = df_2017.drop(df_2017.columns[indices_a_eliminar], axis='columns')
df_2018 = df_2018.drop(df_2018.columns[indices_a_eliminar], axis='columns')
df_2019 = df_2019.drop(df_2019.columns[indices_a_eliminar], axis='columns')




df=pd.concat([df_2016,df_2017,df_2018,df_2019]) # Concatenate all clean dataframes in just one
print(df)




""" 
# Deled rows with invalid values, checking validation columns in 'row_validation'
# Select only rows where there is a 'V' tellings that its the god one value
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


df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
print(df) """

#df['FECHA'] = date(int(df.loc[0,'ANO']), int(df.loc[0,'MES']), int(df.loc[0,'DIA'][1:]))

# for i in range(len(df)):  ## FUNCIONA PERO ES MUY INEFICIENTE EN CÁLCULO!!! ####
#     df.loc[i,'FECHA']=date(int(df.loc[i,'ANO']), int(df.loc[i,'MES']), int(df.loc[i,'DIA'][1:]))

""" 
df['DIA'] = df['DIA'].astype(str).str[1:]  # Elimnate the first character 'D' to use as a number
#df['DIA'] = df['DIA'].str.replace('D', '')  # Elimnate the first character 'D' to use as a number
fechas_str = (df['ANO'].astype(str) + '-' + df['MES'].astype(str) + '-' + df['DIA'].astype(str))

df['FECHA'] = pd.to_datetime(fechas_str, format="%Y-%m-%d", errors='coerce')

# Crear la nueva columna 'FECHA' usando las columnas 'ANO', 'MES' y 'DIA' convertidas a enteros
#df['FECHA'] = df.apply(lambda row: date(int(row['ANO']), int(row['MES']), row['DIA']), axis=1)

print(df.head())

#####################################################################################################################################
# Mostrar y guardar en un fichero .CSV un resumen descriptivo por año (mínimo, máximo, media, etc.) 
# para cada contaminante.
#####################################################################################################################################
abailable_stations=df['ESTACION'].unique().tolist()
pollutants=df['MAGNITUD'].unique().tolist()

years=['2016','2017','2018','2019']

for year in years:
    df_describe=df
    df_describe=df_describe.set_index(['ESTACION'])
    df_describe=df_describe[df_describe['ANO']==year]
    df_describe=df_describe.drop(columns=['MES','DIA','FECHA'])

    if df_describe['VALOR'].dtypes == 'string':
        df_describe['VALOR']=df_describe['VALOR'].astype(float)

    df_describe = df_describe.groupby(['MAGNITUD'])
    df_describe=df_describe.describe().round(2)

    print(df_describe,"\n")

    df_min_max_mean = df_describe['VALOR'][['min', 'max', 'mean']]
    print(df_min_max_mean)
    df_min_max_mean.to_csv(f'{year}_min_max_mean.csv',sep=';',decimal=',')



#####################################################################################################################################
# Mostrar y guardar en un fichero .CSV un resumen descriptivo por año para cada distrito (estaciones).
#####################################################################################################################################
for year in years:
    df_describe=df
    df_describe=df_describe.set_index(['ESTACION'])
    df_describe=df_describe[df_describe['ANO']==year]
    df_describe=df_describe.drop(columns=['MES','DIA','FECHA'])

    if df_describe['VALOR'].dtypes == 'string':
        df_describe['VALOR']=df_describe['VALOR'].astype(float)

    df_describe = df_describe.groupby(['ESTACION'])
    df_describe=df_describe.describe().round(2)

    print(df_describe,"\n")

    df_describe.to_csv(f'{year}_describe.csv',sep=';',decimal=',')



#####################################################################################################################################
# Crear una función que reciba el DataFrame, una estación y un contaminante y devuelva un resumen 
# descriptivo de las emisiones del contaminante indicado en la estación indicada.
#####################################################################################################################################
print("Escoja una estación y un contaminante para lanzar consultar")

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
        df_filtrado = df[((df['ESTACION'] == station) & (df['MAGNITUD'] == contaminant) )]
        if df_filtrado.empty:
            print(f"La solicitud de ESTACIÓN ({station}) y MAGNITUD ({contaminant}) no existe en este dataFrame.\
                  \nEscoge de nuevo el contaminante.")
            flag=True
        else:
            flag=False
    else:
        print("El contaminante escogido no es correcto.  Vuelva a intentarlo")
        flag=True
    
df_describe=df[(df['ESTACION']==station)&(df['MAGNITUD']==contaminant)].drop(columns=['MES','DIA','FECHA'])
print(df_describe)

df_describe['VALOR']=df_describe['VALOR'].astype(float)
print(f"Los datos descriptivos para la ESTACIÓN ({station}) y la MAGNITUD ({contaminant}) en los años ({years}) es: ")
print(df_describe['VALOR'].describe().round(2))



#####################################################################################################################################
# Crear una función que reciba el DataFrame, un contaminante y un año, y que devuelva las emisiones 
# medias mensuales para todas las estaciones.
#####################################################################################################################################
print("\nEscoja un contaminante y un año para lanzar consultar")

flag=True
while flag:
    flag=False

    print(f"Posibles contaminantes: {pollutants}")
    contaminant=input("Escoja contaminante \n")
    contaminant=contaminant.lower().strip()
    if (contaminant in pollutants):
        print(f"   El contaminante escogido es: {contaminant}")
        flag=False
    else:
        print("   El contaminante escogido no es correcto.  Vuelva a intentarlo")
        flag=True

flag=True
while flag:
    flag=False

    print(f"\nPosibles años: {years}")
    year=input("   Escoja año \n")
    year=year.lower().strip()
    if (year in years):
        print(f"   El año escogido es: {year}")

        df_filtrado = df[((df['MAGNITUD'] == contaminant) & (df['ANO'] == year))]
        if df_filtrado.empty:
            print(f"La solicitud de MAGNITUD ({contaminant}) y de ANO ({year}) no existe en este dataFrame.\
                    \nEscoge de nuevo el año.")
            flag=True
        else:
            flag=False
    else:
        print("El año escogido no es correcto.  Vuelva a intentarlo")
        flag=True

df_filtrado=df_filtrado.drop(columns=['DIA','FECHA'])
df_filtrado['VALOR']=df_filtrado['VALOR'].astype(float)
df_filtrado=df_filtrado.groupby(['MAGNITUD','ESTACION','MES'])
print(df_filtrado['VALOR'].mean().round().head(46))


#####################################################################################################################################
# Crear un función que reciba el DataFrame y una estación de medición, y devuelva un DataFrame con las 
# medias mensuales de los distintos tipos de contaminantes.
#####################################################################################################################################print("Escoja una estación y un contaminante para lanzar consultar")
print("\nEscoja una estación de medición para recibir las medias mensules de los distintos contaminantes")

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

df_filtrado = df[(df['ESTACION'] == station)]
df_filtrado=df_filtrado.drop(columns=['DIA','FECHA'])
df_filtrado['VALOR']=df_filtrado['VALOR'].astype(float)
df_filtrado=df_filtrado.groupby(['ESTACION','MAGNITUD','MES'])

print(df_filtrado['VALOR'].mean().round())
 """