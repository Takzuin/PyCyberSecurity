from cryptography.fernet import Fernet
import hashlib
import base64

# Función para generar clave a partir de una contraseña
def generar_clave(contraseña):
    # Usar SHA-256 para derivar la clave
    hash_entrada = hashlib.sha256(contraseña.encode()).digest()  # Convertir contraseña a hash de 32 bytes
    clave_base64 = base64.urlsafe_b64encode(hash_entrada)  # Convertir a base64
    return clave_base64

# Función para cifrar el texto
def cifrar_texto(texto, contraseña):
    clave = generar_clave(contraseña)
    fernet = Fernet(clave)
    return fernet.encrypt(texto.encode())

# Función principal para interactuar con el usuario
def main():
    print("=== Encriptador ===")
    
    # Solicitar al usuario la contraseña y el texto
    contraseña = input("Introduce una contraseña (puede ser cualquier texto): ")
    texto = input("Introduce el texto que deseas cifrar: ")
    
    # Cifrar el texto
    texto_cifrado = cifrar_texto(texto, contraseña)
    print(f"Texto cifrado: {texto_cifrado.decode()}")

if __name__ == "__main__":
    main()
