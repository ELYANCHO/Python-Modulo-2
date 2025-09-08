def comando():
    """
    Esta función simula el menu de una consola

    :returns:
    case 1: Imprime "Guardando..."
    case 2: Imprime "Cargando..."
    case 3: Imprime "Saliendo..." y termina el bucle.
    case _: Imprime "Opción no válida, intente de nuevo."
    """

    print("Bienvenido al sistema  de comandos")


    while True:
        comando = input("\nIngrese un comando (guardar, cargar, salir): ").strip().lower()
        if not comando:
            print(" No puede dejar el campo vacío.")
            continue

        match comando:
            case "guardar":
                print("Guardando  archivo...")
            case "cargar":
                print("Cargando archivo...")
            case "salir":
                print("Saliendo del programa...")
                break
            case _:  # Default
                print(f" Comando inválido: '{comando}'. Intente nuevamente.")

    print(" Programa finalizado.")


def main():
    comando()


if __name__ == "__main__":
    main()
