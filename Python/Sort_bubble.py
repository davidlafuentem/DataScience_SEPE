desordenado = [6, 8, 25, 12, 79, 1, 4, 62]
indice = 0
orden = False

ordenado = desordenado

while not orden:
    orden = True
    indice = 0

    while indice < len(ordenado)-1:
        if ordenado[indice] > ordenado[indice+1]:
            apoyo = ordenado[indice]
            ordenado[indice] = ordenado[indice+1]
            ordenado[indice+1] = apoyo
            orden = False
        indice += 1

print(ordenado)
print(desordenado)