from Ejercicio_1 import verificador_edad, verificador_ocupacion, main


def test_verificador_edad():
    mensaje, entrada = verificador_edad(10)
    assert "niño menor" in mensaje
    assert entrada == 10000

    mensaje, entrada = verificador_edad(15)
    assert "joven" in mensaje
    assert entrada == 15000

    mensaje, entrada = verificador_edad(30)
    assert "adulto" in mensaje
    assert entrada == 20000

    mensaje, entrada = verificador_edad(85)
    assert "muertos" in mensaje
    assert entrada == 0

    mensaje, entrada = verificador_edad(0)
    assert "No ha nacido" in mensaje
    assert entrada == 0

def test_verificador_ocupacion_estudiante():
    mensaje = verificador_ocupacion("S", 20000)
    assert "descuento" in mensaje
    assert "18000" in mensaje

    mensaje = verificador_ocupacion("N", 15000)
    assert "no tiene descuento" in mensaje
    assert "15000" in mensaje

def test_verificador_ocupacion_espacios():
    mensaje = verificador_ocupacion("  s  ", 10000)
    assert "descuento" in mensaje
    assert "9000" in mensaje
