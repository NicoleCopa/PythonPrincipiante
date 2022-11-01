"""Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
 (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
 la nota más alta que ha sacado y la menor."""

#declaramos variables y lista
notas = []
ingreso = int()
masAlta = 0
masBaja = 11
#usamos for para que el programa se repita hasta cargar las 5 notas
for i in range (5):
    #pedimos al usuario que ingrese la nota obtenida
    ingreso = int(input("Ingrese la nota obtenida por el alumno (entre 0 y 10): "))
    #usamos máximos y minimos para saber que nota es mayor y menos
    if ingreso > masAlta:
        masAlta = ingreso
    if ingreso < masBaja:
        masBaja = ingreso
    #agregamos la nota a la lista
    notas.append(ingreso)
#usamnos y dividimos sum / len para sacar el promedio
notaMedia = sum(notas)/len(notas)
#mostramos por pantalla lo pedido
print("Todas las notas son:", notas)
print("La nota media es:", round(notaMedia,2))
print("La nota más alta es:", masAlta)
print("La nota más baja es:", masBaja)
