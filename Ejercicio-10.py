def transpuesta_comprehension(matriz):
    """
            Esta funcion recibe una matriz y devuelve su transpuesta.

            :arg matriz: Matriz.

           :returns: Transpuesta.
    """
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]


def main():
    m = [[1, 2, 3], [4, 5, 6]]
    print("Matriz original:", m)
    print("Transpuesta (con comprensión de listas):", transpuesta_comprehension(m))

if __name__ == "__main__":
    main()