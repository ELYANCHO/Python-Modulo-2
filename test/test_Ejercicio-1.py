import pytest
from Ejercicio_1 import pedir_entero, pedir_si_no, calcular_precio, main




def test_calcular_precio_nino(capsys):
    precio = calcular_precio(10)
    salida = capsys.readouterr().out
    assert "Niño" in salida
    assert precio == 10000


def test_calcular_precio_joven(capsys):
    precio = calcular_precio(15)
    salida = capsys.readouterr().out
    assert "Joven" in salida
    assert precio == 15000


def test_calcular_precio_adulto(capsys):
    precio = calcular_precio(30)
    salida = capsys.readouterr().out
    assert "Adulto" in salida
    assert precio == 20000


def test_pedir_entero_valido(monkeypatch):
    entradas = iter(["5"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    valor = pedir_entero("Digite un número: ", minimo=1, maximo=10)
    assert valor == 5


def test_pedir_entero_vacio(monkeypatch, capsys):
    entradas = iter(["", "3"])  # primero vacío, luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    valor = pedir_entero("Digite un número: ", minimo=1, maximo=10)
    salida = capsys.readouterr().out
    assert "No puede dejar el campo vacío" in salida
    assert valor == 3


def test_pedir_entero_no_numerico(monkeypatch, capsys):
    entradas = iter(["abc", "4"])  # primero inválido, luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    valor = pedir_entero("Digite un número: ", minimo=1, maximo=10)
    salida = capsys.readouterr().out
    assert "Solo se permiten números enteros positivos" in salida
    assert valor == 4


def test_pedir_entero_fuera_de_rango(monkeypatch, capsys):
    entradas = iter(["0", "15", "7"])  # fuera de rango, luego válido
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    valor = pedir_entero("Digite un número: ", minimo=1, maximo=10)
    salida = capsys.readouterr().out
    assert "El valor no puede ser menor a 1" in salida or "El valor no puede ser mayor a 10" in salida
    assert valor == 7


def test_pedir_si_no_si(monkeypatch):
    entradas = iter(["si"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    assert pedir_si_no("¿Es estudiante? ") is True


def test_pedir_si_no_no(monkeypatch):
    entradas = iter(["no"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    assert pedir_si_no("¿Es estudiante? ") is False


def test_pedir_si_no_invalido(monkeypatch, capsys):
    entradas = iter(["quizás", "si"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    resultado = pedir_si_no("¿Es estudiante? ")
    salida = capsys.readouterr().out
    assert "Respuesta inválida" in salida
    assert resultado is True



def test_main_flujo_completo(monkeypatch, capsys):
    """
    Caso de prueba:
    - Cantidad = 2
    - Persona 1: edad=10 (niño), estudiante=si -> 10.000 - 10% = 9.000
    - Persona 2: edad=25 (adulto), estudiante=no -> 20.000
    - Total esperado = 29.000
    """
    entradas = iter(["2", "10", "si", "25", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main()

    salida = capsys.readouterr().out
    assert "Precio final: $9000" in salida
    assert "Precio final: $20000" in salida
    assert "Total a pagar por todas las entradas: $29000" in salida
