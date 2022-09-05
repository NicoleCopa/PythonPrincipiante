"""Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener
el valor del último dígito de un número entero? ¿Y cómo obtendría
los dos últimos dígitos? Desarrolle un programa que cargue un
número entero por teclado, y muestre el último dígito del mismo
(por un lado) y los dos últimos dígitos (por otro lado)."""

num = 0
ultimo = 0
ultimo2 = 0

num = int(input("Ingrese un numero entero: "))

ultimo = num % 10

print("El ultimo digito es:", ultimo)

ultimo2 = num % 100

print("El ultimo digito es:", ultimo2)