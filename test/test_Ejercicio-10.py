import Ejercicio_10  # cámbialo por el nombre real de tu archivo

def test_transpuesta_bucles():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert Ejercicio_10 .transpuesta(matriz) == esperado

def test_transpuesta_comprehension():
    matriz = [[7, 8], [9, 10], [11, 12]]
    esperado = [[7, 9, 11], [8, 10, 12]]
    assert Ejercicio_10 .transpuesta_comprehension(matriz) == esperado

def test_transpuesta_un_elemento():
    matriz = [[42]]
    esperado = [[42]]
    assert Ejercicio_10 .transpuesta(matriz) == esperado
    assert Ejercicio_10 .transpuesta_comprehension(matriz) == esperado
