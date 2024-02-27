##  Ejercicio 13 - Control de contraseñas   ###
# I. Realizar un programa que pida por pantalla un nombre de usuario y una contraseña. 
# A continuación se le preguntará qué datos quiere mostrar mediante una letra. 
# Si elige la letra n mostrará el nombre, si elige la letra c mostrará la contraseña, 
# y si elige la letra t mostrará el nombre y la contraseña.
import getpass
from bullet import Password

#cli = Password("Contraseña: ")
#p= cli.launch()

print("\n")

user = input("Introduzca el nombre de usuario: ")
#password = input("Introduzca un password: ")
password = getpass.getpass("Introduzca un password: ")

while True:
    option = input("¿Qué desea ver, el nombre de usuario (n), la contraseña (c) o ambos (t)")
    if option.isalpha and (option == "n" or option == "c" or option == "t"):
        break

match option:
    case "n":
        message = user
    case "c":
        message = password
    case "t":
        message = user+" "+password

print(message)

