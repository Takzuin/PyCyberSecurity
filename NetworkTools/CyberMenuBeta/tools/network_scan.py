import os
import subprocess

def network_scan():
    print("===== Escaneo de Red =====")
    red = input("Introduzca una red (por defecto{192.168.1}): ")
    if red == "":
        red = "192.168.1"
    try:
        rango_inicial = int(input("Introduzca el rango inicial (por ejemplo 1): "))
        rango_final = int(input("Introduzca el rango final (por ejemplo 250): "))
    except ValueError:
        print("Por favor, introduce números válidos para los rangos.")
        return

    if rango_inicial > rango_final:
        print("Debe indicar un rango inicial menor o igual al rango final")
        return
    else:
        lista_ip = []  # Lista de IPs que responden al ping
        for i in range(rango_inicial, rango_final + 1):  # +1 para incluir rango_final
            ip_equipo = f"{red}.{i}"
            print(f"Haciendo ping a IP {ip_equipo}", end="")

            # Usamos subprocess para capturar la salida del ping
            try:
                # Parámetros según el sistema operativo
                parametros = ["ping", "-n" if os.name == "nt" else "-c", "1", "-w", "1000", ip_equipo]
                resultado = subprocess.run(parametros, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Analizar la salida para ver si hay una respuesta real
                if "TTL=" in resultado.stdout:  # Windows
                    lista_ip.append(ip_equipo)
                    print(" [OK]")
                elif "ttl=" in resultado.stdout.lower():  # Linux/macOS
                    lista_ip.append(ip_equipo)
                    print(" [OK]")
                else:
                    print(" [No responde]")
            except Exception as e:
                print(f"Error al hacer ping a {ip_equipo}: {e}")

        print(f"\n===== Resultados =====")
        print(f"IPs que han respondido al ping: {len(lista_ip)}")
        for ip in lista_ip:
            print(ip)
