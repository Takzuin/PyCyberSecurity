import os

red = input("Introduzca una red (por ejemplo 192.168.1): ")
if red == "":
    red = "192.168.1"
rangoInicial = int(input("Introduzca el rango inicial (por ejemplo 1): "))
rangoFinal = int(input("Introduzca el rango final (por ejemplo 250): "))

if rangoInicial > rangoFinal:
    print("Debe indicar un rango inferior al rango final")
else:
    listaIP = [] #Lista que responden al ping
    for i in range(rangoInicial, rangoFinal, 1):
        ipEquipo = red + "." + str(i)
        print("Haciendo ping a IP" + ipEquipo, end="")
        rep = os.system("ping -n 1 " + ipEquipo + " > 1")
        if rep == 0:
            listaIP.append(ipEquipo)
            print("[OK]")
        else:
            print("[No responde]")

    print("Las Ip que han respondido al ping " + str(len(listaIP)))
    for i in range(len(listaIP)):
        print(listaIP[i])