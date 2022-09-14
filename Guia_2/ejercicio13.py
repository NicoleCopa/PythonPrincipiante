"""Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
Por cada habitantes e ingresa: sexo (M/F)y edad. La carga de datos analiza al ingresar cualquier otro valor 
para sexo. El programa debe informar: A qué sexo corresponde la mayor cantidad de habitantes
(considerar que puede ser igual) Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún
varón que supere los 80 años de edad."""

#declaramos variables
sexo = str()
edad = int()
cantidadM = int()
cantidadF = int()
mayor80 = int()
edadEscolar = int()

#mostramos por pantalla el titulo del ejercicio
print("-- C E N S O --")
print("")

#pedimos al usuario que ingrese el sexo del habitante
sexo = str(input("Ingrese el sexo del habitante (M/F): "))

#usamos while mientras que el sexo sea M o F
while (sexo == "M" or sexo == "F"):
    #pedimos al usuario la edad del habitante
    edad = int(input("Ingrese la edad del habitante: "))
    #usamos condicional dependiendo del sexo
    if sexo == "M":
        #usamos contador para saber cuantos habitantes de sexo M hay
        cantidadM = cantidadM + 1
        #usamos condicional si la edad supera los 80
        if edad > 80:
            #usamos contador para saber cuantos hombres hay mayores a 80 años
            mayor80 = mayor80 + 1
    else:
        #usamos contador para saber cuantos habitantes de sexo F hay
        cantidadF = cantidadF +1
        #usamos condicional si la edad está entre los 4 y 18
        if edad >= 4 and edad <= 18:
            #usamos contador para saber cuantas mujeres hay entre los 4 y 18 años
            edadEscolar = edadEscolar +1
    #volvemos a pedir el sexo del siguiente habitante
    sexo = str(input("Ingrese el sexo del habitante (M/F): "))

#usamos condicional para saber si hay mas habitantes de sexo M o F
if cantidadF > cantidadM:
    #mostramos mensaje por pantalla que hay mas mujeres que hombres
    print("La mayor cantidad de habitantes es del sexo FEMENINO.")
elif cantidadF < cantidadM:
    #mostramos mensaje por pantalla que hay mas hombres que mujeres
    print("La mayor cantidad de habitantes es del sexo MASCULINO.")
elif cantidadF == cantidadM:
    #mostramos mensaje por pantalla que hay la misma cantidad por sexo
    print("La cantidad de habitantes es igual de ambos sexos.")
#mostramos por pantalla la cantidad de mujeres en edad escolar
print("La cantidad de mujeres en edad escolar es de:", edadEscolar)
#mostramos por pantalla la cantidad de hombres mayores a 80 años
print("La cantidad de hombres que superan los 80 años de edad es de:", mayor80)
