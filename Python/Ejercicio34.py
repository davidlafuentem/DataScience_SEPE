##   Ejercicio 34 - Introduccion a las matrices usando tablas
# Escribir un programa que almacene la siguiente matriz cuadrada de 3x3 en una tabla y la muestre
# por pantalla:  (1 -3  2)
#                (2  5  0)
#                (0 -1 -2)

# Transpuesta    ( 1  2  0)
#                (-3  5 -1)
#                ( 2  0 -2)

# Obtener de esta matriz su equivalente traspuesta y la muestre por pantalla.
# Para representar matrices mediante arrays se usan listas anidadas, representando cada vector fila 
# en una lista. Una matriz traspuesta se obtiene invirtiendo filas y columnas.
from os import system


###############################      FUNCIONES      ###############################

###############################      MAIN      ###############################
matrix = [[1,-3,2],[2,5,0],[0,-1,-2]]
ttable = [[0,0,0],[0,0,0],[0,0,0]]


system("clear")   #Clear shell
print("###############################      Ejercicio34      ###############################")

print(f"Original   {matrix}")
for row in matrix:  # Show each row in the original table
    print(f"   {row}")

for i,row in enumerate(matrix): # Take each row that will become at each column
    for ii,value in enumerate(row): # Take each position of the row (ii) and swap it in column (i)
        ttable[ii][i] = value

print(f"Transposed {ttable}")
for row in ttable:
    print(f"   {row}")

print("\n")




