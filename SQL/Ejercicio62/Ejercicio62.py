# Ejercicio 62 - Dataframes de Pandas desde GitHub
# I. El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 
# con las siguientes columnas:

# Nombre (nombre de la empresa)
# Final (precio de la acción al cierre de bolsa)
# Maximo (precio máximo de la acción durante la jornada)
# Minimo (precio mínimo de la acción durante la jornada)
# Volumen (Volumen al cierre de bolsa)
# Efectivo (capitalización al cierre en miles de euros).

# II. Crear una función que construya un DataFrame a partir del fichero .CSV con el 
# formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de 
# dada columna. El fichero se descargará directamente al programa de Python desde un 
# repositorio de GitHub usando el siguiente link:

# https://gitfront.io/r/InboxColon/soJ3JjHrPQKF/pythonfiles/raw/cotizacion.csv

# III. Imprimir por pantalla todos los resultados. Guardar el documento en tu carpeta 
# como ejercicio_62.py

import pandas as pd
import funciones_externas
from funciones_externas import *
import ssl
from urllib.request import urlopen

#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio62      ######################################################")

#####################################################################################################################################
# II. Crear una función que construya un DataFrame a partir del fichero .CSV con el 
# formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de 
# cada columna. El fichero se descargará directamente al programa de Python desde un 
# repositorio de GitHub usando el siguiente link:
# https://gitfront.io/r/InboxColon/soJ3JjHrPQKF/pythonfiles/raw/cotizacion.csv
#####################################################################################################################################
import ssl
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context #Set off SSL certify certification

df_fichero= pd.read_csv('https://gitfront.io/r/InboxColon/soJ3JjHrPQKF/pythonfiles/raw/cotizacion.csv', sep=';', decimal=',')

result=dayly_key_indicators(df_fichero)

print(result)