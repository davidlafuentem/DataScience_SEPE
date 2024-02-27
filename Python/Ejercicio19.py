##   Ejercicio 19 - Modificar cadenas de caracteres   ###

while True:
    entrada = input("Introduzca su teléfono (+2 dígitos prefijo-teléfono 9 dígitos-extension: ")
    if entrada[0]=="+" and entrada[1:3].isalnum() and entrada[3] == "-" and entrada[4:13].isalnum() and entrada[13]=="-" and entrada[-2:-1].isalnum() and len(entrada)==16:
        prefijo = entrada[1:3]
        telefono = entrada[4:13]
        extension = entrada[-2:]
        break


print("Su prefijo es:",prefijo)
print("Su número de teléfono es: ",telefono)
print("Su extensión es: ",extension)