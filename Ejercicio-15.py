import random

# Tamaño del tablero
N = 5


def crear_tablero():
    """Crea un tablero vacío de 5x5"""
    return [["~" for _ in range(N)] for _ in range(N)]


def colocar_barco():
    """
    Esta función coloca un barco de 3 casillas horizontal o vertical.

    Args:
        None
    Returns:
        list: lista de coordenadas de los puntos de disparo
    """
    """Coloca un barco de 3 casillas horizontal o vertical"""
    orientacion = random.choice(["H", "V"])
    if orientacion == "H":  # Horizontal
        fila = random.randint(0, N - 1)
        col = random.randint(0, N - 3)
        return [(fila, col + i) for i in range(3)]
    else:  # Vertical
        fila = random.randint(0, N - 3)
        col = random.randint(0, N - 1)
        return [(fila + i, col) for i in range(3)]


def imprimir_tablero(tablero):
    """
    Esta función muestra el tablero con coordenadas.

    Args:
        tablero (list): lista de listas que representa el tablero
    Returns:
        None
    """
    """Muestra el tablero con coordenadas"""
    print("   " + " ".join(str(i + 1) for i in range(N)))
    for i, fila in enumerate(tablero):
        print(chr(65 + i) + "  " + " ".join(fila))


def convertir_coordenada(coordenada):
    """
    Esta función convierte entrada tipo 'A3' en índices (fila, columna).

    Args:
        coordenada (str): entrada del usuario
    Returns:
        list: lista de dos índices (fila, columna)
    """
    """Convierte entrada tipo 'A3' en índices (fila, columna)"""
    try:
        fila = ord(coordenada[0].upper()) - 65
        col = int(coordenada[1]) - 1
        if 0 <= fila < N and 0 <= col < N:
            return fila, col
    except:
        return None
    return None


def jugar():
    """
    Este programa juega al juego de batalla naval.

    Args:
        None
    Returns:
        None
    """
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 10
    aciertos = 0

    print(" Bienvenido a Batalla Naval (5x5)")
    print("Tienes 10 turnos para hundir un barco de 3 casillas.")
    imprimir_tablero(tablero)

    while intentos > 0 and aciertos < 3:
        disparo = input("\nIngresa coordenada (ej: A3): ").strip().upper()
        pos = convertir_coordenada(disparo)

        if not pos:
            print(" Entrada inválida. Usa formato LetraNúmero (ej: B2).")
            continue

        fila, col = pos
        if tablero[fila][col] != "~":
            print(" Ya disparaste aquí.")
            continue

        if pos in barco:
            tablero[fila][col] = "X"
            aciertos += 1
            print(" ¡Tocado!")
        else:
            tablero[fila][col] = "O"
            print(" Agua.")

        intentos -= 1
        print(f"Turnos restantes: {intentos}")
        imprimir_tablero(tablero)

    # Resultado final
    if aciertos == 3:
        print("\n ¡Felicidades! Hundiste el barco.")
    else:
        print("\n💀 Te quedaste sin turnos. El barco estaba en:")
        print([f"{chr(65 + f)}{c + 1}" for f, c in barco])


def main():
    jugar()
if __name__ == "__main__":
    main()
