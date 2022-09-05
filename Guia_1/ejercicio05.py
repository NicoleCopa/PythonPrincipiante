"""Cuadrado de un binomio. Plantear un script
directamente en el shell de Python, que permita 
mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al 
cuadrado (suma) es igual al cuadrado del primer 
término, más el doble producto del primero por el 
segundo más el cuadrado del segundo."""

a = int(0)
b = int(0)
binomio = int(0)

# (a+b)^2 = (a^2 + 2ab + b^2)

print("-- B I N O M I O  A L  C U A D R A D O --")
print("")

a = int(input("Ingrese el valor de 'a': "))
b = int(input("Ingrese el valor de 'b': "))

binomio = ((a**2) + (2*a*b) + (b**2))

print("El resultado del binomio al cuadrado es: " + str(binomio))