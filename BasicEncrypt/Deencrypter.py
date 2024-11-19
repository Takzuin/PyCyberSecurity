from cryptography.fernet import Fernet
import hashlib
import base64

# Función para generar clave a partir de una contraseña
def generar_clave(contraseña):
    # Usar SHA-256 para derivar la clave
    hash_entrada = hashlib.sha256(contraseña.encode()).digest()  # Convertir contraseña a hash de 32 bytes
    clave_base64 = base64.urlsafe_b64encode(hash_entrada)  # Convertir a base64
    return clave_base64

# Función para descifrar el texto
def descifrar_texto(texto_cifrado, contraseña):
    clave = generar_clave(contraseña)
    crypt_pass = Fernet(clave)
    return crypt_pass.decrypt(texto_cifrado).decode()

# Función principal para interactuar con el usuario
def main():
    print("=== Desencriptador ===")
    
    # Solicitar al usuario la contraseña y el texto cifrado
    contraseña = input("Introduce la contraseña para descifrar: ")
    texto_cifrado = input("Introduce el texto cifrado: ").encode()  # Convertir a bytes
    
    # Descifrar el texto
    texto_descifrado = descifrar_texto(texto_cifrado, contraseña)
    print(f"Texto descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
