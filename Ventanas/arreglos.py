import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los precios
precios = []

# Función para mostrar la ventana de Arreglos
def show_arreglos_menu(menu_ventana):
    arreglos_menu = tk.Toplevel()
    arreglos_menu.title("Gestión de Precios - Arreglos")
    arreglos_menu.geometry("400x300")

    # Función para agregar precio
    def agregar_precio():
        try:
            precio = float(entry_precio.get())
            precios.append(precio)
            messagebox.showinfo("Precio Agregado", f"Precio {precio} agregado a la lista.")
            entry_precio.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    # Función para eliminar precio por índice
    def eliminar_precio():
        try:
            indice = int(entry_indice.get())
            if 0 <= indice < len(precios):
                precios.pop(indice)
                messagebox.showinfo("Precio Eliminado", f"El precio en la posición {indice} fue eliminado.")
                entry_indice.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Índice fuera de rango.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    # Función para mostrar los precios
    def mostrar_precios():
        precios_text = "\n".join([f"{i}: ${precio}" for i, precio in enumerate(precios)])
        if precios_text:
            messagebox.showinfo("Lista de Precios", precios_text)
        else:
            messagebox.showinfo("Lista de Precios", "No hay precios en la lista.")

    # Función para sumar los precios
    def sumar_precios():
        precio_final = sum(precios)
        messagebox.showinfo("Precio Final", f"El precio total es de: ${precio_final:.2f}")

    # Función para regresar al menú principal
    def regresar_menu():
        arreglos_menu.destroy()  # Cierra la ventana de arreglos
        menu_ventana.deiconify()  # Reabre la ventana de menú principal

    # Etiquetas y entradas para agregar y eliminar precios
    tk.Label(arreglos_menu, text="Agregar Precio").pack(pady=5)
    entry_precio = tk.Entry(arreglos_menu)
    entry_precio.pack(pady=5)
    tk.Button(arreglos_menu, text="Agregar", command=agregar_precio).pack(pady=5)

    tk.Label(arreglos_menu, text="Eliminar Precio por Índice").pack(pady=5)
    entry_indice = tk.Entry(arreglos_menu)
    entry_indice.pack(pady=5)
    tk.Button(arreglos_menu, text="Eliminar", command=eliminar_precio).pack(pady=5)

    tk.Button(arreglos_menu, text="Mostrar Precios", command=mostrar_precios).pack(pady=10)
    tk.Button(arreglos_menu, text="Sumar Precios", command=sumar_precios).pack(pady=10)
    
    # Botón para regresar al menú principal
    tk.Button(arreglos_menu, text="Regresar al Menú", command=regresar_menu).pack(pady=10)

    # Ocultar la ventana de menú principal mientras se muestra la ventana de arreglos

    arreglos_menu.mainloop()
