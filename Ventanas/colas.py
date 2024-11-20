import tkinter as tk
from tkinter import messagebox
import collections

# Creamos una cola utilizando deque
cola = collections.deque()

def show_colas_menu(menu_ventana):
    colas_menu = tk.Toplevel()
    colas_menu.title("Gestión de Clientes - Colas")
    colas_menu.geometry("400x400")

    def agregar_cliente():
        cliente = entry_cliente.get().strip()
        if not cliente:
            messagebox.showerror("Error", "Por favor ingrese un nombre válido.")
        elif not cliente.isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
        else:
            cola.append(cliente)
            messagebox.showinfo("Éxito", f"Cliente {cliente} agregado a la cola.")
            entry_cliente.delete(0, tk.END)
            mostrar_cola()

    def atender_cliente():
        if not cola:
            messagebox.showerror("Error", "La cola está vacía. No hay clientes para atender.")
        else:
            cliente_atendido = cola.popleft()
            messagebox.showinfo("Cliente Atendido", f"Se atendió al cliente: {cliente_atendido}")
            mostrar_cola()

    def mostrar_cola():
        if not cola:
            lbl_cola.config(text="La cola está vacía.")
        else:
            cola_texto = "\n".join([f"{i + 1}. {cliente}" for i, cliente in enumerate(cola)])
            lbl_cola.config(text=f"Clientes en la cola:\n{cola_texto}")
    
    def regresar_menu():
        colas_menu.destroy()
        menu_ventana.deiconify()

    # Sección para agregar cliente
    tk.Label(colas_menu, text="Agregar Cliente", font=("Arial", 12)).pack(pady=5)
    entry_cliente = tk.Entry(colas_menu)
    entry_cliente.pack(pady=5)
    tk.Button(colas_menu, text="Agregar", command=agregar_cliente).pack(pady=5)

    # Botón para atender cliente
    tk.Button(colas_menu, text="Atender Cliente", command=atender_cliente).pack(pady=10)

    # Sección para mostrar la cola
    lbl_cola = tk.Label(colas_menu, text="La cola está vacía.", font=("Arial", 10), justify="left")
    lbl_cola.pack(pady=20)

    #Regresar al menu
    tk.Button(colas_menu, text="Regresar al Menú", command=regresar_menu).pack(pady=10)

    # Mostrar la cola inicial
    mostrar_cola()
