import pytest
import random
from Ejercicio_4 import ppt


def test_input_vacio(monkeypatch, capsys):
    entradas = iter(["", "piedra", "piedra", "piedra", "piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")  # pc siempre tijeras

    ppt()
    salida = capsys.readouterr().out
    assert "No puede dejar la opción vacía." in salida
    assert "¡Felicidades, ganaste el juego!" in salida


def test_input_con_numero(monkeypatch, capsys):
    entradas = iter(["123", "piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")  # jugador gana

    ppt()
    salida = capsys.readouterr().out
    assert "No se permiten números" in salida
    assert "¡Felicidades, ganaste el juego!" in salida


def test_input_con_caracter_especial(monkeypatch, capsys):
    entradas = iter(["@@@", "piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")

    ppt()
    salida = capsys.readouterr().out
    assert "No se permiten caracteres especiales" in salida
    assert "¡Felicidades, ganaste el juego!" in salida


def test_input_invalido(monkeypatch, capsys):
    entradas = iter(["lagarto", "piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")

    ppt()
    salida = capsys.readouterr().out
    assert "'lagarto' no es válido" in salida
    assert "¡Felicidades, ganaste el juego!" in salida


def test_flujo_completo_gana_jugador(monkeypatch, capsys):
    entradas = iter(["piedra", "papel", "tijeras", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")  # siempre tijeras

    ppt()
    salida = capsys.readouterr().out
    assert "¡Ganaste esta ronda!" in salida
    assert "¡Felicidades, ganaste el juego!" in salida


def test_flujo_completo_gana_pc(monkeypatch, capsys):
    entradas = iter(["piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    monkeypatch.setattr(random, "choice", lambda _: "papel")  # pc siempre papel

    ppt()
    salida = capsys.readouterr().out
    assert "La computadora gana esta ronda." in salida
    assert "La computadora ganó el juego" in salida


def test_empate(monkeypatch, capsys):
    entradas = iter(["piedra", "papel", "tijeras", "piedra", "piedra", "piedra"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugadas_pc = iter(["piedra", "papel", "tijeras", "tijeras", "tijeras", "tijeras"])
    monkeypatch.setattr(random, "choice", lambda _: next(jugadas_pc))

    ppt()
    salida = capsys.readouterr().out

    assert "Empate." in salida
    assert "¡Felicidades, ganaste el juego!" in salida
