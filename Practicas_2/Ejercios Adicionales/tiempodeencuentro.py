
Auto1 = float(input("Ingresa la velocidad en M/s del auto 1: "))
Auto2 = float(input("Ingresa la velocidad en M/s del auto 2: "))
Distanciainicial = float(input("Ingrese la distacia inicial M: "))
Autos = Auto1 + Auto2
tiempo = Distanciainicial/Autos

print("Tiempo de encuentro entre los vehículos: "  + str(tiempo) +  " segundos")
