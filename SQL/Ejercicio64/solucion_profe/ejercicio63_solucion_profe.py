
           # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = "C:/proyectos/ejercicio63/"
fichero = ""

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import pandas as pd
from datetime import datetime


# Funcion del apartado 7
        
def apartado7(df, estacion, contaminante, fecha_inicio, fecha_fin):
    filtrado = df[(df['ESTACION'] == estacion) & (df['MAGNITUD'] == contaminante) & (df['FECHA'] >= fecha_inicio) & (df['FECHA'] <= fecha_fin)]
    return filtrado[['FECHA', 'VALOR']]



#********************************** APARTADO 1 **********************************


# Apartado 1: Generar un DataFrame con los datos de los cuatro ficheros.
# Leemos cada archivo CSV y lo guardamos en una tabla independiente

tabla_2016 = pd.read_csv(carpeta + "emisiones-2016.csv", sep=';', decimal=',')
tabla_2017 = pd.read_csv(carpeta + "emisiones-2017.csv", sep=';', decimal=',')
tabla_2018 = pd.read_csv(carpeta + "emisiones-2018.csv", sep=';', decimal=',')
tabla_2019 = pd.read_csv(carpeta + "emisiones-2019.csv", sep=';', decimal=',')

# Unimos los DataFrames y los pasamos a fichero para verificar que esta todo correcto 

tabla_total = pd.concat([tabla_2016, tabla_2017, tabla_2018, tabla_2019], ignore_index=True)
tabla_total.to_csv(carpeta + "resultados/tabla_totales.csv", index=False, sep=';', decimal=',')



#********************************** APARTADO 2 **********************************


# Apartado 2: Generar un nuevo DataFrame con las columnas ESTACION, MAGNITUD, AÑO, MES y los días (D01..D31)
# Filtramos las columnas del DataFrame y nos quedamos con las columnas ESTACION, MAGNITUD, AÑO, MES y los días D01..D31
# Seleccion inicial

columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']   

# Ampliamos la seleccion a las columnas restantes que empiezan con D

columnas.extend([col for col in tabla_total if col.startswith('D')])   

tabla_total = tabla_total[columnas]

# La guardamos en otro fichero para verificar que esta todo correcto 

tabla_total.to_csv(carpeta + "resultados/tabla_total_filtrada.csv", index=False, sep=';', decimal=',')




#********************************** APARTADO 3 **********************************


# Apartado 3: Reestructurar el DataFrame para que los valores de los contaminantes 
#               de las columnas de los días aparezcan en una única columna.

tabla_nueva = tabla_total.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')

# Convertimos la columna 'VALOR' a tipo float, para posteriormente hacer cálculos

tabla_nueva['VALOR'] = tabla_nueva['VALOR'].astype(float)

# La guardamos en otro fichero para verificar que esta todo correcto 

tabla_nueva.to_csv(carpeta + "resultados/tabla_nueva.csv", index=False, sep=';', decimal=',')




#********************************** APARTADO 4 **********************************

# Añadir una columna con la fecha a partir de la concatenación del año, 
#           el mes y el día (usar el módulo DATETIME).


# Concatenamos las columnas del año, mes y día Y BORRAMOS LA D DEL DIA

tabla_nueva['FECHA'] = tabla_nueva.DIA.apply(str) + "/" + tabla_nueva.MES.apply(str) + "/" + tabla_nueva.ANO.apply(str) 
tabla_nueva['FECHA'] = tabla_nueva.FECHA.str.strip('D')

# Convertimos la nueva columna al tipo fecha

tabla_nueva['FECHA'] = pd.to_datetime(tabla_nueva.FECHA, format="%d/%m/%Y", errors="coerce")

# La guardamos en otro fichero para verificar que esta todo correcto 

tabla_nueva.to_csv(carpeta + "resultados/tabla_nueva_fecha.csv", index=False, sep=';', decimal=',')




#********************************** APARTADO 5 **********************************

# Eliminar las filas con fechas no válidas (utilizar la función dropna) 
#       y ordenar el DataFrame por fecha.

tabla_nueva = tabla_nueva.dropna(subset='FECHA')

# Ordenar el el dataframe por fecha

tabla_nueva = tabla_nueva.sort_values(['FECHA'])

# La guardamos en otro fichero para verificar que esta todo correcto 

tabla_nueva.to_csv(carpeta + "resultados/tabla_nueva_fecha.csv", index=False, sep=';', decimal=',')




#********************************** APARTADO 6 **********************************

# Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
# Es conveniente generar una serie de las estaciones y otra de los contaminantes para
#       para verificar después que la estacion o contaminante solicitado es correcto

estaciones = tabla_nueva.ESTACION.unique()
contaminantes = tabla_nueva.MAGNITUD.unique()
print("\nListado de estaciones: ")
print(estaciones)
print("\nListado de contaminantes: ")
print(contaminantes)




#********************************** APARTADO 7 **********************************

# Crear una función que reciba el DataFrame, una estación, un contaminante y 
#       un rango de fechas y devuelva una serie con las emisiones del contaminante 
#       dado en la estación y rango de fechas dado.


estacion = 48
contaminante = 12
fecha_inicio = datetime(2016, 12, 22)
fecha_fin = datetime(2017, 1, 25)
resultado = apartado7(tabla_nueva, estacion, contaminante, fecha_inicio, fecha_fin)
print("\nEmisiones del contaminante " + str(contaminante) + " en la estación " + str(estacion))
print("\nFechas del informe: dese el " + str(fecha_inicio) + " hasta " + str(fecha_fin) + "\n")
print(resultado)

resultado.to_csv(carpeta + "resultados/resultado.csv", index=False, sep=';', decimal=',')



