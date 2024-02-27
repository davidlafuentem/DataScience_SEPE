## Ejercicio 6
## Calcula los días, horas y minutos correspondientes a los segundos introducidos por teclado

print("\n\n###   PROGRAMA CÁLCULO DE DÍAS, HORAS, MINUTOS Y      ###\n"
          "###   SEGUNDOS, DADA UNA CANTIDAD INICIAL DE SEGUNDOS ###\n")

       
while True:
    segundos = input("Introduzca los segundos: ")
    if segundos.isdigit():
        segundos = int(segundos)
        break
        
dias = int(segundos / 86400)
resto_dia = segundos % 86400

horas = int(resto_dia / 3600)
resto_horas = resto_dia % 3600

minutos = int(resto_horas / 60)
segundos = resto_horas % 60

print("\nResultados:")
print("   Días: ",dias,"\n   Horas: ",horas,"\n   Minutos: ",minutos,"\n   Segundos: ",segundos)


