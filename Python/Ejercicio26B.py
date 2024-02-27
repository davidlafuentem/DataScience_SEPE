##  Ejercicio 26 - Sucesión de Fibonacci usando FOR  ##
# La sucesión de Fibonacci es una de las secuencias de números más famosas de la historia. 
# La llaman "el código secreto de la naturaleza" o la "secuencia divina", porque aparece 
# una y otra vez en estructuras naturales, como los pétalos de un girasol o la cáscara de una piña.

entrada = ''
resultado = 0
v1 = 0
v2 = 1
testigo = True

while testigo == True:
    testigo = False
    entrada = input("Cuántos valores de la secuencia Fibonacci quiere imprimir (mín. 2): ")
    if ord(entrada) < 50:
        testigo = True

entrada = int(entrada)
print(v1,v2,"",end="")

for i in range(entrada-1):
    result = v1 + v2
    print(result,"",end="")
    v1 = v2
    v2 = result

print("\r")