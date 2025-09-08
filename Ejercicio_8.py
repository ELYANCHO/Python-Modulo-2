def filtrado():
    """
        Esta función toma una lista inicial para crear tres listas nuevas.

        Returns:
            str: La frase válida ingresada por el usuario.
        """

    numeros = [-5, 10, -15, 20, -25, 30]
    positivo = [n for n in numeros if n > 0]

    cuadrados = [n ** 2 for n in numeros]

    signos = ["positivo" if n >= 0 else "negativo" for n in numeros]
    print(f"La lista de numeros positivos es: {positivo}")
    print(f"La lista con los cuadrados de todos los números: {cuadrados}")
    print(f"La lista de positivos y negativos es: {signos}")

def main():
    filtrado()
if __name__ == "__main__":
    main()
