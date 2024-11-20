import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar el inventario por sección
inventario = {
    "Frutas": [],
    "Verduras": [],
    "Enlatados": []
}

# Función para mostrar la ventana de Arreglos
def show_arreglos_menu(menu_ventana):
    arreglos_menu = tk.Toplevel()
    arreglos_menu.title("Gestión de Inventario - Arreglos")
    arreglos_menu.geometry("500x400")

    # Función para agregar un producto a una sección
    def agregar_producto():
        seccion = seccion_var.get()
        producto = entry_producto.get().strip()
        if not producto.isalpha():  # Validación: Solo permite texto sin números
            messagebox.showerror("Error", "El producto solo debe contener letras.")
            return
        if seccion and producto:
            inventario[seccion].append(producto)
            messagebox.showinfo("Producto Agregado", f"Producto '{producto}' agregado a la sección '{seccion}'.")
            entry_producto.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor selecciona una sección y escribe un producto válido.")

    # Función para eliminar un producto por su índice
    def eliminar_producto():
        try:
            seccion = seccion_var.get()
            if not seccion:
                messagebox.showerror("Error", "Por favor selecciona una sección.")
                return
            indice = int(entry_indice.get())
            if 0 <= indice < len(inventario[seccion]):
                producto_eliminado = inventario[seccion].pop(indice)
                messagebox.showinfo("Producto Eliminado", f"Producto '{producto_eliminado}' eliminado de la sección '{seccion}'.")
                entry_indice.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Índice fuera de rango o sección vacía.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido para el índice.")

    # Función para mostrar los productos por sección
    def mostrar_inventario():
        inventario_texto = "\n".join(
            [f"{seccion}:\n  " + ", ".join(productos) if productos else f"{seccion}: Vacío" for seccion, productos in inventario.items()]
        )
        messagebox.showinfo("Inventario", inventario_texto if inventario_texto else "No hay productos en el inventario.")

    # Función para regresar al menú principal
    def regresar_menu():
        arreglos_menu.destroy()
        menu_ventana.deiconify()

    # Etiquetas y widgets para agregar productos
    tk.Label(arreglos_menu, text="Sección").pack(pady=5)
    seccion_var = tk.StringVar(value="Frutas")  # Valor inicial
    secciones_menu = tk.OptionMenu(arreglos_menu, seccion_var, *inventario.keys())
    secciones_menu.pack(pady=5)

    tk.Label(arreglos_menu, text="Producto").pack(pady=5)
    entry_producto = tk.Entry(arreglos_menu)
    entry_producto.pack(pady=5)
    tk.Button(arreglos_menu, text="Agregar Producto", command=agregar_producto).pack(pady=10)

    # Widgets para eliminar productos
    tk.Label(arreglos_menu, text="Eliminar Producto (Por Índice)").pack(pady=5)
    entry_indice = tk.Entry(arreglos_menu)
    entry_indice.pack(pady=5)
    tk.Button(arreglos_menu, text="Eliminar Producto", command=eliminar_producto).pack(pady=10)

    # Botones para mostrar el inventario y regresar al menú principal
    tk.Button(arreglos_menu, text="Mostrar Inventario", command=mostrar_inventario).pack(pady=10)
    tk.Button(arreglos_menu, text="Regresar al Menú", command=regresar_menu).pack(pady=10)


    arreglos_menu.mainloop()
