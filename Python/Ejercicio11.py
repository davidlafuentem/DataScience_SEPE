##  Ejercicio 11 - Condición IF anidada         ##

print("\n       Bienvenido a la pizzería Bella Napoli!!!")

while True:
    vegetariana = input("Desea una piza vegetariana (y-n): ")
    if vegetariana.isalpha and (vegetariana == "y" or vegetariana == "n") :
        break

print("Todas nuestra pizzas llevan mozzarella y tomate como base.")
if vegetariana == "y":
    vegetariana = "vegetariana"
    while True:
        extras = input("Puede elegir un extra entre Pimiento y Tofu (p-t): ")
        if extras.isalpha and (extras == "p" or extras == "t"):
            if extras == "p":
                extras = "pimiento"
            elif extras == "t":
                extras = "tofu"
            break
elif vegetariana == "n":
    vegetariana = "no vegetariana"
    while True:
        extras = input("Puede elegir un extra entre Peperoni, Jamón o Salmón (p-j-s): ")
        if extras.isalpha and (extras == "p" or extras == "j" or extras == "s"):
            if extras == "p":
                extras = "peperoni"
            elif extras == "j":
                extras = "jamón"
            elif extras == "s":
                extras = "salmón"
            break

print("   Ha elegido pizza "+vegetariana+", con "+extras+".")
            