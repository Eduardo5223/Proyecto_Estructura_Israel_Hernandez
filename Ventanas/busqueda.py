import tkinter as tk
from tkinter import messagebox

# Lista para almacenar productos (cada producto tiene nombre y código de barras)
productos = [
    ("Manzana", 101),
    ("Leche", 302),
    ("Pan", 403),
    ("Arroz", 504),
    ("Huevos", 205)
]

# Función de búsqueda binaria
def busqueda_binaria(arr, codigo_barra, low, high):
    if high >= low:
        mid = (high + low) // 2
        # Comprobar si el código de barras está en la posición media
        if arr[mid][1] == codigo_barra:
            return mid
        # Si el código es menor, buscar en la mitad izquierda
        elif arr[mid][1] > codigo_barra:
            return busqueda_binaria(arr, codigo_barra, low, mid - 1)
        # Si el código es mayor, buscar en la mitad derecha
        else:
            return busqueda_binaria(arr, codigo_barra, mid + 1, high)
    else:
        return -1  # No encontrado

# Ventana de búsqueda binaria
def show_busqueda_binaria_menu(menu_ventana):
    busqueda_menu = tk.Toplevel()
    busqueda_menu.title("Búsqueda Binaria - Productos")
    busqueda_menu.geometry("500x800")

    def agregar_producto():
        nombre = entry_nombre.get().strip()
        try:
            codigo = int(entry_codigo.get())
        except ValueError:
            messagebox.showerror("Error", "El código de barras debe ser un número válido.")
            return

        if not nombre:
            messagebox.showerror("Error", "El nombre del producto no puede estar vacío.")
        elif any(producto[1] == codigo for producto in productos):
            messagebox.showerror("Error", "El código de barras ya existe.")
        else:
            productos.append((nombre, codigo))
            messagebox.showinfo("Éxito", f"Producto '{nombre}' con código {codigo} agregado.")
            entry_nombre.delete(0, tk.END)
            entry_codigo.delete(0, tk.END)
            mostrar_productos()

    def ordenar_productos():
        if not productos:
            messagebox.showerror("Error", "No hay productos para ordenar.")
            return
        productos.sort(key=lambda x: x[1])  # Ordenar por código de barras
        messagebox.showinfo("Éxito", "Productos ordenados por código de barras.")
        mostrar_productos()

    def buscar_producto():
        try:
            codigo = int(entry_buscar_codigo.get())
        except ValueError:
            messagebox.showerror("Error", "El código de barras debe ser un número válido.")
            return

        if not productos:
            messagebox.showerror("Error", "No hay productos en la lista.")
            return

        resultado = busqueda_binaria(productos, codigo, 0, len(productos) - 1)
        if resultado != -1:
            producto = productos[resultado]
            messagebox.showinfo("Resultado", f"Producto encontrado: {producto[0]}, Código: {producto[1]}")
        else:
            messagebox.showinfo("Resultado", "Producto no encontrado.")

    def mostrar_productos():
        productos_texto = (
            "Productos:\n" +
            "\n".join([f"{nombre} - Código: {codigo}" for nombre, codigo in productos])
            if productos else "No hay productos en la lista."
        )
        lbl_productos.config(text=productos_texto)

    def regresar_al_menu():
        busqueda_menu.destroy()
        menu_ventana.deiconify()

    # Sección para agregar productos
    tk.Label(busqueda_menu, text="Agregar Producto", font=("Arial", 12)).pack(pady=5)
    tk.Label(busqueda_menu, text="Nombre:").pack()
    entry_nombre = tk.Entry(busqueda_menu)
    entry_nombre.pack(pady=5)
    tk.Label(busqueda_menu, text="Código de Barras:").pack()
    entry_codigo = tk.Entry(busqueda_menu)
    entry_codigo.pack(pady=5)
    tk.Button(busqueda_menu, text="Agregar", command=agregar_producto).pack(pady=10)

    # Sección para ordenar productos
    tk.Button(busqueda_menu, text="Ordenar Productos por Código", command=ordenar_productos).pack(pady=10)

    # Sección para buscar productos
    tk.Label(busqueda_menu, text="Buscar Producto", font=("Arial", 12)).pack(pady=10)
    tk.Label(busqueda_menu, text="Código de Barras:").pack()
    entry_buscar_codigo = tk.Entry(busqueda_menu)
    entry_buscar_codigo.pack(pady=5)
    tk.Button(busqueda_menu, text="Buscar", command=buscar_producto).pack(pady=10)

    # Sección para mostrar productos
    lbl_productos = tk.Label(busqueda_menu, text="", font=("Arial", 10), justify="left")
    lbl_productos.pack(pady=20)

    # Mostrar productos iniciales en la interfaz
    mostrar_productos()

    # Botón para regresar al menú principal
    tk.Button(busqueda_menu, text="Regresar al Menú", command=regresar_al_menu).pack(pady=20)

