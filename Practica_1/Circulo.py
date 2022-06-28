Radio = float(input("Ingresa el valor del radio: "))
Pi = float(3.1416)
Paso1 = int(pow(Radio,2))  #int(Radio**2) otra forma de elevar el radio al cuadrado
paso2= float(Paso1 * Pi)
redondear= round(paso2, 2) # funcion round sirve para redondear el numero a dos decimales 
print("El área del círculo es:" + str(redondear))
