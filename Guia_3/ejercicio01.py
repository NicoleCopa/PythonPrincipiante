"""Comisión de vendedores. Una empresa debe calcular el total de comisiones que debe abonar por ventas 
realizadas por sus vendedores, para ello les solicita un sistemita que le permita calcular dichos montos. 
Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).Usted debe solicitar el 
ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría 
igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los 
siguientes cálculos:
Categoría1:cobra una comisión de 10%
Categoría2: cobra una comisión de 25%
Categoría3:cobra una comisión de 30%
Categoría4:cobra una comisión de 40%
Una vez procesadas todas las ventas, mostrar el total de comisiones a pagar por cada categoría de vendedor que es en la empresa,
junto con el total general."""

#declaramos variables
categoria = int()
ventas = float()
comision1 = float()
comision2 = float()
comision3 = float()
comision4 = float()
comisionTotal = float()

#mostramos por pantalla el titulo del ejercicio
print("-- C O M I S I O N  D E  V E N D E D O R E S --")
print("")

#preguntamos al usuario cual es su categoria
categoria = int(input("Ingrese su categoria (1-4), para finalizar ingrese '0': "))

#el programa termina cuadnos e ingresa 0 en categoria
while (categoria != 0):
    #validacion de categoria con while
    while (categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4):
        print("ERROR, ingresó una categoria incorrecta.")
        categoria = int(input("Ingrese su categoria (1-4), para finalizar ingrese '0': "))

    #preguntamos el total de la venta
    ventas = float(input("Ingrese el total de la venta: $"))

    #usamos condicional para ver las comisiones de cada categoria
    if categoria == 1:
        comision1 = comision1 + (ventas * 0.10)
    elif categoria == 2:
        comision2 = comision2 + (ventas * 0.25)
    elif categoria == 3:
        comision3 = comision3 + (ventas * 0.30)
    elif categoria == 4:
        comision4 = comision4 + (ventas * 0.40)
    
    #volvemos a preguntar al usuario cual es su categoria
    categoria = int(input("Ingrese su categoria (1-4), para finalizar ingrese '0': "))

#sacamos el total general de las comisiones
comisionTotal = comision1 + comision2 + comision3 + comision4

#mostramos en pantalla lo pedido
print("******************************************************************")
print("El total de comisiones por cada categoria es:")
print("CATEGORIA 1 = "+ str(round(comision1,2)) + "%.")
print("CATEGORIA 2 = "+ str(round(comision2,2)) + "%.")
print("CATEGORIA 3 = "+ str(round(comision3,2)) + "%.")
print("CATEGORIA 4 = "+ str(round(comision4,2)) + "%.")
print("El total general de las comisiones es: "+ str(round(comisionTotal,2)) + "%.")
print("******************************************************************")