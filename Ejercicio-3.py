def verifiricador_contrasena():
    """
        Esta función verifica si la palabra cumple con las condiciones para ser una contraseña.
        Verifica si dentro de la contraseña hay una letra mayuscula, un número y si tiene 8 caracteres.

       :returns:

        """
    while True:

        contrasena = input("Ingrese su contraseña: ")
        if len(contrasena) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
        elif not any(l.isdigit() for l in contrasena):
            print("La contraseña debe tener almenos un número")
        elif not any(l.isupper() for l in contrasena):
            print("La contraseña debe tener almenos una Mayuscula")
        else:
            print("Contraseña guardada")
            break


def main (value=None):
    print(verifiricador_contrasena())
if __name__ == "__main__":
    main()