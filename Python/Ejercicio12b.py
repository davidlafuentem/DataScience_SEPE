##  Ejercicio 12 - Condición SWITCH (MATCH)     ##

print("\n       Bienvenido a la pizzería Bella Napoli!!!")

while True:
    vegetariana = input("Desea una piza vegetariana (y-n): ")
    if vegetariana.isalpha and (vegetariana == "y" or vegetariana == "n") :
        break

print("Todas nuestra pizzas llevan mozzarella y tomate como base.")

match vegetariana:
    case "y":
        vegetariana = "vegetariana"
        while True:
            extras = input("Puede elegir un extra entre Pimiento y Tofu (p-t): ")
            if extras.isalpha and (extras == "p" or extras == "t"):
                match extras:
                    case "p":
                        extras = "pimiento"
                    case "t":
                        extras = "tofu"    
                break
    case "n":
        vegetariana = "no vegetariana"
        while True:
            extras = input("Puede elegir un extra entre Peperoni, Jamón o Salmón (p-j-s): ")
            if extras.isalpha and (extras == "p" or extras == "j" or extras == "s"):
                match extras:
                    case "p":
                        extras = "peperoni"    
                    case "j":
                        extras = "jamón"
                    case "s":
                        extras = "salmón"
                break

print("   Ha elegido pizza "+vegetariana+", con "+extras+".")
