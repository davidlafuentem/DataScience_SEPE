## Ejercicio3
## Suponiendo tasa 1 euro = 1.33250 dólares
## Pedir un número de dólares y calcular
## el cambio en euros redondeando a dos decimales.

while True:
    dolares = input("\nIntroduzca los dólares que quiere cambiar a euros: ")
    if dolares.isdigit():
        dolares = float(dolares)
        break

print(dolares," equivalen actualmente a: ",round(dolares * 1.3325,2))