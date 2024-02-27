##  Ejercicio 31 - Array de números ordenados  ##
# Realizar un programa que cree un array de 10 posiciones y rellenarlo automáticamente con 10 números distintos 
# del 25 al 50 usando la librería random. Ordenarlo de menor a mayor e imprimir su contenido EN HORIZONTAL para
# comprobar que los números que contiene son correctos y estan ordenados.
import random

limite = 10
orden = False
desordenado = []

for i in range(limite-1):   #Creación con números aleatorios de un array
    desordenado.append(random.randint(25,50))

ordenado = desordenado

print(desordenado)

while not orden:
    orden = True
    for indice,valor in enumerate(desordenado):
        if desordenado[indice] >= desordenado[indice+1]:
            menor_desordenado = desordenado[indice+1]
            mayor_desordenado = desordenado[indice]
            
            ordenado[indice] = menor_desordenado
            ordenado[indice+1] = mayor_desordenado
            print(ordenado)
            orden = False
        elif indice == len(desordenado)-1 and orden == True:
            orden = False

print(ordenado)


