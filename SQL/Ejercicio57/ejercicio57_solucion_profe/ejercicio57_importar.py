
           # Para indicar el lugar donde se encuentra el fichero

import os   # Libreria para trabajar con metodos del sistema operativo

from os import system
system("cls")

carpeta = "C:/proyectos/ejercicio57/"
fichero = "tabla_salida.csv"

ruta = os.path.join(carpeta, fichero)
ruta = os.path.abspath(ruta)

import numpy as np
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="ejercicio57")
cursor1=conexion1.cursor()


cursor1.execute("select * from pasajeros;")

longitud = 0
tabla = list()
for fila in cursor1:
    ancho = len(fila)
    tabla.append(fila)
    longitud += 1

conexion1.close()

            # Pasamos la tabla del Dataframe obtenido desde MySQL a NumPy

tabla_np = np.array(tabla)

elementos = tabla_np.size       # Numero de elementos del array (filas * columnas)

dimensiones = tabla_np.ndim     # Numero de dimensiones del array 

filas = tabla_np.shape[0]       # Numero de filas

columnas = tabla_np.shape[1]    # Numero de columnas

print("\nEn la tabla pasajeros tienes " + str(columnas)+ " campos y " + str(filas) + " registros \n")


    # ************************ PARTE 1. DATOS DE LAS FILAS *****************************


            # Creamos una tabla vacia de NumPy para ir metiendo los registros
            # La tabla sera de 2 diensiones y la rellenamos con los nombres de los campos
           


tabla_salida = np.array([["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked","Menor"]])


            # Extraemos los tipos de dato de la tabla_np y
            # los añadimos a la tabla de salida. Basta con hacerlo en una fila


copia = np.array([])            # Primero creamos un array vacio de dimension 1

for i in range(columnas):

    copia = np.append(copia, type(tabla_np[0][i]))  # Añadimos los tipos de datos a copia


copia = np.array([copia])       # Colocamos la misma dimension a copia que a tabla_salida

tabla_salida = np.concatenate((tabla_salida, copia))    # Unimos ambas tablas



            # Extraemos los n primeros pasajeros de la tabla_np y
            # los añadimos a la tabla de salida

n = 10

for i in range(n):
    copia = np.array([tabla_np[i]])
    tabla_salida = np.concatenate((tabla_salida, copia))



            # Extraemos el pasajero 148 de la tabla_np y
            # lo añadimos a la tabla de salida
    
pasajero = "148"

for i in range(filas):

     if (tabla_np[i][0]==pasajero):
        copia = np.array([tabla_np[i]])
        tabla_salida = np.concatenate((tabla_salida, copia))



            # Extraemos los n últimos pasajeros de la tabla_np y
            # los añadimos a la tabla de salida

for i in range(filas):

    if (i>=(filas-n)):
        copia = np.array([tabla_np[i]])
        tabla_salida = np.concatenate((tabla_salida, copia))




    # ************************ PARTE 2. DATOS DEL ANALISIS  *****************************


elementos = tabla_np.size       # Numero de elementos del array (filas * columnas)

dimensiones = tabla_np.ndim     # Numero de dimensiones del array 

todos = filas                   # Numero total de pasajeros 

print("\nNumero de elementos de la tabla: " + str(elementos))
print("Dimension de la tabla: " + str(dimensiones))
print("Numero de pasajeros contabilizados: " + str(todos))
      

    # Podemos crear una funcion a la que le pasamos la tabla y calcula
    # el porcentaje de supervivientes. Despues lo podemos restar de 100
    # y tenemos el porcentaje de victimas


def supervivientes(recibe_tabla):

    # inicializamos las variables de salvados

    salvados = 0                    
    
    for i in range(len(recibe_tabla)):
       if (recibe_tabla[i][1]=="1"):
            salvados+=1

    porcien_salvados = (salvados/len(recibe_tabla))*100
    porcien_salvados = round(porcien_salvados, 2)
    
    return porcien_salvados

supervi = supervivientes(tabla_np)
no_supervi = 100 - supervi

supervi = (str(supervi)+"%")
no_supervi = (str(no_supervi)+"%")

print("\nPorcentaje de supervivientes: " + supervi)
print("Porcentaje de no supervivientes: " + no_supervi)


                # Generamos una tabla nueva para cada clase
                # Usamos un encabezado vacío para unir las filas

primera = np.array([["","","","","","","","","","","","",""]])
segunda = primera
tercera = primera

for i in range(filas):
    copia = np.array([tabla_np[i]])

    match (tabla_np[i][2]):     # Tambien se puede hacer con IF

        case "1":
             primera = np.concatenate((primera, copia))
        case "2":
             segunda = np.concatenate((segunda, copia))
        case "3":
             tercera = np.concatenate((tercera, copia))
        case _: continue       # He dejado esta linea para activar el default del match


    # En principio las tablas deben llevar datos en cada registro, no filas vacías
    # Podemos eliminar tanto el encabezado vacío como otras filas vacías usando
    # WHILE y la función np.delete(tabla, fila/columna, axis=(0--> filas)(1-->columnas))
        
    # Podemos construir una funcion de borrado a la que le enviamos la tabla y 
    # la recibimos sin filas vacias.


def borrar_filas(tabla):

    inicio = 0
    numerofilas = len(tabla)

    while (inicio < numerofilas):

        if (tabla[inicio][0]==""):  # En este caso basta con controlar que la primera celda este vacia
            tabla = np.delete(tabla, inicio, axis=0)
            numerofilas-=1          # Hay que ir restando las filas borradas
                                    # Para evitar salirse del rango de la tabla
        inicio+=1

    return tabla

                # Obtenemos las tablas definitivas con las filas borradas

