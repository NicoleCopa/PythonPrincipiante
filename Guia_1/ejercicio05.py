"""Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita 
mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer 
término, más el doble producto del primero por el segundo más el cuadrado del segundo."""

#declaramos las variables
a = int()
b = int()
binomio = int()

#mostramos por pantalla el titulo del ejercicio
print("-- B I N O M I O  A L  C U A D R A D O --")
print("")

#preguntamos al usuario el valor de a y b
a = int(input("Ingrese el valor de 'a': "))
b = int(input("Ingrese el valor de 'b': "))

#hacemos el calculo de binomio
binomio = ((a**2) + (2*a*b) + (b**2))

#mostramos en pantalla el resultado pedidio
print("El resultado del binomio al cuadrado es: " + str(binomio))
