import tkinter as tk
from tkinter import messagebox

# Variables globales para la pila y su límite
pila = []
limite = 5  # Límite inicial de la pila

# Función para mostrar el menú de Pilas
def show_pilas_menu(menu_ventana):
    pilas_menu = tk.Toplevel()
    pilas_menu.title("Gestión de Pilas - Productos")
    pilas_menu.geometry("700x800")

    def agregar_elemento():
        if len(pila) >= limite:
            messagebox.showerror("Error", "La estanteria está llena. Elimine elementos antes de agregar más.")
            return

        producto = entry_producto.get().strip()

        if not producto:
            messagebox.showerror("Error", "El campo de producto no puede estar vacío.")
            return

        if not producto.isalpha():
            messagebox.showerror("Error", "El nombre del producto solo debe contener letras.")
            return

        pila.append(producto)
        entry_producto.delete(0, tk.END)
        actualizar_pila()
        messagebox.showinfo("Éxito", f"Producto '{producto}' agregado a la pila.")

    def eliminar_elemento():
        if not pila:
            messagebox.showerror("Error", "La estanteria está vacía. No hay productos para eliminar.")
            return

        producto = pila.pop()
        actualizar_pila()
        messagebox.showinfo("Éxito", f"Producto '{producto}' eliminado de la estanteria.")

    def buscar_elemento():
        producto = entry_buscar.get().strip()

        if not producto:
            messagebox.showerror("Error", "El campo de búsqueda no puede estar vacío.")
            return

        if producto in pila:
            messagebox.showinfo("Búsqueda", f"El producto '{producto}' se encuentra en la estanteria.")
        else:
            messagebox.showwarning("Búsqueda", f"El producto '{producto}' no está en la estanteria.")
        
        entry_buscar.delete(0, tk.END)

    def actualizar_pila():
        pila_text.set("\n".join(reversed(pila)) if pila else "La pila está vacía.")

    def cambiar_tamano():
        global limite  # Usamos la variable global en lugar de nonlocal
        try:
            nuevo_limite = int(entry_limite.get())
            if nuevo_limite < len(pila):
                messagebox.showerror(
                    "Error", 
                    "El nuevo tamaño no puede ser menor que la cantidad actual de elementos en la estanteria."
                )
                return
            limite = nuevo_limite
            messagebox.showinfo("Éxito", f"El nuevo límite de la estanteria es: {limite}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")


    # Función para regresar al menú principal
    def regresar_menu():
        pilas_menu.destroy()
        menu_ventana.deiconify()

    # Interfaz gráfica
    tk.Label(pilas_menu, text="Pila de Productos", font=("Arial", 16)).pack(pady=10)

    # Mostrar la pila
    pila_text = tk.StringVar(value="La estanteria está vacía.")
    tk.Label(pilas_menu, textvariable=pila_text, relief="sunken", width=40, height=8, bg="white").pack(pady=10)

    # Entrada y botón para agregar productos
    tk.Label(pilas_menu, text="Agregar Producto:").pack(pady=5)
    entry_producto = tk.Entry(pilas_menu)
    entry_producto.pack(pady=5)
    tk.Button(pilas_menu, text="Agregar", command=agregar_elemento).pack(pady=5)

    # Botón para eliminar el último producto
    tk.Button(pilas_menu, text="Eliminar Último Producto", command=eliminar_elemento).pack(pady=5)

    # Entrada y botón para buscar un producto
    tk.Label(pilas_menu, text="Buscar Producto:").pack(pady=5)
    entry_buscar = tk.Entry(pilas_menu)
    entry_buscar.pack(pady=5)
    tk.Button(pilas_menu, text="Buscar", command=buscar_elemento).pack(pady=5)

    # Entrada y botón para cambiar el límite de la pila
    tk.Label(pilas_menu, text="Cambiar Tamaño de la estanteria:").pack(pady=5)
    entry_limite = tk.Entry(pilas_menu)
    entry_limite.pack(pady=5)
    tk.Button(pilas_menu, text="Cambiar Tamaño", command=cambiar_tamano).pack(pady=5)

    # Botón para regresar al menú principal
    tk.Button(pilas_menu, text="Regresar al Menú Principal", command=regresar_menu).pack(pady=10)

    actualizar_pila()

