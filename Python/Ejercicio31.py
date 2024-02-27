##  Ejercicio 31 - Array de números ordenados  ##
# Realizar un programa que cree un array de 10 posiciones y rellenarlo automáticamente con 10 números distintos 
# del 25 al 50 usando la librería random. Ordenarlo de menor a mayor e imprimir su contenido EN HORIZONTAL para
# comprobar que los números que contiene son correctos y estan ordenados.
import random
from os import system

orden = False
notin = True
desordenado = []
posiciones = 9


for i in range(posiciones):   # Creation array of random numbers 
    notin = True
    while notin:    # For introduce not repeated numbers
        notin = False
        number = random.randint(25,50)

        for valor in desordenado: # 
            if number == valor:
                notin = True    # Keep searching for a non repeated number
        
        if not notin:   # If there has not been found any repeated
            desordenado.append(number)


system("cls")   #Clear shell
ordenado = desordenado

print(desordenado,"Origen")

while not orden:
    orden = True
    for indice,valor in enumerate(ordenado):
        if indice < len(ordenado)-1:  # Check the limits of the array
            if desordenado[indice] > desordenado[indice+1]:    # Value check
                valor_mayor = desordenado[indice]
                valor_menor = desordenado[indice+1]
                ordenado[indice] = valor_menor    # Swap of the min backward
                ordenado[indice+1] = valor_mayor    # Swap of the max forward
                orden = False   # Keep seeking for

print(ordenado,"Ordenado")

