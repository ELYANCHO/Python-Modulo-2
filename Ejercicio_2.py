def consola():
    """
    Esta función simula el menu de una consola

   :returns:
    case 1: Imprime "Guardando..."
    case 2: Imprime "Cargando..."
    case 3: Imprime "Saliendo..." y termina el bucle.
    case _: Imprime "Opción no válida, intente de nuevo."
    """

    while True:
        print(f"¿Qué le gustaría hacer?\n 1.Guardar \n 2.Cargar \n 3.Salir")
        opcion=int(input("Ingrese una opción (1, 2, 3): "))
        match opcion:
            case 1:
                print("Guardando...")

            case 2:
                print("Cargando...")

            case 3:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intente de nuevo.")

def main (value=None):
    consola()
if __name__ == "__main__":
    consola()