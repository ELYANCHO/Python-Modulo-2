def verificador_edad(edad):
    """
   Esta función toma la edad del usuario y define si es mayor de edad, niño menor, joven o mayor de edad.
   De igual manera define si la persona ha nacido o no vive.

   Args:
       edad (int): valor numérico insertado por el usuario.

   Returns:
       str: final (mensaje + el valor de la entrada al cine)
       """
    global entrada
    entrada = 0
    final =""

    if 1 < edad <= 12:
        entrada = 10000
        final = f"Usted es un niño menor, su entada tiene un costo de {entrada}"
    elif 12 <= edad <= 17:
        entrada = 15000
        final = f"Usted es un joven, su entada tiene un costo de {entrada}"
    elif 18 <= edad <= 80:
        entrada = 20000
        final = f"Usted es un adulto, su entada tiene un costo de {entrada}"
    elif edad >= 80:
        final = f"No puede ingresar muertos al cine"
    else:
        final = "No ha nacido"
    return final

def verificador_ocupacion(ocupacion):
    """
       Esta función toma la respuesta del usuario para poder definir si tiene un descuento o no.
       Todas las personas tienen descuento siempre y cuando sean estudiantes, independientemente de la edad.

       Args:
           ocupacion (str): respuesta del usuario

       Returns:
           str: final2 (mensaje + el valor de la entrada al cine con descuento)
           """
    ocupacion_nueva = ocupacion.replace(" ", "")
    final2= ""
    if ocupacion_nueva.lower() == "s":
        descuento = entrada * 0.10
        entrada_nueva = entrada - descuento
        final2 = (f"El descuento es de {descuento}\n"
                  f"------------------------------------------\n"
              f"El valor de su entrada es de {entrada_nueva}\n"
                  f"------------------------------------------")
    else:
        final2 = (f"Usted no tiene descuento\n"
              f"su Entrada es de {entrada}")
    return final2

def main (value=None):
    edad = int(input("Ingrese su edad: "))
    print(verificador_edad(edad))
    ocupacion = input("Es usted estudiante S/N: ")
    print(verificador_ocupacion(ocupacion))

if __name__ == "__main__":
    main()