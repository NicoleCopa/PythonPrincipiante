"""Queremos guardar los nombres y las edades de los alumnos de un curso. 
Realiza un programa que introduzca el nombre y la edad de cada alumno. 
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) 
Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad)."""

listaNombres = []
alumnoMayor = []
ingresoNombre = str()
ingresoEdades = int()
maximo = int()

while ingresoNombre != "*":
    ingresoNombre = str(input("Ingrese el nombre del alumno - para finalizar ingrese '*': "))
    if ingresoNombre != "*":
        ingresoEdades = int(input("Ingrese la edad del alumno: "))
    if ingresoEdades >= 18:
        listaNombres.append(ingresoNombre)
    if maximo < ingresoEdades:
        alumnoMayor.append(ingresoNombre)
        maximo = ingresoEdades

print("Los alumnos mayores de edad son:", listaNombres)
print("Los alumnos mayores son:", alumnoMayor)
