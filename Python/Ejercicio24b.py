##  Ejercicio 24 - Control de Contraseñas WHILE con IF  ##
# Realizar un programa que pida por pantalla un nombre de usuario. 
# A continuación pedirá una contraseña y solicitará repetir la contraseña. 
# Se establecerán las siguientes condiciones:
# Si el nombre del usuario está vacío el programa seguirá pidiendo un nuevo nombre de usuario.
# Si las contraseñas están vacías el programa seguirá pidiendo unas nuevas contraseñas.
# Si la primera contraseña es distinta de la segunda el programa mostrará un mensaje de error y 
# pedirá unas nuevas contraseñas.
# Cuando el nombre del usuario y las contraseñas estén correctas el programa finalizará mostrando el nombre 
# del usuario y una de las contraseñas.

nombre = ''
contraseña = ''


if nombre == '':
    testigo = True
    while testigo == True:
        testigo = False
        nombre = input("Introduzca su nombre: ")
        if  not nombre.isalpha() or nombre == '':
            print("   El nombre no es correcto (no puede tener números o estar vacía)")
            testigo = True

if contraseña == '':
    testigo = True
    while testigo == True:
        testigo = False
        contraseña = input("Introduzca su contraseña: ")
        if contraseña == '':
            print("   La contraseña no puede estar vacía")
            testigo = True
    
    testigo = True
    while testigo == True:
        testigo = False
        contraseña2 = input("Comprobación, vuelva a introducir su contraseña: ")
        if contraseña2 == '' or contraseña != contraseña2:
            print("   La contraseña no es igual o está vacía.")
            testigo = True
            while testigo == True:
                testigo = False
                entrada = input("Desea volver a comprobar la contraseña (y-n): ")
                if entrada.isalpha and entrada == "y":
                    testigo = True
                    contraseña2 = ''
                    break
                elif entrada.isalpha and entrada == "n":
                    testigo = False
        elif contraseña != '' and contraseña == contraseña2:
            print("Usuario: ",nombre,"\nContraseña: ",contraseña)
            testigo = False

