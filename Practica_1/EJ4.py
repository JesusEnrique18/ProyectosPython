import math 
AX = float(input("Coordenada X de A: "))
AY = float(input("Coordenada Y de A: "))
BX = float(input("Coordenada X de B: "))
BY = float(input("Coordenada  Y de B: "))

D1 = math.sqrt(((AX - BX)**2) + ((AY - BY)**2))
redondear= round(D1, 2)
input("Distancia entre el punto A y B es: " + str(redondear))