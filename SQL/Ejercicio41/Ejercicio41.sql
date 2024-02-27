/*DROP DATABASE inmuebles;*/
CREATE DATABASE inmuebles character set latin1 collate latin1_spanish_ci;
USE inmuebles;


CREATE TABLE tipo_inmueble(codigo_tipo varchar(3) NOT NULL PRIMARY KEY, descrip_tipo varchar(30));

CREATE TABLE regimen_inmueble(codigo_reg varchar(3) NOT NULL PRIMARY KEY, descrip_reg varchar(30));

CREATE TABLE propietarios(nif_propiet varchar(9) NOT NULL PRIMARY KEY, nombre_propiet varchar(40), direcc_propiet varchar(40));

CREATE TABLE inmuebles(cod_inm varchar(6), tipo_inm varchar(3), localiz_inm varchar(40), localidad_inmueble varchar(30), super_inm int , reg_inm varchar(3), precio_inm int , propiet_inm varchar(9), disponib_inm varchar(10),
    FOREIGN KEY (propiet_inm) REFERENCES propietarios(nif_propiet),
    FOREIGN KEY (tipo_inm) REFERENCES tipo_inmueble(codigo_tipo),
    FOREIGN KEY (reg_inm) REFERENCES regimen_inmueble(codigo_reg));


insert into tipo_inmueble values    ('SUB','Solar Urbano'),
							        ('SIN','Solar Industrial'),
							        ('VUB','Vivienda Urbana'),
    							    ('VRU','Vivienda Rural'),
	    						    ('OUB','Oficina Urbana'),
		    					    ('OIN','Oficina Industrial'),
                                    ('NIN','Nave Industrial');

insert into regimen_inmueble values ('ALQ','Alquiler'),
							        ('VEN','Venta'),
							        ('ALV','Alquiler opción venta');

insert into propietarios values ('12345678A', 'FELIPE GARCIA', 'PONTONES, 56'),
						    	('23456789B', 'GESURB. S.A.','MERCURIO, 12'),
							    ('34567890C', 'ALFONSO PEREZ GESTIONES','MARACAIBO, 20');

insert into inmuebles values    ('MA-001', 'SIN', 'PASTOR, 4','LEGANES',2500,'VEN',390000,'23456789B',NULL),
                                ('MA-002', 'VUB', 'LENNIN, 41','ALGETE',120,'ALQ',650,'12345678A','01/11/2009'),
                                ('T0-001', 'VUB', 'MAYOR, 23','TOLEDO',95,'VEN',220000,'23456789B','01/06/2012'),
                                ('T0-002', 'VUB', 'ARROYO, 3','TOLEDO',65,'ALQ',350,'23456789B','01/07/2011'),
                                ('MA-003', 'NIN', 'PLATO, 2','ALCORCON',750,'ALQ',4500,'34567890C',NULL),
                                ('MA-004', 'OUB', 'ARENAL, 4','MADRID',80,'VEN',650000,'34567890C','01/01/2012'),
                                ('MA-005', 'OUB', 'ASCAO,56','MADRID',150,'ALQ',1500,'23456789B','01/03/2012');


select * FROM inmuebles;

