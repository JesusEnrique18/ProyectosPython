print("Este algoritmo.Calcula un aumento del 15%, si el sueldo de un trabajador  es inferior a $1000.")
print("---------------------------------------------------------------------------------------------")
sueldo = float (input ('Ingresa el  sueldo: '))
if sueldo<1000:
    aumento=sueldo * 0.15 
    sueldonuevo = sueldo + aumento
    print (" Aumento $" + str (aumento) + " Nuevo sueldo $" + str (sueldonuevo))
else:
    print("No hay aumento")
