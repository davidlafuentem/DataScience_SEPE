/*  Ejercicio 42 - Creación de consultas de selección por parámetros (practica de evaluación)
I. Abrir la base de datos del Ejercicio 41 y crear las siguientes consultas de selección:

INMUEBLES ORDENADOS TIPO: Muestra los campos TIPO INM, LOCALIZAC INM, LOCALIDAD INM, REGIMEN INM y PRECIO INM. Ordenar la consulta por TIPO INM.
INMUEBLES EN ALQUILER DISPONIBLES: Muestra los campos TIPO INM, LOCALIZAC INM, LOCALIDAD INM, SUPERFICIE INM, y PRECIO INM. Deben aparecer los registros con el campo REGIMEN INM = “ALQ”. Deben aparecer los registros con la disponibilidad menor que el día de hoy.
Copiar la consulta INMUEBLES EN ALQUILER DISPONIBLES dos veces para crear INMUEBLES EN VENTA DISPONIBLES y INMUEBLES EN ALV DISPONIBLES. Modificar lo necesario en cada copia.

II. Crear las siguientes consultas:

INMUEBLES POR SUPERFICIE: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los registros que tengan una superficie entre un mínimo y un máximo que nos solicite.

INMUEBLES POR PROPIETARIO: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los inmuebles del nif de propietario que nos solicite.

INMUEBLES EN VENTA POR PRECIO: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los registros de inmuebles en venta, ordenados por superficie.

ALTA DE INMUEBLES: Debe mostrar todos los campos de la tabla INMUEBLES y los campos NOMBRE PROPIET y DIRECC PROPIET de la tabla PROPIETARIOS.

INMUEBLES POR CRITERIOS: Debe mostrar los campos que considere de la tabla INMUEBLES. La consulta debe solicitar el tipo de inmueble, el régimen de inmueble y la localidad del inmueble, solo aparecerán los disponibles.

III. Guardar el documento .SQL en tu carpeta como Ejercicio 42." */


/* INMUEBLES ORDENADOS TIPO: Muestra los campos TIPO INM, LOCALIZAC INM, LOCALIDAD INM, REGIMEN INM y PRECIO INM. Ordenar la consulta por TIPO INM.*/
SELECT tipo_inm, localiz_inm, localidad_inmueble, reg_inm, precio_inm FROM inmuebles ORDER BY tipo_inm ASC;

/*NMUEBLES EN ALQUILER DISPONIBLES: Muestra los campos TIPO INM, LOCALIZAC INM, LOCALIDAD INM, SUPERFICIE INM, y PRECIO INM. Deben aparecer los registros con el campo REGIMEN INM = “ALQ”. Deben aparecer los registros con la disponibilidad menor que el día de hoy.*/
SELECT tipo_inm, localiz_inm, localidad_inmueble, super_inm, precio_inm FROM inmuebles WHERE reg_inm = "ALQ" and disponib_inm < "2023/12/12";

/*Copiar la consulta INMUEBLES EN ALQUILER DISPONIBLES dos veces para crear INMUEBLES EN VENTA DISPONIBLES y INMUEBLES EN ALV DISPONIBLES. Modificar lo necesario en cada copia. */
SELECT tipo_inm, localiz_inm, localidad_inmueble, super_inm, precio_inm FROM inmuebles WHERE reg_inm = "ALV" and  disponib_inm < "2023/12/12";

/* INMUEBLES POR SUPERFICIE: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los registros que tengan una superficie entre un mínimo y un máximo que nos solicite. */
SELECT * FROM inmuebles WHERE  super_inm > 10 AND super_inm < 100 ORDER BY super_inm ASC;

/* INMUEBLES POR PROPIETARIO: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los inmuebles del nif de propietario que nos solicite. */
SELECT * FROM inmuebles WHERE  propiet_inm = "23456789B";

/* INMUEBLES EN VENTA POR PRECIO: Debe mostrar los campos que considere de la tabla INMUEBLES y deben aparecer los registros de inmuebles en venta, ordenados por superficie. */
SELECT * FROM inmuebles WHERE  reg_inm = "VEN"  ORDER BY super_inm ASC;

/* ALTA DE INMUEBLES: Debe mostrar todos los campos de la tabla INMUEBLES y los campos NOMBRE PROPIET y DIRECC PROPIET de la tabla PROPIETARIOS. */
SELECT inmuebles.*, propietarios.nombre_propiet, propietarios.direcc_propiet FROM inmuebles, propietarios;

/* INMUEBLES POR CRITERIOS: Debe mostrar los campos que considere de la tabla INMUEBLES. La consulta debe solicitar el tipo de inmueble, el régimen de inmueble y la localidad del inmueble, solo aparecerán los disponibles. */
SELECT * FROM inmuebles WHERE tipo_inm = "OUB" AND reg_inm = "VEN" AND localidad_inmueble = "MADRID" AND (disponib_inm <> "" OR disponib_inm <> NULL);
