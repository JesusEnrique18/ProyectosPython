PG = float(input("NÚMERO DE PARTIDOS GANADOS: "))
PE = float(input("ÚMERO DE PARTIDOS EMPATADOS: "))
PP = float(input("NÚMERO DE PARTIDOS PERDIDOS: "))
PPG = PG * 3
PPE = PE * 1
PPP = PP * 0
PT = PPG + PPE + PPP
input("El puntaje final es:" + str(PT))
