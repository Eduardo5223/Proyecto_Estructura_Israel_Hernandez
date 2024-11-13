import tkinter as tk
from Ventanas import menu
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk

# Ventana Principal
root = tk.Tk()
# Configura el color de fondo
root.configure(bg="white")  # Cambia "lightblue" por el color que desees
root.title("Proyecto_Estructura_Israel_Hernandez")
root.geometry("1000x800")  # Tamaño de la ventana
     
# Variable global para guardar la imagen
imagen_global = None

# Funciones
def create_label(texto, pad, fuente, size_letra):
    mi_fuente = font.Font(family=fuente, size=size_letra, weight="bold")
    label = tk.Label(root, text=texto, font=mi_fuente, bg="white")
    label.pack(pady=pad)

def image_label(ruta, pad, tamano):
    global imagen_global  # Para que la imagen persista
    # Cargar la imagen
    imagen_original = Image.open(ruta)  # Coloca la ruta de tu imagen
    imagen_redimensionada = imagen_original.resize(tamano)
    imagen_global = ImageTk.PhotoImage(imagen_redimensionada)
    # Crear una etiqueta con la imagen
    label_imagen = tk.Label(root, image=imagen_global, bg="white")
    label_imagen.pack(pady=pad)

def abrir_menu():
    root.destroy()  # Cierra la ventana principal
    menu.mostrar()  # Llama a la función de la nueva ventana



#Etiquetas
image_label("./imagenes/logo.jpg", 10, (500, 200))
create_label("Universidad Anahuac Mayab", 10, "Times New Roman", 18)
create_label("Proyecto Integrador", 20, "Times New Roman", 18)
create_label("Estructura de Datos y Algoritmos", 20, "Times New Roman", 18)
create_label("Israel Eduardo Hernandez Valdez", 20, "Times New Roman", 18)
  

# Función para el botón
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Has hecho clic en el botón!")

# Crear un botón
button = tk.Button(root, text="Comenzar", command=abrir_menu, width = 25, height = 2)
button.pack(pady=10)  # Agregar el botón a la ventana

# Ejecutar el bucle principal de la interfaz
root.mainloop()
