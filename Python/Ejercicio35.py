##   Ejercicio 35 - Operaciones con matrices cuadradas (actividad de evaluación)
# Generar dos matrices cuadradas A y B del mismo tamaño, solicitando el tamaño de ambas al operador
# desde un mínimo de 2x2 hasta un  máximo de 5X5. Controlar que no se introducen valores de tamaño 
# de matriz menores de 2 ni mayores de 5, si no es así continuar pidiendo el tamaño. Rellenar los 
# números de ambas matrices automáticamente entre -10 y 10. 
# Operaciones a realizar:
# Obtener la matriz C resultante de la suma de las matrices A y B.
# Generar automáticamente un número escalar N entre 1 y 5, multiplicarlo por la matriz C y obtener la matriz D.
# Generar la matriz E como traspuesta de la matriz D.
# Mostrar los resultados de las operaciones anteriores, dibujando en el terminal:
# Las matrices A, B, C, D y E, identificando cada una de ellas.
# El número escalar N
# Notas: 
# Para representar matrices mediante arrays se usan listas anidadas, representando cada vector fila en una lista.
# Una matriz traspuesta se obtiene invirtiendo filas y columnas.
# Para sumar matrices cuadradas se suman los valores de cada posición y el resultado es el valor de cada posición 
# en la matriz final.
# El producto de una matriz por un número escalar da como resultado otra matriz donde sus valores resultan del 
# producto de cada valor original y el número escalar.

from os import system
import random

###############################      FUNCIONES      ###############################
# Get a integer number between min and max
def prompt_int(minimum,maximum):
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca número (entero): ")
        if entrada != "" and entrada.isnumeric() and int(entrada) >= minimum and int(entrada) <= maximum:
            return int(entrada)
        else:
            testigo = True


##################################      MAIN      ##################################
system("clear")   #Clear shell

print("###############################      Ejercicio35      ###############################")

print("Introduce el orden de la matriz (2min - 5max): ")
order = prompt_int(2,5) # Get the arrays order

# Fill the matrix with randoms numbers between -10 and 10, or zeros
matrixA = [[random.randint(-10,10) for _ in range(order)] for _ in range(order)]
matrixB = [[random.randint(-10,10) for _ in range(order)] for _ in range(order)]
matrixC = [[0 for j in range(order)] for _ in range(order)]    #Create matrixC 
matrixD = [[0 for j in range(order)] for _ in range(order)]    #Create matrixD
matrixE = [[0 for j in range(order)] for _ in range(order)]    #Create matrixE 

print("MatrixA:")
[print(row) for row in matrixA] 
    
print("MatrixB:")
[print(row) for row in matrixB]

print("---- Suma de matrices A y B en C----")
for i in range(order):   
    for ii in range(order):
        matrixC[ii][i] = matrixA[ii][i] + matrixB[ii][i]
print("MatrixC:")
[print(row) for row in matrixC]

multiplier = random.randint(1,5)
print(f"---- Multiplicación matriz C X{multiplier} en matriz D ----")

matrixD = [[(matrixC[ii][i]) * multiplier for i in range(order)]  for ii in range(order)]
print("MatrixD:")
[print(row) for row in matrixD]

print("---- Transpuesta de matriz D en E----")
for i,row in enumerate(matrixD): # Take each row that will become at each column
    for ii,value in enumerate(row): # Take each position of the row (ii) and swap it in column (i)
        matrixE[ii][i] = value
print("MatrixE:")
[print(row) for row in matrixE]