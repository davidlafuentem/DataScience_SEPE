/*
Ejercicio 40 - Importar ficheros de datos en SQL
I. Se entrega un fichero de datos llamado "alumnos.txt". Crear el código en SQL necesario para importar el fichero a una tabla en SQL, usando como clave primaria el DNI. 
II. Realizar las siguientes  consultas:
Listado de los alumnos de Madrid, Guadalajara y Soria, mostrando solamente Nombre, Dirección, Población y Teléfono ordenados por Nombre.
Listado de los alumnos mayores de 18 años y menores de 65 años (inclusive), mostrando solamente Nombre, Población, Edad y Teléfono ordenados por Edad.
*/
DROP DATABASE alumnos;
CREATE DATABASE alumnos CHARACTER SET latin1 COLLATE latin1_spanish_ci;
USE alumnos;

CREATE TABLE datos (dni varchar(9) NOT NULL PRIMARY KEY, nombre varchar(30), edad int, direccion varchar(30), provincia varchar (30), telf varchar (9),fecha_ini varchar(10), fecha_fin varchar(10));

LOAD DATA INFILE "C:/Proyectos_David/ficheros/alumnos.txt" INTO TABLE datos FIELDS TERMINATED BY "\t" LINES TERMINATED BY "\n";

/*Listado de los alumnos de Madrid, Guadalajara y Soria, mostrando solamente Nombre, Dirección, Población y Teléfono ordenados por Nombre.*/ 
SELECT nombre, direccion, provincia, telf FROM datos WHERE (provincia = "Madrid" OR provincia = "Guadalajara" OR provincia = "Soria") ORDER BY nombre ASC;*/

/*Listado de los alumnos mayores de 18 años y menores de 65 años (inclusive), mostrando solamente Nombre, Población, Edad y Teléfono ordenados por Edad. */
SELECT nombre, provincia, edad, telf FROM datos WHERE (edad >= 18 AND edad <= 65) ORDER BY edad ASC;