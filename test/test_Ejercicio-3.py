import builtins
import pytest
from Ejercicio_3 import verificador_contrasena

def test_contrasena_valida(monkeypatch, capsys):
    """
    Caso válido: la contraseña cumple todos los requisitos (>=8, mayúscula, número).
    """
    inputs = iter(["Abcdefg1"])  # Contraseña correcta a la primera
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    verificador_contrasena()
    salida = capsys.readouterr().out

    assert "Contraseña válida. Registro exitoso." in salida


def test_contrasena_muy_corta(monkeypatch, capsys):
    """
    Caso inválido: primero una contraseña corta, luego una correcta.
    """
    inputs = iter(["abc", "Abcdefg1"])  # 1° incorrecta, 2° correcta
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    verificador_contrasena()
    salida = capsys.readouterr().out

    assert "La contraseña debe tener al menos 8 caracteres." in salida
    assert "Contraseña válida. Registro exitoso." in salida


def test_contrasena_sin_mayuscula(monkeypatch, capsys):
    """
    Caso inválido: primero sin mayúscula, luego correcta.
    """
    inputs = iter(["abcdefghi1", "Abcdefg1"])  # 1° incorrecta, 2° correcta
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    verificador_contrasena()
    salida = capsys.readouterr().out

    assert "La contraseña debe contener al menos una letra mayúscula." in salida
    assert "Contraseña válida. Registro exitoso." in salida


def test_contrasena_sin_numero(monkeypatch, capsys):
    """
    Caso inválido: primero sin número, luego correcta.
    """
    inputs = iter(["Abcdefghi", "Abcdefg1"])  # 1° incorrecta, 2° correcta
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    verificador_contrasena()
    salida = capsys.readouterr().out

    assert "La contraseña debe contener al menos un número." in salida
    assert "Contraseña válida. Registro exitoso." in salida
