import tools.network_scan
import pyfiglet

def mostrar_banner():
    banner_ascii = pyfiglet.figlet_format("BasicWifiTools")
    github_info = """
    ==============================================
    🌐 Desarrollado por [Takzuin]
    💻 GitHub: https://github.com/takzuin
    Info: Las herramientas son basicas(para una red basica de hogar) por lo que en una red
    que analiza paquetes podria ser muy escandaloso el script
    o simplemente no funcionar.
    ==============================================
    """
    print(banner_ascii)
    print(github_info)

def menu_principal():
    while True:
        mostrar_banner()
        print("Selecciona una opción:")
        print('1. Escaneo de red(Verifica mediante "ping" de redes dentro de un rango ip)')
        print("2. Salir")

        try:
            opcion = int(input("\n👉 Ingresa el número de tu elección: "))
        except ValueError:
            print("\n❌ Opción inválida. Por favor, ingresa un número.")
            continue

        if opcion == 1:
            tools.network_scan.network_scan()
        elif opcion == 2:
            print("\n👋 ¡Gracias por usar las herramientas! Hasta la próxima.")
            break
        else:
            print("\n❌ Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    menu_principal()
