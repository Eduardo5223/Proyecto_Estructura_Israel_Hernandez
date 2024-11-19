import tkinter as tk
from tkinter import messagebox
from Ventanas import arreglos  # Importa el archivo arreglos.py para acceder a show_arreglos_menu

def mostrar(root=None):
    # Crear una nueva ventana
    menu_ventana = tk.Toplevel(root) if root else tk.Tk()
    menu_ventana.title("Menú Estructuras")
    menu_ventana.geometry("900x700")

    # Configurar las columnas para centrar los botones
    menu_ventana.columnconfigure(0, weight=1)
    menu_ventana.columnconfigure(1, weight=1)

    # Etiqueta en la ventana del menú
    label = tk.Label(menu_ventana, text="Menú", font=("Times New Roman", 16))
    label.grid(row=0, column=0, columnspan=2, pady=100, sticky="n")

    # Función para cerrar el menú y abrir arreglos
    def abrir_arreglos():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        arreglos.show_arreglos_menu(menu_ventana)  # Abre la ventana de arreglos y pasa el menú

    # Lista de temas con sus funciones respectivas
    temas = [
        ("Arreglos", abrir_arreglos),  # Llama a abrir_arreglos en lugar de arreglos.show_arreglos_menu directamente
        ("Pilas", lambda: mostrar_mensaje("Pilas")),
        ("Colas", lambda: mostrar_mensaje("Colas")),
        ("QuickSort", lambda: mostrar_mensaje("QuickSort")),
        ("Búsqueda Binaria", lambda: mostrar_mensaje("Búsqueda Binaria")),
        ("Listas Doblemente Ligadas", lambda: mostrar_mensaje("Listas Doblemente Ligadas")),
        ("Árboles", lambda: mostrar_mensaje("Árboles")),
        ("Grafos", lambda: mostrar_mensaje("Grafos"))
    ]

    # Función para mostrar un mensaje de ejemplo por cada tema (excepto Arreglos)
    def mostrar_mensaje(tema):
        messagebox.showinfo("Información", f"Has seleccionado el tema: {tema}")

    # Crear un botón para cada tema en dos columnas
    for i, (tema, func) in enumerate(temas):
        fila = (i // 2) + 1
        columna = i % 2
        boton = tk.Button(menu_ventana, text=tema, font=("Times New Roman", 12), width=25, command=func)
        boton.grid(row=fila, column=columna, padx=0, pady=2, sticky="n")

    # Centrar la ventana en pantalla
    menu_ventana.geometry("+{}+{}".format(
        int(menu_ventana.winfo_screenwidth() / 2 - menu_ventana.winfo_reqwidth() / 2),
        int(menu_ventana.winfo_screenheight() / 2 - menu_ventana.winfo_reqheight() / 2)
    ))

    menu_ventana.mainloop()


