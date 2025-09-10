import pytest
from Ejercicio_13 import procesar_accion

def test_ir_al_norte():
    estado_inicial = {'habitacion': 'inicio', 'tiene_llave': False}
    nuevo_estado, mensaje, juego_activo = procesar_accion("ir al norte", estado_inicial)
    assert nuevo_estado['habitacion'] == 'tesoro'
    assert "Entras en una habitación con un gran cofre" in mensaje
    assert juego_activo

def test_derrota_por_trampa():
    estado_inicial = {'habitacion': 'inicio', 'tiene_llave': False}
    nuevo_estado, mensaje, juego_activo = procesar_accion("ir al este", estado_inicial)
    assert nuevo_estado['habitacion'] == 'trampa'
    assert "GAME OVER" in mensaje
    assert not juego_activo

def test_abrir_cofre_con_llave():
    estado_inicial = {'habitacion': 'tesoro', 'tiene_llave': True}
    nuevo_estado, mensaje, juego_activo = procesar_accion("abrir cofre", estado_inicial)
    assert "GANASTE" in mensaje
    assert not juego_activo

def test_abrir_cofre_sin_llave():
    estado_inicial = {'habitacion': 'tesoro', 'tiene_llave': False}
    nuevo_estado, mensaje, juego_activo = procesar_accion("abrir cofre", estado_inicial)
    assert "cerrado con llave" in mensaje
    assert juego_activo

def test_tomar_llave():
    estado_inicial = {'habitacion': 'llave', 'tiene_llave': False}
    nuevo_estado, mensaje, juego_activo = procesar_accion("tomar llave", estado_inicial)
    assert nuevo_estado['tiene_llave']
    assert "Has recogido la llave" in mensaje
    assert juego_activo

def test_tomar_llave_ya_tenida():
    estado_inicial = {'habitacion': 'llave', 'tiene_llave': True}
    nuevo_estado, mensaje, juego_activo = procesar_accion("tomar llave", estado_inicial)
    assert nuevo_estado['tiene_llave']
    assert "Ya tienes la llave" in mensaje
    assert juego_activo

def test_accion_invalida_en_inicio():
    estado_inicial = {'habitacion': 'inicio', 'tiene_llave': False}
    nuevo_estado, mensaje, juego_activo = procesar_accion("saltar", estado_inicial)
    assert "No entiendo esa acción" in mensaje
    assert nuevo_estado['habitacion'] == 'inicio'
    assert juego_activo
