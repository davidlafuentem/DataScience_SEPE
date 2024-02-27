import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", db="")
cursor1=conexion1.cursor()      

cursor1.execute("drop database if exists ejercicio57;")
cursor1.execute("CREATE database ejercicio57 character set latin1 collate latin1_spanish_ci;")
cursor1.execute("USE ejercicio57;")

cursor1.execute("CREATE TABLE pasajeros (pasajero_id int PRIMARY KEY, \
				superviviente boolean, \
                clase int, \
                nombre varchar (50), \
				sexo varchar (10), \
				edad int, \
				sibsp int, \
				parch int, \
				ticket varchar(15), \
				fare float,\
				cabina varchar (10),\
				embarque varchar(1));")


cursor1.execute("LOAD DATA INFILE 'C:/proyectos/ejercicio57/titanic.csv' INTO TABLE pasajeros FIELDS TERMINATED BY  ';'  LINES TERMINATED BY '\n'; ")		


# Añadimos el campo de control para los menores de edad

cursor1.execute("alter table pasajeros add menor_edad boolean default 0;")


# Actualizamos el campo de los menores de edad

cursor1.execute("update pasajeros set menor_edad = 1 where edad >= 18;")


conexion1.commit()



#  Para ver en python el contenido de las tablas

cursor1.execute('SELECT * FROM pasajeros; ')   

longitud = 0
tabla = list()
for fila in cursor1:
    ancho = len(fila)
    tabla.append(fila)
    longitud += 1

for i in range(longitud):
    linea = ""
    for j in range(ancho):
        linea = linea + str(tabla[i][j]) + "\t"
    print(linea)


print("\nEn la tabla pasajeros tienes " + str(ancho)+ " campos y " + str(longitud) + " registros \n")
 

conexion1.close()


