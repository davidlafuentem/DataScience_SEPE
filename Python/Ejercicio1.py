
## Ejercicio 01 - Programa básico de Phyton
## I. Crear un programa en Phyton que pida por pantalla nombre, primer apellido, 
## segundo apellido, edad, código postal, población y teléfono. Posteriormente 
## mostrará los resultados por terminal

print("### Introduzca sus datos personales ###")
      
nombre = input("Nombre: ")
apellido_uno = input("Primer apellido: ")
apellido_segundo = input("Segundo apellido: ")
edad = input("Edad: ")
postal = input("Código postal: ") 
poblacion = input("Población: ")

print("Recopilación de todos los datos: \n")
print(nombre+"\n"+apellido_uno+"\n"+apellido_segundo+"\n"+edad+"\n"+postal+"\n"+poblacion)
