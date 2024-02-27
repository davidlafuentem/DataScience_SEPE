###  Ejercicio 02 - Cálculo de área, perímetro  rectángulo  ###

import math

while True:
    lado1 = input("\nIntroduzca el primer lado del rectángulo: ")
    if lado1.isdigit():
        lado1 = int(lado1)
        break

while True:
    lado2 = input("Introduzca el segundo lado del rectángulo: ")
    if lado2.isdigit():
        lado2 = int(lado2)
        break

area = lado1 * lado2
perimetro = 2 * (lado1 + lado2)

print("   El área es: ",int(area))
print("   El perímetro es: ",int(perimetro))