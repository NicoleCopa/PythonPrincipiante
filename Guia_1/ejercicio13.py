"""Crear un conversor de dólares a pesos y pesos
a dólares, donde se ingrese por teclado el valor
del peso actual."""

dolar = 0.0
peso = 0.0
conversion = 0
opcion = 0
cantidad = 0.0

peso = float(input("Ingrese el valor del peso actual: $"))

print("Ingrese que operacion desea hacer:")
opcion = int(input("1- dólares a pesos  /  2- pesos a dólares: "))
if opcion == 1:
    dolar = float(input("Ingrese el valor que desea convertir: U$S"))
    conversion = dolar * peso
    print("La conversion de U$S", dolar, "es de $", conversion)
elif opcion == 2:
    cantidad = float(input("Ingrese cuantos pesos desea convertir: $"))
    conversion = (cantidad * 1)/peso #regla de 3 simples
    print("La conversion de ARS$", cantidad, "es de U$S", conversion)
