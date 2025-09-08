import pytest
from Ejercicio_6 import encontrar_indices, validacion_frase, validacion_letra, main



def test_encontrar_indices_coincidencias():
    assert encontrar_indices("Hola SENA", "a") == [3, 8]

def test_encontrar_indices_sin_coincidencias():
    assert encontrar_indices("Hola", "z") == []

def test_encontrar_indices_case_insensitive():
    assert encontrar_indices("Hola", "h") == [0]
    assert encontrar_indices("Hola", "H") == [0]




def test_validacion_frase_vacia(monkeypatch, capsys):
    entradas = iter(["", "Hola Mundo"])  # primero vacío (inválido), luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validacion_frase("Ingrese una frase: ")
    salida = capsys.readouterr().out

    assert resultado == "Hola Mundo"
    assert "No puede dejar la respuesta vacía." in salida


def test_validacion_frase_caracter_invalido(monkeypatch, capsys):
    entradas = iter(["Hola123", "Hola"])  # primero inválido, luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validacion_frase("Ingrese una frase: ")
    salida = capsys.readouterr().out

    assert resultado == "Hola"
    assert "Solo se permiten letras y espacios." in salida


def test_validacion_letra_invalida(monkeypatch, capsys):
    entradas = iter(["12", "@", "o"])  # varios intentos inválidos y luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    resultado = validacion_letra("Ingrese una letra: ")
    salida = capsys.readouterr().out

    assert resultado == "o"
    assert "Debe ingresar solo una letra válida." in salida




def test_main_letra_aparece(monkeypatch, capsys):
    entradas = iter(["Hola Mundo", "o"])  # frase válida y letra que sí aparece
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main()
    salida = capsys.readouterr().out

    assert "La letra 'o' aparece en las posiciones:" in salida


def test_main_letra_no_aparece(monkeypatch, capsys):
    entradas = iter(["Hola Mundo", "z"])  # frase válida y letra que NO aparece
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main()
    salida = capsys.readouterr().out

    assert "La letra 'z' no aparece en la frase." in salida
