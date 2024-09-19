from scapy.all import  ARP, Ether, srp

# Introduce la red que deseas escanear
red = input("Introduzca una red (por ejemplo 192.168.1.0/24): ")
if red == "":
    red = "192.168.1.0/24"

# Crear un paquete ARP
arp = ARP(pdst=red)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
paquete = ether/arp

# Enviar el paquete ARP y obtener las respuestas
respuesta, _ = srp(paquete, timeout=2, verbose=False)

# Crear una lista para almacenar las IPs y MACs que responden
dispositivos = []

for envio, recibo in respuesta:
    # Para cada respuesta, obtener la IP y la MAC
    dispositivos.append({'ip': recibo.psrc, 'mac': recibo.hwsrc})

# Mostrar los dispositivos encontrados
print(f"Dispositivos en la red {red}:")
print("IP" + " "*18 + "MAC")
print("-"*40)
for dispositivo in dispositivos:
    print(f"{dispositivo['ip']:16}    {dispositivo['mac']}")

