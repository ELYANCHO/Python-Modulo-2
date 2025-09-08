def poi():
    """
    Esta función toma el número digitado por el usuario y le da un valor dependiendo si el número es par o impar

    :arg
    numero_usuario (int): Número de usuario

    :returns:
    respuesta (bool): Respuesta si el número del usuario es par o impar
    """
    try:
        numero = int(input("Ingrese un número: "))

        # Usando operador ternario
        tipo = "Par" if numero % 2 == 0 else "Impar"
        print(f"El número {numero} es {tipo}.")

        # Mensaje extra si es múltiplo de 5
        if numero % 5 == 0:
            print("Además, es múltiplo de 5.")
    except ValueError:
        print(" Debe ingresar un número válido.")

def main():
    poi()
if __name__ == "__main__":
    main()
