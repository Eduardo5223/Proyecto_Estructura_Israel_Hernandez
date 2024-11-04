import tkinter as tk
from tkinter import messagebox

# Ventana Principal
root = tk.Tk()
root.title("Proyecto_Estructura_Israel_Hernandez")
root.geometry("1000x800")  # Tamaño de la ventana

# Etiquetas
def create_label(texto, pad):
    label = tk.Label(root, text=texto)
    label.pack(pady=pad)

create_label("Universidad Anahuac Mayab", 10)
create_label("Proyecto Integrador", 10)
create_label("Estructura de Datos y Algoritmos", 10)
create_label("Israel Eduardo Hernandez Valdez", 10)
  

# Función para el botón
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Has hecho clic en el botón!")

# Crear un botón
button = tk.Button(root, text="Haz clic aquí", command=mostrar_mensaje)
button.pack(pady=10)  # Agregar el botón a la ventana

# Ejecutar el bucle principal de la interfaz
root.mainloop()
