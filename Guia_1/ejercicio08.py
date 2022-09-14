"""Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas, pulgadas 
centimetros, metros. Sabiendo que: 
1 pie = 12 pulgadas, 
1 yarda = 3 pies, 
1 pulgada = 2.54 centimetros, 
1 metro = 1000 centimetros"""

#declaramos las variables
pies = 0.0
yarda = 0.0
pulgada = 0.0
metro = 0.0
centimetro = 0.0

#mostramos por pantalla el titulo del ejercicio
print("-- C O N V E R S I O N  D E  M E D I D A S --")

#le preguntamos al usuario la medida en pies
pies = float(input("Ingrese una medida en pies: "))

#hacemos los calculos
pulgada = 12 * pies
yarda = 3 * pies
centimetro = pulgada * 2.54
metro = centimetro / 1000

#mostramos por pantalla lo pedido
print("La conversión de medidas por", pies, "pies equivalen a:", pulgada, "pulgadas,", yarda, "yardas,", centimetro, "centimetros y", metro, "metros.")
