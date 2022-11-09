"""Queremos guardar los nombres y las edades de los alumnos de un curso. 
Realiza un programa que introduzca el nombre y la edad de cada alumno. 
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) 
Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad)."""

#inicializamos variables y listas
listaNombres = []
alumnoMayor = []
ingresoNombre = str()
ingresoEdades = int()
maximo = int()

#insertamos while para que se repita el programa hasta que se ingrese un *
while ingresoNombre != "*":
    #pedimos al usuario que ingrese un nombre
    ingresoNombre = str(input("Ingrese el nombre del alumno - para finalizar ingrese '*': "))
    #si el nombre es diferente a *, pedimos que ingrese la edad
    if ingresoNombre != "*":
        ingresoEdades = int(input("Ingrese la edad del alumno: "))
    #si la edad es mayor a 18, agregamos el nombre a listaNombres
    if ingresoEdades >= 18:
        listaNombres.append(ingresoNombre)
    #si la edad es mayor a la condicional maximo, agregamos el nombre a alumnoMayor
    if maximo < ingresoEdades:
        alumnoMayor.append(ingresoNombre)
        maximo = ingresoEdades

#mostramos por pantalla lo pedido
print("Los alumnos mayores de edad son:", listaNombres)
print("Los alumnos mayores son:", alumnoMayor)
