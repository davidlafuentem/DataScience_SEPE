##   Ejercicio 32 - Búsqueda de datos en un array (actividad de evaluación)   ##
# Escribir un programa que genere 10 números enteros positivos y negativos entre -100 y 100, 
# descartando el 0, y los vaya almacenando en un array. 
# Al terminar, mostrará por pantalla los siguientes datos:
# • Listado de todos los números.
# • Número menor introducido.
# • Número mayor introducido.
# • Suma de todos los números.
# • Media de la suma de todos los números.
# • Suma de los números positivos.
# • Suma de los números negativos.
# Imprimir su contenido EN HORIZONTAL para comprobar que los números que contiene son correctos y 
# están ordenados.


import random
from os import system

###############################      FUNCIONES      ###############################


###############################         MAIN        ###############################
suma = 0
sum_neg = 0
sum_pos = 0
orden = False
lista = []

system("cls")   #Clear shell
print("###############################         EJERCICIO 32        ###############################")

# for i in range(10):   ##it works but I'll use a simpler way
#     if random.randint(0,1):
#         lista.append(random.choice(range(-100,-1)))
#     else:
#         lista.append(random.choice(range(1,100)))

while (len(lista)<10):
    valor = random.randint(-100,100)
    if valor:   # Exclude the 0 value
        lista.append(valor)

ordenado = lista

print(lista,"Origen")

orden = False
while not orden:
    orden = True
    for indice,valor in enumerate(ordenado):
        if indice < len(ordenado)-1:  # Check the limits of the array
            if lista[indice] > lista[indice+1]:    # Value check
                valor_mayor = lista[indice]
                valor_menor = lista[indice+1]
                ordenado[indice] = valor_menor    # Swap of the min backward
                ordenado[indice+1] = valor_mayor    # Swap of the max forward
                orden = False   # Keep seeking for

print(ordenado,"Ordenado")

for i in ordenado:
    suma = i + suma
    if i > 0:
        sum_pos = i + sum_pos
    else:
        sum_neg = i + sum_neg

print(f"Mayor: {ordenado[-1]}")
print(f"Menor: {ordenado[0]}")
print(f"Suma total: {suma}")
print(f"Media: {round(suma/len(lista),2)}")
print(f"Suma de los negativos: {sum_neg}")
print(f"Suma de los positivos: {sum_pos}")



print("###############################         EJERCICIO 32B        ###############################")
lista.clear()
ordenado.clear()

lista = [(lambda: random.choice(range(-100, -1)) if random.randint(0, 1) else random.choice(range(1, 100)))() for _ in range(10)]

ordenado = lista

print(lista,"Origen")

orden = False
while not orden:
    orden = True
    for indice,valor in enumerate(ordenado):
        if indice < len(ordenado)-1:  # Check the limits of the array
            if lista[indice] > lista[indice+1]:    # Value check
                valor_mayor = lista[indice]
                valor_menor = lista[indice+1]
                ordenado[indice] = valor_menor    # Swap of the min backward
                ordenado[indice+1] = valor_mayor    # Swap of the max forward
                orden = False   # Keep seeking for

print(ordenado,"Ordenado")

print(f"Mayor: {max(lista)}")
print(f"Menor: {min(lista)}")
print(f"Suma total: {sum(lista)}")
print(f"Media: {round(sum(lista)/len(lista),2)}")
print(f"Suma de los positivos: {sum(value for value in lista if value > 0) }")
print(f"Suma de los negativos: {sum(value for value in lista if value < 0) }")

#print(random.sample(range(1,100),10))




