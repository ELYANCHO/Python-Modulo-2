import tkinter as tk
from tkinter import simpledialog, messagebox


def pedir_entero(mensaje: str) -> int:
    """
    Esta funcion sirve para validar si el numero es menor a 0 y si tiene otros caracteres diferentes a numeros

    Args:
        mensaje (str): Mensaje que se muestra en el cuadro de dialogo
    Returns:
        int: Numero entero mayor a 0

    """
    while True:
        valor = simpledialog.askstring("Entrada", mensaje)
        if valor and valor.strip().isdigit():  # Solo números sin espacios
            numero = int(valor.strip())
            if numero > 0:
                return numero
            else:
                messagebox.showwarning("Error", "El número debe ser mayor que 0.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un número entero válido (sin letras ni símbolos).")


def pedir_float(mensaje: str) -> float:
    """Esta funcion sirve para validar si el numero es menor a 0 y si tiene otros caracteres diferentes a numeros
    Args:
        mensaje (str): Mensaje que se muestra en el cuadro de dialogo
    Returns:
        float: Numero flotante mayor o igual a 0
    """
    while True:
        valor = simpledialog.askstring("Entrada", mensaje)
        try:
            numero = float(valor.strip())
            if numero >= 0:  # Acepta 0 pero no negativos
                return numero
            else:
                messagebox.showwarning("Error", "No se permiten números negativos.")
        except (AttributeError, ValueError):
            messagebox.showwarning("Error", "Debe ingresar un número válido (ejemplo: 3 o 3.5).")


def main():
    """
    Esta funcion sirve para pedir al usuario la cantidad de estudiantes y calcular el promedio de cada uno de ellos

    Args:
        None
    Returns:
    """
    root = tk.Tk()
    root.withdraw()  # Oculta ventana principal

    estudiantes = dict()

    # Pide cantidad de estudiantes
    cantidad = pedir_entero("Ingrese la cantidad de estudiantes:")

    for i in range(cantidad):
        # Nombre
        while True:
            nombre = simpledialog.askstring("Entrada", f"Ingrese el nombre del estudiante {i + 1}:")
            if nombre and nombre.strip() and nombre.replace(" ", "").isalpha():
                break
            else:
                messagebox.showwarning("Error", "El nombre no puede estar vacío y solo debe contener letras.")

        # Pide cantidad de notas
        cantidad_notas = pedir_entero(f"Ingrese la cantidad de notas para {nombre}:")

        # Pide notas
        notas = []
        for j in range(cantidad_notas):
            nota = pedir_float(f"Ingrese la nota {j + 1} de {nombre}:")
            notas.append(nota)

        # Calcula promedio
        promedio_estudiante = sum(notas) / len(notas)
        estudiantes[nombre] = promedio_estudiante

    # Mostrar resultados
    mensaje = "Promedios finales de los estudiantes:\n\n"
    for est, prom in estudiantes.items():
        mensaje += f"{est}: {prom:.2f}\n"

    messagebox.showinfo("Resultados", mensaje)


if __name__ == "__main__":
    main()
