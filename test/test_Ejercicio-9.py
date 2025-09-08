import Ejercicio_9
from Ejercicio_9 import productosiva


def test_diccionario_con_iva(capsys):
    # Ejecutamos la función
    productosiva()

    # Capturamos la salida impresa
    salida = capsys.readouterr().out.strip()

    # Diccionario esperado
    esperado = {"Camisa": 59500.0, "Pantalón": 95200.0}

    # Convertimos salida (string) a dict evaluándolo con eval
    salida_dict = eval(salida)

    # Comparamos que los diccionarios sean iguales
    assert salida_dict == esperado
