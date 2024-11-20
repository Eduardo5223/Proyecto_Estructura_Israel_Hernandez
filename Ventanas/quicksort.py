import tkinter as tk
from tkinter import messagebox
import random

# Lista para almacenar productos
productos = []

# Funciones para QuickSort
def quicksort_in_place(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_in_place(arr, low, pivot_index - 1)
        quicksort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j][1] <= pivot[1]:  # Comparar precios o fechas
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Interfaz gráfica para QuickSort
def show_quicksort_menu(menu_ventana):
    quicksort_menu = tk.Toplevel()
    quicksort_menu.title("Ordenamiento de Productos - QuickSort")
    quicksort_menu.geometry("500x400")

    def agregar_producto():
        nombre = entry_nombre.get().strip()
        try:
            precio = float(entry_precio.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un precio válido.")
            return

        if not nombre:
            messagebox.showerror("Error", "El nombre del producto no puede estar vacío.")
        elif precio <= 0:
            messagebox.showerror("Error", "El precio debe ser un valor positivo.")
        else:
            productos.append((nombre, precio))
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado con precio ${precio:.2f}.")
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            mostrar_productos()

    def ordenar_productos():
        if not productos:
            messagebox.showerror("Error", "No hay productos para ordenar.")
            return
        quicksort_in_place(productos, 0, len(productos) - 1)
        messagebox.showinfo("Éxito", "Los productos han sido ordenados por precio.")
        mostrar_productos()

    def mostrar_productos():
        if not productos:
            lbl_productos.config(text="No hay productos en la lista.")
        else:
            productos_texto = "\n".join([f"{nombre}: ${precio:.2f}" for nombre, precio in productos])
            lbl_productos.config(text=f"Productos:\n{productos_texto}")

    # Función para regresar al menú principal
    def regresar_menu():
        quicksort_menu.destroy()
        menu_ventana.deiconify()

    # Sección para agregar productos
    tk.Label(quicksort_menu, text="Agregar Producto", font=("Arial", 12)).pack(pady=5)
    tk.Label(quicksort_menu, text="Nombre:").pack()
    entry_nombre = tk.Entry(quicksort_menu)
    entry_nombre.pack(pady=5)
    tk.Label(quicksort_menu, text="Precio:").pack()
    entry_precio = tk.Entry(quicksort_menu)
    entry_precio.pack(pady=5)
    tk.Button(quicksort_menu, text="Agregar", command=agregar_producto).pack(pady=10)

    # Sección para ordenar productos
    tk.Button(quicksort_menu, text="Ordenar Productos", command=ordenar_productos).pack(pady=10)

    # Sección para mostrar productos
    lbl_productos = tk.Label(quicksort_menu, text="No hay productos en la lista.", font=("Arial", 10), justify="left")
    lbl_productos.pack(pady=20)

    # Botón para regresar al menú principal
    tk.Button(quicksort_menu, text="Regresar al Menú", command=regresar_menu).pack(pady=20)




