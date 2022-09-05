"""Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor,
correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto
del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre."""

#declaramos variables
sueldo = 0.0
aguinaldo = 0.0
maximo = 0.0
minimo = 99999999999
total = 0.0
mes = 1
promedio = 0.0

#mostramos por pantalla
print("-- S U E L D O S  Y  A G U I N A L D O --")

#usamos un while para repetir los meses hasta que llegue a 6
while mes <= 6:
    print("Mes 0"+ str(mes))
    #pedimos el sueldo al usuario
    sueldo = float(input("Ingrese su sueldo del mes: $"))
    #usamos maximo para ver el sueldo mas alto del periodo
    if sueldo > maximo:
        maximo = sueldo
    #usamos minimo para saber el mes en que se pagó menos
    if sueldo < minimo:
        minimo = mes
    #usamos acumulador para todos los sueldos del semestre
    total = total + sueldo
    #usamos contador para los meses
    mes = mes + 1
#sacamos aguinaldo y promedio
aguinaldo = maximo/ 2
promedio = total / 6
#mostramos por pantalla
print("")
print("El aguinaldo es de: $"+ str(aguinaldo))
print("El mes en que recibió el sueldo más bajo es el 0" + str(minimo))
print("El sueldo promedio del semestre es: $" + str(promedio))