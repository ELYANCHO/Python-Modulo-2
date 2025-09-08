def poi(numero_usuario):
    """
        Esta función toma el número digitado por el usuario y le da un valor dependiendo si el número es par o impar

        :arg
        numero_usuario (int): Número de usuario

        :returns:
        respuesta (bool): Respuesta si el número del usuario es par o impar
    """
    resultado = "Par" if numero_usuario % 2 == 0 else "Impar"
    respuesta = f"El número {numero_usuario} es {resultado}"
    if numero_usuario % 5 == 0:
        print("El número es múltiplo de 5")
    return respuesta

def main (value=None):
    numero_usuario = int(input("Introduce un numero: "))
    print(poi(numero_usuario))
if __name__ == "__main__":
    main()

