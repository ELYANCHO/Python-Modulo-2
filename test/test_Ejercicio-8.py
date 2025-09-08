from Ejercicio_8 import filtrado

def test_list_comprehensions(capsys):
    # Ejecutamos la función principal
    filtrado()

    # Capturamos lo que imprime en consola
    salida = capsys.readouterr().out

    # Valores esperados
    esperado_positivos = [10, 20, 30]
    esperado_cuadrados = [25, 100, 225, 400, 625, 900]
    esperado_signos = ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]

    # Comprobamos que las listas correctas estén en la salida
    assert f"La lista de numeros positivos es: {esperado_positivos}" in salida
    assert f"La lista con los cuadrados de todos los números: {esperado_cuadrados}" in salida
    assert f"La lista de positivos y negativos es: {esperado_signos}" in salida
