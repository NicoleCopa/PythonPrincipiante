"""Jornal de un Operario. Se necesita desarrollar un programa
 para el área de recursos humanos de una empresa que permita 
 informar el jornal de un determinado operario. Usted deberá 
 cargar por teclado el código de turno que el operario trabajó 
 ese día (1- representa Diurno y 2- representa Nocturno) y la 
 cantidad de horas trabajadas. La política de trabajo en la 
 empresa es que los operarios de la misma pueden trabajar en 
 el turno diurno o nocturno. Si un operario trabaja en el turno 
 nocturno el pago es 40.60 pesos la hora, si lo hace en el turno 
 diurno cobra 35.50 pesos la hora."""

turno = 0
horas = 0.0
pago = 0.0

turno = int(input("Ingrese en que turno trabaja (1-Diurno 2-Nocturno): "))
horas = float(input("Ingrese la cantidad de horas trabajadas: "))

if turno == 1:
    pago = 35.50 * horas
    print("El pago total es: $" + str(pago))
elif turno == 2:
    pago = 40.60 * horas
    print("El pago total es: $" + str(pago))
else:
    print("El valor ingresado no corresponde a ningun turno.")
    