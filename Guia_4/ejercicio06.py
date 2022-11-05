"""Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
 y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. 
 Para simplificarlo vamos a suponer que febrero tiene 28 días."""

#enero: 31 / febrero: 28 / marzo: 31 / abril: 30 / mayo: 31 / junio: 30 / julio: 31 / agosto: 31 / septiembre: 30 / octubre: 31 / noviembre: 30 / diciembre: 31

mesSeleccionado = int()
mes30 = [4, 6, 9, 11]
mes31 = [1, 3, 5, 7, 8, 10, 12]

mesSeleccionado = int(input("Ingrese un número de mes: "))

if mesSeleccionado in mes30:
    print("El mes tiene 30 días.")
elif mesSeleccionado in mes31:
    print("El mes tiene 31 días.")
else:
    print("El mes tiene 28 días.")
