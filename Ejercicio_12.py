import random
def simulador_dados(intentos=10000):
    """
    Esta función simula el lanzamiento de dos dados un número determinado de veces.
    Cuenta la frecuencia de cada posible suma (de 2 a 12) usando un diccionario.

    Args:
        intentos (int): número de veces que se lanzarán los dados
    Returns:
        dict: diccionario con la frecuencia de cada suma
    """
    frecuencias = {}

    for _ in range(intentos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # Usamos get() para sumar frecuencias
        frecuencias[suma] = frecuencias.get(suma, 0) + 1
    return frecuencias

def main():
    intentos = 10000
    resultados = simulador_dados(intentos)
    print(f"Resultados después de {intentos} lanzamientos:\n")
    for suma in range(2, 13):  # posibles resultados 2 - 12
        print(f"Suma {suma}: {resultados.get(suma, 0)} veces")
if __name__ == "__main__":
    main()
