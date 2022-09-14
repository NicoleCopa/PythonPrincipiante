"""Galería de Arte. Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba
con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros 
son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). Determinar 
cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”."""

#declaramos variables
cuadro1 = 0
cuadro2 = 0
cuadro3 = 0

#mostramos titulo del ejercicio
print("G A L E R I A  D E  A R T E")

#pedimos los años del cuadro al usuario
cuadro1 = int(input("Ingrese de que año es el primer cuadro: "))
cuadro2 = int(input("Ingrese de que año es el segundo cuadro: "))
cuadro3 = int(input("Ingrese de que año es el tercer cuadro: "))

#usamos condicional para saber si todos 
if (cuadro1 < 1901) and (cuadro2 < 1901) and (cuadro3 < 1901):
    print("Todos los cuadros son anteriores al siglo XX.")
    if (cuadro1 < 1981):
        print("")
else:
    print("Los cuadros son superiores al siglo XX")
