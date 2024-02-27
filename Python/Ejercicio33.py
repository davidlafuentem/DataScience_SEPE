##   Ejercicio 33 - Manipulación de datos usando arrays   ##
# Escribir un programa que almacene en un array las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua). Después le preguntará al usuario la nota que ha sacado para 
# cada asignatura, admitiendo solamente valores numéricos de 0 a 10. Si no se introduce un valor 
# correcto se seguirá pidiendo una nota válida. El programa deberá mostrar por pantalla las asignaturas 
# que el usuario ha suspendido y tiene que repetir usando el mensaje: "Debes repetir " y las asignaturas.
# Si ha aprobado todas mostrará el mensaje "Has aprobado todo, pasas al curso siguiente".
from os import system


###############################      FUNCIONES      ###############################
def prompt_int(minimum,maximum):
    testigo = True
    while (testigo == True):
        testigo = False
        entrada = input("   -- Introduzca número (entero): ")
        if entrada != "" and entrada.isnumeric() and int(entrada) >= minimum and int(entrada) <= maximum:
            return int(entrada)
        else:
            testigo = True


###############################      MAIN      ###############################
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = list()
passing = True

system("cls")   #Clear shell
print("###############################      Ejercicio33      ###############################")

for i,asignatura in enumerate(asignaturas):
    print(f"Introduzca la nota de {asignaturas[i]}  (0-10).")
    notas.append(prompt_int(0,10))

passing = True  #Flag to know all subjects are beyond 5 value
for i,value in enumerate(notas):
    if notas[i] < 5:    #Result is not ok
        passing = False #There is at least one subject with less than 5 value
        print(f"   DEBE REPETIR {asignaturas[i]}({value})")

if passing: #All subjects are beyond 5 value
    print("   Has aprovado todo!!!  PASAS AL CURSO SIGUIENTE")



print("\n###############################      Ejercicio33B      ###############################")
resultados = [] #List with subject and its note by peers
notas = [-1]*len(asignaturas) #Creat an empty array with the length of "asignaturas"

for i,asignatura in enumerate(asignaturas):  #Introduce notes by subject
    #print(f"Introduzca la nota de {asignaturas[i]} (0-10).")
    #notas.append(prompt_int(0,10))
    print(f"Introduzca la nota de {asignatura} (0-10).")
    notas[i] = prompt_int(0,10)

passing = True  #Flag to know all subjects are beyond 5 value
for i,value in enumerate(notas):
    if notas[i] < 5:    #Result is not ok
        #resultados.append([asignaturas[i],notas[i]])
        passing = False
        print(f"   DEBE REPETIR {asignaturas[i]}(Nota: {value})")

if passing: #All subjects are beyond 5 value
    print("   Has aprovado todo!!!  Pasas al curso siguiente")

# for asignatura, nota in zip(asignaturas,notas):
    # resultados.append([asignatura,nota])

for i in range(len(asignaturas)):
    resultados.append([asignaturas[i],notas[i]])
    
print(f"Matriz de resultados para BD: {resultados}")
    


