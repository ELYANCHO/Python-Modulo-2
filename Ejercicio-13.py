def aventura():
    """
    Este es un juego de aventura basado en texto donde el jugador navega por habitaciones y toma decisiones.
    El juego comienza en una habitación y puede tomar decisiones ('ir al norte', 'abrir cofre'):

    Args:
        None
    Returns:
        None
    """
    print("""
                   |>>>                    |>>>
                   |                        |
               _  _|_  _                _  _|_  _
              | |_| |_| |              | |_| |_| |
              \  .      /              \  .      /
               |:  .    |                |:  .    |
              /|:.  .  /|              /|:.  .  /|
             /_|___ ._/ |            /_|___ ._/ |
            |           |          |           |
            |  []   []  |          |  []   []  |
         __ |     .--.  | __    __ |     .--.  | __
        |  ||    (    ) ||  |  |  ||    (    ) ||  |
     ___|__||____'--'___||__|__|__||____'--'___||__|___
    /_______________________________________________
    """)
    print("------------------------------------------------ ")
    print("Bienvenido a la Aventura del Castillo Misterioso ")
    print("------------------------------------------------ ")
    print("Estás en una habitación oscura con dos puertas:\n"
          "Una lo dirige al norte y otra hacia este"
          "\n-> Escriba lo siguiente para dirigirse al lugar\n"
          "1.ir al norte\n"
          "2.ir al este.\n")
    print("""
                 NORTE                     ESTE
                <<<|                        |>>>
                   |                        |
               _  _|_  _                _  _|_  _ 
    /_______________________________________________\\
    """)

    habitacion = "inicio"
    tiene_llave = False
    juego_activo = True

    while juego_activo:
        accion = input("¿Qué quieres hacer? ").lower()

        # HABITACIÓN INICIAL
        if habitacion == "inicio":
            if accion == "ir al norte":
                habitacion = "tesoro"
                print("\nEntras en una habitación con un gran cofre en el centro.")
                print(r"""
                      _________________________
                     /                        /|
                    /________________________/ |
                   |                        |  |
                   |  ____    _______       |  |
                   | |####|  |#######|      |  |
                   | |####|  |#######|      |  |
                   | |####|  |#######|      |  |
                   | |____|  |_______|      |  |
                   |                        |  |
                   |      === TESORO ===    |  |
                   |________________________| /
                   |________________________|/
                """)
                print(
                      "-> Escriba la acción que quiere realizar:\n"
                      "1.ir al sur\n"
                      "2.ir al oeste.\n"
                      "3.abrir cofre")

            elif accion == "ir al este":
                habitacion = "trampa"
                print("\n¡Oh no! Has caído en una trampa llena de pinchos.")
                print(r"""
                        ________________________
                       |                        |
                       |      ¡GAME OVER!       |
                       |   Trampa con pinchos   |
                       |________________________|

                       ||||||||||||||||||||||||
                       |\/\/\/\/\/\/\/\/\/\/\|
                       |/\/\/\ (x_x) /\/\/\|
                       |\/\/\/\ /|\  /\/\/\/|
                       |/\/\/\  / \  \/\/\/\/|
                       ||||||||||||||||||||||||
                """)
                juego_activo = False
            else:
                print("No entiendo esa acción. Intenta: 'ir al norte' o 'ir al este'.")

        # HABITACIÓN DEL TESORO

        elif habitacion == "tesoro":

            if accion == "abrir cofre":
                if not tiene_llave:
                    print("-------------------------------------------------------")
                    print("El cofre está cerrado con llave. Necesitas encontrarla.")
                    print("-------------------------------------------------------")
                    print("-> Escriba la acción que quiere realizar:\n"
                          "1.ir al sur\n"
                          "2.ir al oeste.\n"
                          "3.abrir cofre")
                else:
                    print("-----------------------------------------------------------")
                    print("¡Abres el cofre y encuentras un tesoro brillante!  GANASTE ")
                    print("-----------------------------------------------------------")
                    juego_activo = False
            elif accion == "ir al sur":
                habitacion = "inicio"
                print("\nRegresas a la primera habitación.")
            elif accion == "ir al oeste":
                habitacion = "llave"
                print("--------------------------------------------------------------")
                print("Encuentras una pequeña habitación con una llave en el suelo.")
                print("--------------------------------------------------------------")
                print("-> Escriba la acción que quiere realizar:\n"
                      "1.ir al este\n"
                      "2.tomar llave.\n")
            else:
                print("Acción no válida. Intenta: 'abrir cofre', 'ir al sur' o 'ir al oeste'.")

        # HABITACIÓN DE LA LLAVE
        elif habitacion == "llave":
            if accion == "tomar llave":
                if not tiene_llave:
                    tiene_llave = True
                    print(r"""
                                     __
                                    /o \____
                                    \__/-="="
                                      ||
                                      ||
                                      ||
                                      ||
                                    __||__
                                   |______|
                                    """)
                    print("-----------------------")
                    print("Has recogido la llave. ")
                    print("-----------------------")
                    print("-> Escriba la acción que quiere realizar:\n"
                          "1.ir al este")

                else:
                    print("Ya tienes la llave.")
            elif accion == "ir al este":
                habitacion = "tesoro"
                print("\nRegresas a la habitación del cofre.")
                print("-> Escriba la acción que quiere realizar:\n"
                      "1.abrir cofre\n")
            else:
                print("Acción no válida. Intenta: 'tomar llave' o 'ir al este'.")
    print("\nGracias por jugar. ")

def main():
    aventura()
if __name__ == "__main__":
    main()
