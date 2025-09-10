def procesar_accion(accion, estado_actual):
    """
    Procesa una acción del jugador y actualiza el estado del juego.

    Args:
        accion (str): La acción que el jugador quiere realizar.
        estado_actual (dict): El estado actual del juego.

    Returns:
        tuple: Un nuevo estado del juego y un mensaje para el jugador.
    """
    habitacion = estado_actual['habitacion']
    tiene_llave = estado_actual['tiene_llave']
    mensaje = ""
    juego_activo = True

    # HABITACIÓN INICIAL
    if habitacion == "inicio":
        if accion == "ir al norte":
            habitacion = "tesoro"
            mensaje = "\nEntras en una habitación con un gran cofre en el centro."
        elif accion == "ir al este":
            habitacion = "trampa"
            mensaje = "\n¡Oh no! Has caído en una trampa llena de pinchos.  GAME OVER."
            juego_activo = False
        else:
            mensaje = "No entiendo esa acción. Intenta: 'ir al norte' o 'ir al este'."

    # HABITACIÓN DEL TESORO
    elif habitacion == "tesoro":
        if accion == "abrir cofre":
            if not tiene_llave:
                mensaje = "El cofre está cerrado con llave. Necesitas encontrarla."
            else:
                mensaje = "¡Abres el cofre y encuentras un tesoro brillante!  GANASTE "
                juego_activo = False
        elif accion == "ir al sur":
            habitacion = "inicio"
            mensaje = "\nRegresas a la primera habitación."
        elif accion == "ir al oeste":
            habitacion = "llave"
            mensaje = "\nEncuentras una pequeña habitación con una llave en el suelo."
        else:
            mensaje = "Acción no válida. Intenta: 'abrir cofre', 'ir al sur' o 'ir al oeste'."

    # HABITACIÓN DE LA LLAVE
    elif habitacion == "llave":
        if accion == "tomar llave":
            if not tiene_llave:
                tiene_llave = True
                mensaje = "Has recogido la llave. "
            else:
                mensaje = "Ya tienes la llave."
        elif accion == "ir al este":
            habitacion = "tesoro"
            mensaje = "\nRegresas a la habitación del cofre."
        else:
            mensaje = "Acción no válida. Intenta: 'tomar llave' o 'ir al este'."

    return {'habitacion': habitacion, 'tiene_llave': tiene_llave}, mensaje, juego_activo


def jugar_partida():
    """
    Esta función maneja el bucle principal del juego y la interacción con el usuario.
    """
    print("Bienvenido a la Aventura del Castillo Misterioso ")
    print("Estás en una habitación oscura con dos puertas: una al norte y otra al este.\n")

    estado_juego = {
        'habitacion': "inicio",
        'tiene_llave': False
    }
    juego_activo = True

    while juego_activo:
        accion = input("¿Qué quieres hacer? ").lower()

        estado_juego, mensaje, juego_activo = procesar_accion(accion, estado_juego)
        print(mensaje)

    print("\nGracias por jugar. ")


if __name__ == "__main__":
    jugar_partida()