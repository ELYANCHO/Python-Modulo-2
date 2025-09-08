def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        entrada = input(mensaje).strip()

        if not entrada:
            print("\n  No puede dejar el campo vacío.")
            continue

        if not entrada.isdigit():
            print(" Solo se permiten números enteros positivos.")
            continue

        valor = int(entrada)

        if minimo is not None and valor < minimo:
            print(f"\n  El valor no puede ser menor a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"\n  El valor no puede ser mayor a {maximo}.")
            continue

        return valor


def pedir_si_no(mensaje):
    while True:
        entrada = input(mensaje).strip().lower()

        if not entrada:
            print("  No puede dejar la respuesta vacía.")
            continue

        if entrada in ["si"]:
            return True
        elif entrada in ["no"]:
            return False
        else:
            print("  Respuesta inválida. Escriba 'si' o 'no'.")


def calcular_precio(edad):
    if edad < 12:
        print("Categoría: Niño")
        return 10000
    elif 12 <= edad < 18:
        print("Categoría: Joven")
        return 15000
    else:
        print("Categoría: Adulto")
        return 20000


def main():

    print(" Bienvenido al sistema del cine ")


    cantidad = pedir_entero("Digite la cantidad de personas a ingresar: ", minimo=1, maximo=20)

    total_general = 0

    for i in range(cantidad):
        print(f"\n Persona número {i + 1}")

        edad = pedir_entero("Digite su edad: ", minimo=1, maximo=90)
        precio = calcular_precio(edad)

        if pedir_si_no("¿Es estudiante? (si/no): "):
            descuento = precio * 0.10
            precio -= descuento
            print(f" Descuento aplicado: ${descuento:.0f}")
        else:
            print(" No aplica descuento.")

        print(f" Precio final: ${precio:.0f}")
        total_general += precio

    print("\n" + "-" * 50)
    print(f" Total a pagar por todas las entradas: ${total_general:.0f}")
    print("-" * 50)


if __name__ == "__main__":
    main()