def filtrado():
    """
        Esta función toma una lista inicial para crear tres listas nuevas.

        Returns:
            str: La frase válida ingresada por el usuario.
        """

    numeros = [-5, 10, -15, 20, -25, 30]

    # Lista de numeros positivos
    positivo = [n for n in numeros if n > 0]

    # Lista con los cuadrados de todos los números.
    cuadrados = [n ** 2 for n in numeros]

    # Lista de strings que diga "positivo" o "negativo" para cada número, usando un ternario dentro de la comprensión.
    signos = ["positivo" if n >= 0 else "negativo" for n in numeros]

    print(f"La lista de numeros positivos es: {positivo}")
    print(f"La lista con los cuadrados de todos los números: {cuadrados}")
    print(f"La lista de positivos y negativos es: {signos}")

def main():
    filtrado()
if __name__ == "__main__":
    main()
