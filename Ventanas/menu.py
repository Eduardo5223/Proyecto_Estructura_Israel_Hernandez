import tkinter as tk
from tkinter import messagebox
from Ventanas import arreglos  # Importa el archivo arreglos.py para acceder a show_arreglos_menu
from Ventanas import pilas
from Ventanas import colas
from Ventanas import quicksort
from Ventanas import busqueda
from Ventanas import lista
from Ventanas import arbol
from Ventanas import grafo

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

    # Función para cerrar el menú y abrir estructura
    def abrir_arreglos():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        arreglos.show_arreglos_menu(menu_ventana)  # Abre la ventana de arreglos y pasa el menú

    def abrir_pilas():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        pilas.show_pilas_menu(menu_ventana)  # Abre la ventana de pilas y pasa el menú

    def abrir_colas():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        colas.show_colas_menu(menu_ventana)  # Abre la ventana de colas y pasa el menú
    
    def abrir_quicksort():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        quicksort.show_quicksort_menu(menu_ventana)  # Abre la ventana de quicksort y pasa el menú

    def abrir_busqueda():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        busqueda.show_busqueda_binaria_menu(menu_ventana)  # Abre la ventana de busqueda y pasa el menú

    def abrir_lista():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        lista.show_lista_doble_menu(menu_ventana)  # Abre la ventana de lista doblemente ligada y pasa el menú
    
    def abrir_arbol():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        arbol.show_arbol_menu(menu_ventana)  # Abre la ventana de arbol y pasa el menú
    
    def abrir_grafo():
        menu_ventana.withdraw()  # Cierra temporalmente el menú principal
        grafo.show_grafo_menu(menu_ventana)  # Abre la ventana de arbol y pasa el menú

    # Lista de temas con sus funciones respectivas
    temas = [
        ("Arreglos", abrir_arreglos), 
        ("Pilas", abrir_pilas),
        ("Colas", abrir_colas),
        ("QuickSort", abrir_quicksort),
        ("Búsqueda Binaria", abrir_busqueda),
        ("Listas Doblemente Ligadas", abrir_lista),
        ("Árboles", abrir_arbol),
        ("Grafos", abrir_grafo)
    ]

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


