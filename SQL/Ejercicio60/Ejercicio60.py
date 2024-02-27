# Ejercicio 60 - Series de diccionarios en Pandas
# I. Escribir una función que reciba un diccionario Pandas (alumnos.py) con las notas de los alumnos de un curso y devuelva una nueva serie/lista de Pandas con la nota mínima, la máxima, media y la desviación típica.

# II. Escribir otra función que reciba el mismo diccionario con las notas de los alumnos y devuelva otro diccionario con las notas de los alumnos aprobados ordenadas de mayor a menor y por orden alfabético ascendente.

# III. Imprimir por pantalla ambos resultados. Guardar el documento en tu carpeta como ejercicio_60.py

import pandas as pd
import alumnos 
import funciones_externas
from funciones_externas import *


#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################

print("#################################################     Ejercicio60      ######################################################")

#####################################################################################################################################
# I. Escribir una función que reciba un diccionario Pandas (alumnos.py) con las notas de los alumnos de un curso 
# y devuelva una nueva serie/lista de Pandas con la nota mínima, la máxima, media y la desviación típica.
#####################################################################################################################################
pd_describe=min_max_mean_std_from_pd_series(alumnos.alumnos)

print(f"{pd_describe} ['min','max,'mean','std']")


#####################################################################################################################################
# II. Escribir otra función que reciba el mismo diccionario con las notas de los alumnos y devuelva otro 
# diccionario con las notas de los alumnos aprobados ordenadas de mayor a menor y por orden alfabético ascendente.
#####################################################################################################################################
pd_tidy=sort_series(alumnos.alumnos)

print(pd_tidy[0],"\n")
print(pd_tidy[1])

    








