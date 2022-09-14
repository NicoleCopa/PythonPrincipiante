"""Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría
los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo
(por un lado) y los dos últimos dígitos (por otro lado)."""

#declaramos variables
num = 0
ultimo = 0
ultimo2 = 0

#mostramos por pantalla el titulo del ejercicio
print("-- U L T I M O S  D I G I T O S --")

#preguntamos al usuario el numero
num = int(input("Ingrese un numero entero: "))

#dividimos el numero en 10 y sacamos el resto
ultimo = num % 10

#mostramos por pantalla el ultimo digito
print("El ultimo digito es:", ultimo)

#dividimos el numero en 100 y sacamos el resto
ultimo2 = num % 100

#mostramos por pantalla los ultimos dos digitos
print("El ultimo digito es:", ultimo2)
