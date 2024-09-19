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
            parametros = ["ping", "-n" if os.name == "nt" else "-c", "1", "-w", "1000", ipEquipo]
            resultado = subprocess.run(parametros, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Analizar la salida para ver si hay una respuesta real
            if "TTL=" in resultado.stdout:  # Windows
                listaIP.append(ipEquipo)
                print(" [OK]")
            elif "ttl=" in resultado.stdout.lower():  # Linux/macOS
                listaIP.append(ipEquipo)
                print(" [OK]")
            else:
                print(" [No responde]")
        except Exception as e:
            print(f"Error al hacer ping a {ipEquipo}: {e}")

    print(f"Las IPs que han respondido al ping: {len(listaIP)}")
    for ip in listaIP:
        print(ip)
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
            parametros = ["ping", "-n" if os.name == "nt" else "-c", "1", "-w", "1000", ipEquipo]
            resultado = subprocess.run(parametros, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Analizar la salida para ver si hay una respuesta real
            if "TTL=" in resultado.stdout:  # Windows
                listaIP.append(ipEquipo)
                print(" [OK]")
            elif "ttl=" in resultado.stdout.lower():  # Linux/macOS
                listaIP.append(ipEquipo)
                print(" [OK]")
            else:
                print(" [No responde]")
        except Exception as e:
            print(f"Error al hacer ping a {ipEquipo}: {e}")

    print(f"Las IPs que han respondido al ping: {len(listaIP)}")
    for ip in listaIP:
        print(ip)
