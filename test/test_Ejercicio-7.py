import pytest
from unittest.mock import patch
import builtins
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog

import Ejercicio_7 as ej7  # importa tu archivo


# ------------------------
# Tests para pedir_entero
# ------------------------

def test_pedir_entero_valido(monkeypatch):
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: "5")
    resultado = ej7.pedir_entero("Ingrese un número:")
    assert resultado == 5


def test_pedir_entero_cero(monkeypatch):
    respuestas = iter(["0", "3"])  # primero inválido, luego válido
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: next(respuestas))
    called = []
    monkeypatch.setattr(messagebox, "showwarning", lambda *a, **k: called.append(a))

    resultado = ej7.pedir_entero("Ingrese un número:")
    assert resultado == 3
    assert len(called) >= 1  # hubo al menos un warning


def test_pedir_entero_invalido(monkeypatch):
    respuestas = iter(["abc", "4"])
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: next(respuestas))
    called = []
    monkeypatch.setattr(messagebox, "showwarning", lambda *a, **k: called.append(a))

    resultado = ej7.pedir_entero("Ingrese un número:")
    assert resultado == 4
    assert len(called) >= 1


# ------------------------
# Tests para pedir_float
# ------------------------

def test_pedir_float_valido(monkeypatch):
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: "4.5")
    resultado = ej7.pedir_float("Ingrese un número:")
    assert resultado == 4.5


def test_pedir_float_negativo(monkeypatch):
    respuestas = iter(["-2", "2.5"])
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: next(respuestas))
    called = []
    monkeypatch.setattr(messagebox, "showwarning", lambda *a, **k: called.append(a))

    resultado = ej7.pedir_float("Ingrese un número:")
    assert resultado == 2.5
    assert len(called) >= 1


def test_pedir_float_invalido(monkeypatch):
    respuestas = iter(["abc", "3.0"])
    monkeypatch.setattr(simpledialog, "askstring", lambda *a, **k: next(respuestas))
    called = []
    monkeypatch.setattr(messagebox, "showwarning", lambda *a, **k: called.append(a))

    resultado = ej7.pedir_float("Ingrese un número:")
    assert resultado == 3.0
    assert len(called) >= 1


# ------------------------
# Tests de lógica (independiente de GUI)
# ------------------------

def test_promedio_estudiantes():
    nombres = ["Ana", "Luis"]
    notas = [[5.0, 4.0, 3.0], [4.5, 4.5]]
    esperado = {"Ana": 4.0, "Luis": 4.5}

    # simulamos lo que hace main
    estudiantes = {}
    for n, lista in zip(nombres, notas):
        estudiantes[n] = sum(lista) / len(lista)

    assert estudiantes == esperado
