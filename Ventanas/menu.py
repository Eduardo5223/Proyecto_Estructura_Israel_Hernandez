import tkinter as tk
from tkinter import messagebox

def mostrar():
    # Crear una nueva ventana
    menu_ventana = tk.Tk()
    menu_ventana.title("Menú Estructuras")
    menu_ventana.geometry("900x700")  # Ajustar tamaño inicial

    # Configurar las columnas para que se centren los botones
    menu_ventana.columnconfigure(0, weight=1)
    menu_ventana.columnconfigure(1, weight=1)

    # Etiqueta en la ventana del menú
    label = tk.Label(menu_ventana, text="Menú", font=("Times New Roman", 16))
    label.grid(row=0, column=0, columnspan=2, pady=100, sticky="n")

    # Función para mostrar un mensaje de ejemplo por cada tema
    def mostrar_mensaje(tema):
        messagebox.showinfo("Información", f"Has seleccionado el tema: {tema}")

    # Lista de temas
    temas = [
        "Arreglos",
        "Pilas",
        "Colas",
        "QuickSort",
        "Búsqueda Binaria",
        "Listas Doblemente Ligadas",
        "Árboles",
        "Grafos"
    ]

    # Crear un botón para cada tema en dos columnas, centrado
    for i, tema in enumerate(temas):
        # Calcular la fila y columna
        fila = (i // 2) + 1
        columna = i % 2
        # Crear y colocar el botón en la grilla
        boton = tk.Button(menu_ventana, text=tema, font=("Times New Roman", 12), width=25, command=lambda t=tema: mostrar_mensaje(t))
        boton.grid(row=fila, column=columna, padx=0, pady=2, sticky="n")

    # Ajustar el tamaño de la ventana para que los elementos se centren mejor
    menu_ventana.geometry("+{}+{}".format(
        int(menu_ventana.winfo_screenwidth() / 2 - menu_ventana.winfo_reqwidth() / 2),
        int(menu_ventana.winfo_screenheight() / 2 - menu_ventana.winfo_reqheight() / 2)
    ))

    # Mantener la ventana del menú abierta
    menu_ventana.mainloop()
