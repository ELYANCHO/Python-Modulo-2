def verificador_contrasena():
    """
    Esta función verifica si la palabra cumple con las condiciones para ser una contraseña.
    Verifica si dentro de la contraseña hay una letra mayuscula, un número y si tiene 8 caracteres.

    """
    print(" Validador de Contraseñas")
    while True:
        contrasena = input("\nCree una contraseña: ").strip()

        if len(contrasena) < 8:
            print(" La contraseña debe tener al menos 8 caracteres.")
            continue

        if not any(c.isupper() for c in contrasena):
            print(" La contraseña debe contener al menos una letra mayúscula.")
            continue

        if not any(c.isdigit() for c in contrasena):
            print(" La contraseña debe contener al menos un número.")
            continue

        print(" Contraseña válida. Registro exitoso.")
        break

def main():
    verificador_contrasena()

if __name__ == "__main__":
    main()
