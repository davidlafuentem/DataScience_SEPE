## Ejercicio 07 - Cálculo de precios con descuento
## Escribe un programa que pregunte el precio, el tanto por ciento de descuento, y te diga el precio con descuento. 
## Por ejemplo, si el precio que introduce el usuario es 300 y el descuento 20, el programa dirá que el precio final 
## con descuento es de 240 redondeando a dos decimales.

print("Introduzca el precio, el descuento para calcular el precio neto")

precio = int(input("Precio: "))
descuento = int(input("Descuento: "))

print("El precio neto es: ", precio - (precio*descuento/100))