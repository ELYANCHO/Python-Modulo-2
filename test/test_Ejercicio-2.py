import builtins
import pytest
from Ejercicio_2 import comando  # 👈 importa tu programa (asegúrate que el archivo se llame igual)


def test_comando_salir(monkeypatch, capsys):
    """
    Verifica que al escribir 'salir' el programa termine.
    """
    entradas = iter(["salir"])
    monkeypatch.setattr(builtins, "input", lambda _: next(entradas))

    comando()
    salida = capsys.readouterr().out

    assert "Saliendo del programa..." in salida
    assert "Programa finalizado." in salida


def test_comando_guardar(monkeypatch, capsys):
    """
    Verifica que el comando 'guardar' imprima el mensaje correcto.
    """
    entradas = iter(["guardar", "salir"])
    monkeypatch.setattr(builtins, "input", lambda _: next(entradas))

    comando()
    salida = capsys.readouterr().out

    assert "Guardando  archivo..." in salida
    assert "Saliendo del programa..." in salida


def test_comando_cargar(monkeypatch, capsys):
    """
    Verifica que el comando 'cargar' imprima el mensaje correcto.
    """
    entradas = iter(["cargar", "salir"])
    monkeypatch.setattr(builtins, "input", lambda _: next(entradas))

    comando()
    salida = capsys.readouterr().out

    assert "Cargando archivo..." in salida or " Cargando archivo..." in salida  # tolera el espacio extra
    assert "Saliendo del programa..." in salida


def test_comando_invalido(monkeypatch, capsys):
    """
    Verifica que un comando inválido imprima el mensaje de error.
    """
    entradas = iter(["invalido", "salir"])
    monkeypatch.setattr(builtins, "input", lambda _: next(entradas))

    comando()
    salida = capsys.readouterr().out

    assert "Comando inválido: 'invalido'" in salida
    assert "Saliendo del programa..." in salida


def test_comando_flujo_completo(monkeypatch, capsys):
    """
    Simula un flujo completo con varios comandos válidos e inválidos.
    """
    entradas = iter(["guardar", "cargar", "invalido", "salir"])
    monkeypatch.setattr(builtins, "input", lambda _: next(entradas))

    comando()
    salida = capsys.readouterr().out

    assert "Guardando  archivo..." in salida
    assert "Cargando archivo..." in salida or " Cargando archivo..." in salida
    assert "Comando inválido: 'invalido'" in salida
    assert "Saliendo del programa..." in salida
    assert "Programa finalizado." in salida
