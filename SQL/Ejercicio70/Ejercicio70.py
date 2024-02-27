# Ejercicio 70 - Creación de diagramas básicos
# I. Completar el análisis del ejercicio 66 con sus diagramas correspondientes.


# Dibujar el diagrama de barras verticales del porcentaje de modelos de cada marca. 
# Usar color #0dbb75 para el fondo de las barras y #df7312 para los bordes. Añadir un título al gráfico 
# y a los ejes X e Y (páginas 27 y 28 del manual).
# Dibujar el diagrama de dispersión de la potencia y el precio. Usar color #5112df para los puntos y 
# como marcador un triángulo (pagina 25 del manual). Añadir un título al gráfico y a los ejes X e Y 
# (páginas 27 y 28 del manual).

# Los gráficos deben mostrarse en pantalla y guardarse automáticamente en una carpeta con los nombres diagrama66_linea.png 
# y diagrama66_dispersion.png.

# II. Crear un fichero de salida .ZIP con las imágenes de los diagramas y el programa. Guardar el documento en tu carpeta 
# como ejercicio_70.py


import os
import ssl
import pandas as pd
from os import system
import funciones_externas
from funciones_externas import *
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('qtagg')
from urllib.request import urlopen
from datetime import date                           # Para trabajar con fechas
from datetime import datetime                       # Para trabajar con horas
from datetime import timedelta                      # Para operar con dias
from dateutil.relativedelta import relativedelta    # Para trabajar con fechas

#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################
system("clear")   #Clear shell
print("#################################################     Ejercicio70      ######################################################")


#####################################################################################################################################
# Dibujar el diagrama de barras verticales del porcentaje de modelos de cada marca. 
# Usar color #0dbb75 para el fondo de las barras y #df7312 para los bordes. 
# Añadir un título al gráfico y a los ejes X e Y.
#####################################################################################################################################
carpeta=r"/Users/dlf/Documents/Curso_Data_Science_2023/Ejercicios/SQL/Ejercicio66"
fichero='coches.csv'
ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)
df = pd.read_csv(ruta, sep=";", dtype="string")

df_coches = df.dropna(how='any')    # Clean bad registers

count_models = df_coches.groupby('Marca')['Modelo'].nunique().sort_values(ascending=False)
print(count_models)

brands = count_models.index.tolist()
values = count_models.values.tolist()


# for marca, valor in count_models.items():
#     print(f"Marca: {marca}, Cantidad de Modelos: {valor}")


plt.figure(figsize=(10, 6))
plt.bar(brands, values, color='#0dbb75',edgecolor='#df7312')
plt.xlabel('Marca')
plt.ylabel('Cantidad de Modelos')
plt.title('Cantidad de Modelos por Marca')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.get_backend() 
plt.savefig('diagrama_barras.png')
plt.show()



#####################################################################################################################################
# Dibujar el diagrama de dispersión de la potencia y el precio. Usar color #5112df para los puntos y 
# como marcador un triángulo (pagina 25 del manual). Añadir un título al gráfico y a los ejes X e Y 
# (páginas 27 y 28 del manual).
#####################################################################################################################################
df_coches['Precio']=df_coches['Precio'].astype(float)
power_price = df_coches.groupby('Potencia')['Precio'].mean().round(2).sort_values(ascending=False)
print(power_price)

power = power_price.index.tolist()
price = power_price.values.tolist()


plt.figure(figsize=(10, 6))
plt.scatter(power, price, color='#5112df', marker = '^')
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.title('Dispersión Potencia vs Precio')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.savefig('diagrama_dispersion.png')
plt.show()
