"""Crear un conversor de pies y pulgadas 
a centímetros."""

#1 pie = 12 pulgadas
#1 pulgada = 2.54 centimetros

pies = 0.0
pulgadas = 0.0
centimetros = 0.0
pregunta = 0

pregunta = int(input("¿Que desea convertir a centimetros?: 1-pies 2-pulgadas: "))
centimetros = float(input("¿Cuantos centimetros desea convertir?: "))

if pregunta == 1:
    pies = 30.48 * centimetros
    print(centimetros, "cm equivalen a: ", pies, "pies.")
elif pregunta == 2:
    pulgadas = 2.54 * centimetros
    print(centimetros, "cm equivalen a: ", pulgadas, "pulgadas.")
else:
    print("Valor ingresado incorrecto")