testigo = True

while( testigo == True):
    testigo = False

    numero = input("Introduce un número positivo mayor")
    if numero <=0:
        print("El número no es válido, repítelo")
        testigo = True