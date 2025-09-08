import random

def ppt():
    """
        Esta función simula el juego de piedra, papel tijera.

        :returns:
    """

    print(" Juego: Piedra, Papel o Tijeras")


    opciones = ["piedra", "papel", "tijeras"]
    victorias_jugador = 0
    victorias_pc = 0

    while victorias_jugador < 3 and victorias_pc < 3:
        jugador = input("\nElige (piedra, papel, tijeras): ").strip().lower()

        if not jugador:
            print("No puede dejar la opción vacía.")
            continue

        if any(c.isdigit() for c in jugador):
            print("No se permiten números, solo texto.")
            continue

        if not jugador.isalpha():
            print(" No se permiten caracteres especiales, solo letras.")
            continue

        if jugador not in opciones:
            print(f" '{jugador}' no es válido. Escriba piedra, papel o tijeras.")
            continue

        # Jugada de la computadora
        pc = random.choice(opciones)
        print(f" La computadora eligió: {pc}")

        # Determinar ganador
        if jugador == pc:
            print(" Empate.")
        elif (jugador == "piedra" and pc == "tijeras") or \
            (jugador == "tijeras" and pc == "papel") or \
            (jugador == "papel" and pc == "piedra"):
            print(" ¡Ganaste esta ronda!")
            victorias_jugador += 1
        else:
            print(" La computadora gana esta ronda.")
            victorias_pc += 1

        print(f" Marcador: Tú {victorias_jugador} - {victorias_pc} PC")

    # Resultado final
    if victorias_jugador == 3:
        print("\n ¡Felicidades, ganaste el juego!")
    else:
        print("\n La computadora ganó el juego. ¡Suerte la próxima!")


def main():
    ppt()

if __name__ == "__main__":
    main()
