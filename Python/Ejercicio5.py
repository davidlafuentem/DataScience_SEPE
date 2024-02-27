## Ejercicio 5
## Calcula los segundos que representas una cantidad de días, horas y minutos introducidos por teclado


print("### Introduzca los días, horas y minutos para calcular los segundos equivalente ###")
      
dias = int(input("Días: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

segundos = minutos*60 + horas*60*60 + dias*24*60*601
print("Los segundos totales: ",segundos)

