## Ejercicio4 Cálculo perímetro, área del círculo, volumen de la esfera

import math


while True:
    radio = input("\nIntroduzca el radio: ")
    if radio.isdecimal():
        radio = float(radio)
        break

print("Con un radio de" ,radio,
      "\n   El perímetro sería: ",(2*math.pi*radio),
      "\n   El área sería: ",(math.pi*radio**2),
      "\n   El volumen de la esfera sería: ",(4*math.pi*radio**3))
