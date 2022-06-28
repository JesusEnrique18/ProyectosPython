import math 
print("Copia de seguridad")
print("---------------------------------------------")
GB = float(input("Número de Gygabyte del disco duro: "))
MG = (GB*1024)
MD = MG / 1.44
print("Numero de Megabytes es de : "+ str(MG)) 

print("Numero de Discos necesarios: ", math.ceil(MD)) 

