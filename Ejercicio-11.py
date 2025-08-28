def validar_cedula(cedula):
    """
        Esta función valida un número de cédula basado en la regla de que la suma de sus dígitos debe ser un número par.

        Args:
            cedula (str): El número de cédula a validar.
        Returns:
            bool: True si la cédula es válida (suma de dígitos es
                    par), False en caso contrario.

        """
    if not cedula.isdigit():
        print("Error: La cédula debe contener solo números.")
        return False
    suma = 0
    for digito in cedula:
        suma += int(digito)
    if suma < 10:
        print("la cedula debe tener 10 numeros")
        return False

    if suma % 2 == 0:
        return True
    else:
        print(" Cédula inválida: la suma de los dígitos no es par.")
        return False

while True:
    cedula_usuario = input("Ingrese su cédula: ")
    if validar_cedula(cedula_usuario):
        print("Cédula válida")
        break

def main():
    validar_cedula(cedula_usuario)
if __name__ == "__main__":
    main()