primera = borrar_filas(primera)     
segunda = borrar_filas(segunda)
tercera = borrar_filas(tercera)


            # Porcentaje de supervivientes de cada clase
            # Podemos usar la funcion superviviente(tabla) que ya tenemos


supervi_1 = supervivientes(primera)
supervi_1 = (str(supervi_1)+"%")
print("\nPorcentaje de supervivientes de 1ª Clase: " + supervi_1)

supervi_2 = supervivientes(segunda)
supervi_2 = (str(supervi_2)+"%")
print("Porcentaje de supervivientes de 2ª Clase: " + supervi_2)

supervi_3 = supervivientes(tercera)
supervi_3 = (str(supervi_3)+"%")
print("Porcentaje de supervivientes de 3ª Clase: " + supervi_3)


            # Edad media mujeres de cada clase
            # Podemos crear una funcion a la que le pasamos la tabla
            # y nos devuelve la media


def media_mujeres(recibe_tabla):

    # Inicializamos las variables de mujeres y suma de edad

    mujeres = 0                    
    edad = 0
    
    for i in range(len(recibe_tabla)):
       if (recibe_tabla[i][4]=="female"):
            mujeres+=1
            edad = edad + int(recibe_tabla[i][5])

    media = round(edad/mujeres, 2)
        
    return media

media_1 = media_mujeres(primera)
media_2 = media_mujeres(segunda)
media_3 = media_mujeres(tercera)


print("\nMedia de edad de las mujeres de 1ª Clase: " + str(media_1) + " años")
print("Media de edad de las mujeres de 2ª Clase: " + str(media_2) + " años")
print("Media de edad de las mujeres de 3ª Clase: " + str(media_3) + " años")



            # Porcentaje de mayores y menores que sobrevivieron por clase
            # Podemos crear una funcion a la que le pasamos la tabla y nos 
            # devuelve el valor de menores. Restandole 100 obtenemos el de mayores


def salvados_menores(recibe_tabla):

    # Inicializamos las variables de menores y salvados

    menores = 0                    
    salvados = 0
    
    for i in range(len(recibe_tabla)):
       
       if (recibe_tabla[i][1] == "1"):
           salvados += 1
           if (int(recibe_tabla[i][5]) < 18):
            menores+=1
            
    por_salv_menores = round((menores/salvados)*100, 2)
    
    return por_salv_menores


    # Calculamos el porcentaje de salvados menores y mayores por clase

salv_menores_1 = salvados_menores(primera)
salv_mayores_1 = 100 - salv_menores_1
salv_menores_1 = str(salv_menores_1)+"%"
salv_mayores_1 = str(salv_mayores_1)+"%"

print("\nPorcentaje de menores salvados de 1ª Clase: " + salv_menores_1)
print("Porcentaje de mayores salvados de 1ª Clase: " + salv_mayores_1)


salv_menores_2 = salvados_menores(segunda)
salv_mayores_2 = 100 - salv_menores_2
salv_menores_2 = str(salv_menores_2)+"%"
salv_mayores_2 = str(salv_mayores_2)+"%"

print("\nPorcentaje de menores salvados de 2ª Clase: " + salv_menores_2)
print("Porcentaje de mayores salvados de 2ª Clase: " + salv_mayores_2)


salv_menores_3 = salvados_menores(tercera)
salv_mayores_3 = 100 - salv_menores_3
salv_menores_3 = str(salv_menores_3)+"%"
salv_mayores_3 = str(salv_mayores_3)+"%"

print("\nPorcentaje de menores salvados de 2ª Clase: " + salv_menores_3)
print("Porcentaje de mayores salvados de 2ª Clase: " + salv_mayores_3)


    # Ahora generamos una tabla con los datos calculados en la 2ª Parte
    # Para unirla con los datos de la 1ª Parte. Deberá tener 13 columnas.


copia = np.array([["","","","","","","","","","","","",""],
                    ["Nº de elementos:",elementos,"","Dimension:", dimensiones,"","Nº de pasajeros:",todos,"","","","",""],
                    ["Porc. supervivientes:", supervi,"","Porc. victimas:",no_supervi,"","","","","","","",""],
                    ["Porc. sup. 1ª Clase:", supervi_1,"","Porc. sup. 2ª Clase:", supervi_2,"","Porc. sup. 3ª Clase:", supervi_3,"","","","",""],
                    ["Media edad mujeres 1ª Clase:",media_1,"años","","Media edad mujeres 2ª Clase:",media_2,"años","","Media edad mujeres 3ª Clase:",media_3,"años","","",],
                    ["Porc. menores salvados 1ª Clase: ",salv_menores_1,"","Porc. menores salvados 2ª Clase: ",salv_menores_2,"","Porc. menores salvados 3ª Clase: ",salv_menores_3,"","","","",""],
                    ["Porc. mayores salvados 1ª Clase: ",salv_mayores_1,"","Porc. mayores salvados 2ª Clase: ",salv_mayores_2,"","Porc. mayores salvados 3ª Clase: ",salv_mayores_3,"","","","",""]])


tabla_salida = np.concatenate((tabla_salida, copia))

      # Guardamos la tabla en un fichero de texto

np.savetxt(carpeta + fichero, tabla_salida, delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'])