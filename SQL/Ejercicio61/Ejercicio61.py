# Ejercicio 61 - Dataframes de diccionarios en Pandas
# I. Escribir un programa que genere y muestre por pantalla un DataFrame de Pandas con los datos 
# de la tabla siguiente:

# II. Crear una serie de Pandas formada por cuatro meses. Los meses se le preguntarán al usuario: 
# "¿Qué meses quieres consultar?" No se podrá repetir el mes, si se repite el mes se seguirá pidiendo 
# otro mes hasta completar los cuatro. Controlar que los meses guardados en la serie tienen el mismo 
# formato que el indice del Dataframe

# III. Crear una función que reciba el DataFrame y la serie anterior y devuelva en otra serie de Pandas
# el balance (ventas - gastos) total en los meses indicados indexado por mes y ordenado por balance.

# IV. Imprimir por pantalla todos los resultados. Guardar el documento en tu carpeta como ejercicio_61.py

import pandas as pd
import funciones_externas
from funciones_externas import *


#####################################################################################################################################
########################################################        MAIN         ########################################################
#####################################################################################################################################

print("#################################################     Ejercicio61      ######################################################")

df = pd.DataFrame([['Enero', 30500,22000], ['Febrero',35600,23400], ['Marzo',28300,18100],['Abril',33900,20700], ['Mayo',36126,28923],['Junio',39861,28789], ['Julio',27603,29667], ['Agosto',32571,29216],['Septiembre',30535,22551], ['Octubre',33587,26346], ['Noviembre',28956,23033],['Diciembre',29495,22375]],columns=['Mes','Ventas', 'Gastos'])
print(df,"\n")

df = df.set_index('Mes')
print(df,"\n")

 #####################################################################################################################################   
# II. Crear una serie de Pandas formada por cuatro meses. Los meses se le preguntarán al usuario: 
# "¿Qué meses quieres consultar?" No se podrá repetir el mes, si se repite el mes se seguirá pidiendo 
# otro mes hasta completar los cuatro. Controlar que los meses guardados en la serie tienen el mismo 
# formato que el indice del Dataframe
#####################################################################################################################################
meses_posibles = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                           index=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                           dtype='int')
flag=True
meses_consulta=[]

print("Escoja 4 meses para consultar")
while flag:
    flag=False

    if len(meses_consulta) < 4:
        mes=input("¿Qué meses quiere añadir a la consulta? \n")
        mes=mes.lower().capitalize()
        if (mes in meses_posibles.index):
            if (mes not in meses_consulta):
                meses_consulta.append(mes)
                print(f"Meses escogidos: {meses_consulta}")
                flag=True
            else:
                print("El mes ya ha sido seleccionado.  Vuelva a intentarlo")
                flag=True    
        else:
            print("El mes no es correcto")
            flag=True
df_seleccionado = df.loc[meses_consulta]

print(df_seleccionado,"\n")


# III. Crear una función que reciba el DataFrame y la serie anterior y devuelva en otra serie de Pandas
# el balance (ventas - gastos) total en los meses indicados indexado por mes y ordenado por balance.
print(balance(df_seleccionado))










