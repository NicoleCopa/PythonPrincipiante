"""Desarrolle un programa que pase un peso de kilogramo a
   libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras."""

#declaración de variables
kilogramo = 0.0
libra = 0.0

#mostramos por pantalla el titulo del ejercicio
print("-- P E S O  A  K I L O G R A M O --")
print("")

#ingreso de variable
kilogramo = float(input("Ingrese un peso en kilogramos: "))

#valildacion si es mayor a 0
if (kilogramo >= 0):
    #sacamos el calculo de los kilos a libras
    libra = kilogramo * 2.2
    #mostramos en pantalla lo pedido
    print("El peso ingresado de", kilogramo, "kg equivale a", libra, "lbrs.")
#si es menor a 0, mostramos un mensaje de error
else:
    print("El valor ingresado debe ser mayor o igual a 0.")
