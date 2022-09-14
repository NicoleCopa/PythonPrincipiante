"""Crear un conversor de pies y pulgadas a centímetros."""
#declaramos variables
pies = 0.0
pulgadas = 0.0
centimetros = 0.0
pregunta = 0

#le preguntamos al usuario que desea convertir
pregunta = int(input("¿Que desea convertir a centimetros?: 1-pies 2-pulgadas: "))

#usamos condicional para la opcion elegida
if pregunta == 1:
    #pedimos al usuario la medida en pies
    pies = float(input("Ingrese la medida en píes: "))
    #calculamos los centimetros
    centimetros = 30.48 * pies
    #mostramos en pantalla el mensaje con la conversion hecha
    print(pies, "pies equivalen a: ", centimetros, "centimetros.")
elif pregunta == 2:
    #pedimos al usuario la medida en pulgadas
    pulgadas = float(input("Ingrese la medida en pulgadas: "))
    #calculamos los centimetros
    centimetros = 2.54 * pulgadas
    #mostramos en pantalla el mensaje con la conversion hecha
    print(pulgadas, "cm equivalen a: ", centimetros, "pulgadas.")
else:
    #mostramos mensaje de error en caso de no seleccional un numero valido
    print("Valor ingresado incorrecto")
