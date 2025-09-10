def validar_cedula(cedula: str) -> bool:
    """
    Valida un número de cédula basado en la regla:
    La suma de sus dígitos debe ser un número par.

    Args:
        cedula (str): Número de cédula como string.

    Returns:
        bool: True si es válido, False en caso contrario.
    """
    if not cedula.isdigit():
        print("Error: La cédula debe contener solo números.")
        return False

    if len(cedula) != 10:
        print("Error: la cédula debe tener exactamente 10 dígitos.")
        return False

    suma = sum(int(digito) for digito in cedula)

    if suma % 2 == 0:
        return True
    else:
        print("Cédula inválida: la suma de los dígitos no es par.")
        return False
