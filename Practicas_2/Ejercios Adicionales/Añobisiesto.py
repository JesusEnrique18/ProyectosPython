print("Este algoritmo determina si un año es bisiesto o no ")
print("---------------------------------------------------")
año = int(input("Ingrese el año:  "))
if año % 4 != 0: #primero determinamos si el año es divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")