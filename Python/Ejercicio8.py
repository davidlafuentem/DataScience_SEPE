###  Ejercicio 08 - Cálculo de área, perímetro e hipotenusa de un triángulo rectángulo  ###

import math

while True:
    base = input("\nIntroduzca la base: ")
    if base.isdigit():
        base = int(base)
        break

while True:
    altura = input("Introduzca la altura: ")
    if altura.isdigit():
        altura = int(altura)
        break

hipotenusa = math.sqrt(math.pow(base,2) + math.pow(altura,2))

area = (base * altura) / 2
perimetro = base + altura + hipotenusa

print("   El área es: ",int(area))
print("   La hipotenusa es: ",int(hipotenusa))
print("   El perímetro es: ",int(perimetro))