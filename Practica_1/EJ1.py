
RC = float(input("Ingresa el numero de respuestas correctas: "))
RI = float(input("Ingresa el numero de respuestas incorrectas: "))
RB = float(input("Ingresa el numero de respuestas en blanco: "))
PRC = RC *3
PRI= RI * -1
PRB= RB * 0

PF= PRC + PRI + PRB

input("Calificacion final es:" + str(PF))