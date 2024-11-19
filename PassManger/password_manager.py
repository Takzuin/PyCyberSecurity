def obtener_contraseña():
    """Solicita al usuario que ingrese una contraseña."""
    try:
        return input("Ingrese la contraseña a verificar (o 'salir' para terminar): ")
    except EOFError:
        print("\nEntrada no válida. Por favor, intenta de nuevo.")
        return ""

def es_longitud_valida(contraseña):
    """Verifica si la contraseña tiene al menos 8 caracteres."""
    return len(contraseña) >= 8

def tiene_mayuscula(contraseña):
    """Verifica si la contraseña contiene al menos una letra mayúscula."""
    return any(c.isupper() for c in contraseña)

def tiene_numero(contraseña):
    """Verifica si la contraseña contiene al menos un número."""
    return any(c.isdigit() for c in contraseña)

def tiene_caracter_especial(contraseña):
    """Verifica si la contraseña contiene al menos un carácter especial."""
    caracteres_especiales = "@#$%^&*()-_+=!?"
    return any(c in caracteres_especiales for c in contraseña)

def analizar_contraseña(contraseña):
    """Analiza la seguridad de la contraseña según criterios predefinidos."""
    criterios_cumplidos = 0
    if es_longitud_valida(contraseña):
        criterios_cumplidos += 1
    if tiene_mayuscula(contraseña):
        criterios_cumplidos += 1
    if tiene_numero(contraseña):
        criterios_cumplidos += 1
    if tiene_caracter_especial(contraseña):
        criterios_cumplidos += 1

    if criterios_cumplidos == 4:
        return "Fuerte"
    elif 2 <= criterios_cumplidos < 4:
        return "Moderada"
    else:
        return "Débil"

def sugerir_mejoras(contraseña):
    """Proporciona sugerencias para mejorar la contraseña."""
    sugerencias = []
    if not es_longitud_valida(contraseña):
        sugerencias.append("usa al menos 8 caracteres")
    if not tiene_mayuscula(contraseña):
        sugerencias.append("incluye al menos una letra mayúscula")
    if not tiene_numero(contraseña):
        sugerencias.append("añade al menos un número")
    if not tiene_caracter_especial(contraseña):
        sugerencias.append("añade al menos un carácter especial")
    return ", ".join(sugerencias)

def main():
    """Función principal que controla el flujo del programa."""
    while True:
        contraseña = obtener_contraseña()
        if contraseña.lower() == "salir":
            print("¡Hasta luego!")
            break
        elif not contraseña:
            continue  # Si la entrada es inválida, solicita de nuevo

        nivel = analizar_contraseña(contraseña)
        print(f"Nivel de seguridad: {nivel}")

        if nivel != "Fuerte":
            print(f"Sugerencias para mejorar: {sugerir_mejoras(contraseña)}")

if __name__ == "__main__":
    main()
