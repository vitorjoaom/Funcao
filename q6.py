def converterhoras(hora,a,p):
    while(hora<25):
        hora = float(input("Digite a hora no seu relógio: "))  
        if(hora == 12):
            print(f"Hora: {hora}")
        elif(hora>12 and hora<25):
            p = hora -12
            print(f"Hora: {p} P.M.")
        elif(hora<12 and hora>=0):
            a = hora
            print(f"Hora: {a} A.M.")
        else:
            print("A hora está errada!")
            break

converterhoras(5,2,14)            