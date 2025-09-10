import pytest
from Ejercicio_11 import validar_cedula



def test_cedula_invalida_impar(capsys):
    # suma de dígitos = 46 → impar
    assert validar_cedula("1111111112") is False
    salida = capsys.readouterr().out
    assert "Cédula inválida" in salida

def test_cedula_con_letras(capsys):
    assert validar_cedula("12345abcde") is False
    salida = capsys.readouterr().out
    assert "solo números" in salida

def test_cedula_con_menos_digitos(capsys):
    assert validar_cedula("12345") is False
    salida = capsys.readouterr().out
    assert "10 dígitos" in salida

def test_cedula_con_mas_digitos(capsys):
    assert validar_cedula("12345678901") is False
    salida = capsys.readouterr().out
    assert "10 dígitos" in salida
