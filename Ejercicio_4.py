import random

def ppt():
    """
        Esta función simula el juego de piedra, papel tijera.

       :returns:
    """
    cc = 0
    cu = 0

    while cc < 3 and cu < 3:
        palabra_usuario = str(input("Escriba la palabra de su elección:\n"
                                "1. Piedra\n"
                                "2. Papel\n"
                                "3. Tijera\n").lower())
        palabras = ["piedra", "papel", "tijera"]
        palabra_aleatoria = random.choice(palabras)

        if palabra_aleatoria == palabra_usuario:
            print("Empate por palabra")
        elif (palabra_usuario == 'piedra' and palabra_aleatoria == 'tijeras') or \
                (palabra_usuario == 'papel' and palabra_aleatoria == 'piedra') or \
                (palabra_usuario == 'tijera' and palabra_aleatoria == 'papel'):
            print("Gana Usuario")
            cu += 1
        else:
            print("Gana Maquina")
            cc += 1
        print(f"Puntaje: Maquina {cc}, Humano {cu}")


def main (value=None):
    ppt()

if __name__ == "__main__":
    main()