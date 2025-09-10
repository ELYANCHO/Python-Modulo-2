import pytest
from Ejercicio_14 import (
    elegir_palabra,
    mostrar_tablero,
    validar_entrada,
    jugar,
    AHORCADO,
    PALABRAS
)
from io import StringIO
from unittest.mock import patch
import random

def test_elegir_palabra():
    """
    Verifica que la función elegir_palabra seleccione una de las palabras de la lista.
    """
    palabra = elegir_palabra()
    assert palabra in PALABRAS

def test_validar_entrada_correcta():
    """
    Verifica que una entrada de una sola letra válida sea True.
    """
    assert validar_entrada('a', set(), set()) is True

def test_validar_entrada_mas_de_una_letra():
    """
    Verifica que una entrada con más de una letra sea inválida.
    """
    with patch('builtins.print') as mock_print:
        assert validar_entrada('ab', set(), set()) is False
        mock_print.assert_called_with(" Ingresa solo una letra válida.")

def test_validar_entrada_caracter_no_alfabetico():
    """
    Verifica que una entrada no alfabética sea inválida.
    """
    with patch('builtins.print') as mock_print:
        assert validar_entrada('1', set(), set()) is False
        mock_print.assert_called_with(" Ingresa solo una letra válida.")

def test_validar_entrada_letra_ya_intentada():
    """
    Verifica que una letra ya intentada sea inválida.
    """
    with patch('builtins.print') as mock_print:
        assert validar_entrada('p', {'p'}, set()) is False
        mock_print.assert_called_with(" Ya intentaste esa letra.")
        assert validar_entrada('q', set(), {'q'}) is False
        mock_print.assert_called_with(" Ya intentaste esa letra.")

def test_mostrar_tablero(capsys):
    """
    Verifica que el tablero se imprima correctamente.
    """
    mostrar_tablero("python", {'p', 'o'}, {'e', 'a'}, 5)
    captured = capsys.readouterr()
    salida = captured.out

    assert AHORCADO[5] in salida
    assert "P y t h o n" not in salida  # Los espacios son un detalle
    assert "_ _ _ _ _ _" not in salida
    assert "p _ _ h o n" in salida or "p _ _ _ o _" in salida
    assert "Letras incorrectas: e a" in salida or "Letras incorrectas: a e" in salida
    assert "Vidas restantes: 5" in salida

# Tests para el flujo de juego con monkeypatch
def test_victoria_del_jugador(monkeypatch, capsys):
    """
    Simula un juego completo donde el jugador gana.
    """
    # Se simula la elección de una palabra conocida para el test
    monkeypatch.setattr(random, 'choice', lambda _: "python")
    # Se simulan las entradas del usuario para adivinar la palabra
    entradas = iter(['p', 'y', 't', 'h', 'o', 'n'])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))

    jugar()
    captura = capsys.readouterr()
    salida = captura.out

    assert "¡Felicidades! Adivinaste la palabra." in salida
    assert "Te quedaste sin vidas" not in salida
    assert "Palabra: p y t h o n" in salida


def test_derrota_del_jugador(monkeypatch, capsys):
    """
    Simula un juego completo donde el jugador pierde.
    """
    monkeypatch.setattr(random, 'choice', lambda _: "ahorcado")
    # Simula 6 letras incorrectas para agotar las 6 vidas
    entradas = iter(['x', 'y', 'z', 'w', 'q', 'j'])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))

    jugar()
    captura = capsys.readouterr()
    salida = captura.out

    assert "Te quedaste sin vidas. La palabra era: ahorcado" in salida
    assert "¡Felicidades! Adivinaste la palabra." not in salida
    assert AHORCADO[0] in salida