"""Desarrolle un programa que pase un peso de kilogramo a
   libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras."""

#declaración de variables
kilogramo = 0.0
libra = 0.0

print("-- P E S O  A  K I L O G R A M O --")
print("")

#ingreso de variable
kilogramo = float(input("Ingrese un peso en kilogramos: "))

#valildacion
if (kilogramo >= 0):
    libra = kilogramo * 2.2
    print("El peso ingresado de", kilogramo, "kg equivale a", libra, "lbrs.")
else:
    print("El valor ingresado debe ser mayor o igual a 0.")
