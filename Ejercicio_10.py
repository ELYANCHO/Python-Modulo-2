def transpuesta(matriz):
    """
    Esta función recibe una matriz y devuelve su transpuesta.
    La transpuesta se logra intercambiando filas por columnas.

    Args:
        matriz (list): lista de listas que representa la matriz
    Returns:
        list: lista de listas que representa la matriz transpuesta
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for j in range(columnas):  # recorro columnas
        nueva_fila = []
        for i in range(filas):  # recorro filas
            nueva_fila.append(matriz[i][j])
        resultado.append(nueva_fila)

    return resultado


def transpuesta_comprehension(matriz):
    """Transpuesta usando list comprehension anidada"""
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

