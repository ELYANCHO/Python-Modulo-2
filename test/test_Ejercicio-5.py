import pytest
from Ejercicio_5 import poi


def test_numero_par_no_multiplo(monkeypatch, capsys):
    entradas = iter(["8"])  # par pero no múltiplo de 5
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    poi()
    salida = capsys.readouterr().out

    assert "El número 8 es Par." in salida
    assert "múltiplo de 5" not in salida


def test_numero_impar_no_multiplo(monkeypatch, capsys):
    entradas = iter(["7"])  # impar pero no múltiplo de 5
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    poi()
    salida = capsys.readouterr().out

    assert "El número 7 es Impar." in salida
    assert "múltiplo de 5" not in salida


def test_numero_par_multiplo(monkeypatch, capsys):
    entradas = iter(["10"])  # par y múltiplo de 5
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    poi()
    salida = capsys.readouterr().out

    assert "El número 10 es Par." in salida
    assert "Además, es múltiplo de 5." in salida


def test_numero_impar_multiplo(monkeypatch, capsys):
    entradas = iter(["15"])  # impar y múltiplo de 5
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    poi()
    salida = capsys.readouterr().out

    assert "El número 15 es Impar." in salida
    assert "Además, es múltiplo de 5." in salida


def test_input_invalido(monkeypatch, capsys):
    entradas = iter(["abc"])  # entrada inválida
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    poi()
    salida = capsys.readouterr().out

    assert "Debe ingresar un número válido." in salida
