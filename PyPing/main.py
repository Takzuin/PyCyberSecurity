import os
import subprocess

red = input("Introduzca una red (por ejemplo 192.168.1): ")
if red == "":
    red = "192.168.1"
rangoInicial = int(input("Introduzca el rango inicial (por ejemplo 1): "))
rangoFinal = int(input("Introduzca el rango final (por ejemplo 250): "))

if rangoInicial > rangoFinal:
    print("Debe indicar un rango inferior al rango final")
else:
    listaIP = []  # Lista de IPs que responden al ping
    for i in range(rangoInicial, rangoFinal + 1):  # +1 para incluir rangoFinal
        ipEquipo = red + "." + str(i)
        print(f"Haciendo ping a IP {ipEquipo}", end="")

        # Usamos subprocess para capturar la salida del ping
        try:
            # Parámetros según el sistema operativo
            rep = subprocess.run(
                ["ping", "-n" if os.name == "nt" else "-c", "1", ipEquipo],
                stdout=subprocess.DEVNULL,  # Redirigir la salida para no mostrarla
                stderr=subprocess.DEVNULL
            )
            if rep.returncode == 0:
                listaIP.append(ipEquipo)
                print(" [OK]")
            else:
                print(" [No responde]")
        except Exception as e:
            print(f"Error al hacer ping a {ipEquipo}: {e}")

    print(f"Las IPs que han respondido al ping: {len(listaIP)}")
    for ip in listaIP:
        print(ip)
