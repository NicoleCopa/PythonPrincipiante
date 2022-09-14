"""Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual."""

#declaramos vairables
dolar = 0.0
peso = 0.0
conversion = 0
opcion = 0
cantidad = 0.0

#mostramos por pantalla el titulo del ejercicio
print("-- C O N V E R S O R --")

#preguntamos al usuario el valor del peso
peso = float(input("Ingrese el valor del peso actual: $"))

#le preguntamos al usuario que conversion desea
print("Ingrese que operacion desea hacer:")
opcion = int(input("1- dólares a pesos  /  2- pesos a dólares: "))

#usamos condicional dependiendo de la opcion que elegió
if opcion == 1:
    #preguntamos el valor de la conversion
    dolar = float(input("Ingrese el valor que desea convertir: U$S"))
    #hacemos la cuenta correspondiente
    conversion = dolar * peso
    #mostramos en pantalla lo pedido
    print("La conversion de U$S", dolar, "es de $", conversion)
elif opcion == 2:
    #preguntamos el valor de la conversion
    cantidad = float(input("Ingrese cuantos pesos desea convertir: $"))
    #hacemos la cuenta correspondiente
    conversion = (cantidad * 1)/peso #regla de 3 simples
    #mostramos en pantalla lo pedido
    print("La conversion de ARS$", cantidad, "es de U$S", conversion)
