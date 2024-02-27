##   Ejercicio 29 - Array de Fibonacci   ###
# Realizar un programa que genere un array de N posiciones de la serie de Fibonacci con tantos valores como diga el usuario. 
# Al ejecutarse debe preguntar “Cuantos números desea imprimir? (mínimo 2 números)”, y leer el número que introduce el usuario. 
# El número deberá ser positivo y mayor que 2. Si no cumple los requisitos el programa seguirá pidiendo un número.
# Una vez generado el array imprimir su contenido EN HORIZONTAL.

entrada = ''
result = []
v1 = 0
v2 = 1
testigo = True

print("\n")

while testigo == True:
    testigo = False
    entrada = input("Cuántos valores de la secuencia Fibonacci quiere imprimir (mín. 2): ")
    if ord(entrada) < 50:
        testigo = True

entrada = int(entrada)
result.append(v1)
result.append(v2)

for i in range(entrada-2):
    result.append(v1 + v2)
    v1 = v2
    v2 = result[-1]

for i in result:
    print(f"{i}, ",end="")

print(result,end="")
print("\r")