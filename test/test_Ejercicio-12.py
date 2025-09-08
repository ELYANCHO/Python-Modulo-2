import pytest
from Ejercicio_12 import simulador_dados

def test_simulador_dados_con_valores_fijos(monkeypatch):
    # Simulamos que siempre salen 3 y 4 → suma = 7
    valores = [3, 4] * 50  # 50 lanzamientos (25 pares)
    iterador = iter(valores)

    def fake_randint(a, b):
        return next(iterador)

    monkeypatch.setattr("random.randint", fake_randint)

    resultados = simulador_dados(25)  # 25 lanzamientos de 2 dados

    # Solo debe haber la suma 7 con frecuencia 25
    assert resultados == {7: 25}


def test_simulador_dados_total_intentos():
    intentos = 1000
    resultados = simulador_dados(intentos)

    # La suma total de frecuencias debe ser igual al número de intentos
    assert sum(resultados.values()) == intentos

    # Todas las claves deben estar en el rango de 2 a 12
    assert all(2 <= k <= 12 for k in resultados.keys())
