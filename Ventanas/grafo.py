import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt


class GrafoTienda:
    def __init__(self):
        self.grafo = nx.Graph()  # Grafo inicializado vacío

    def agregar_seccion(self, seccion):
        """
        Agrega un nodo al grafo.
        """
        if seccion not in self.grafo:
            self.grafo.add_node(seccion)
            return True
        return False

    def agregar_conexion(self, seccion1, seccion2):
        """
        Agrega una conexión (arista) entre dos secciones.
        """
        if seccion1 in self.grafo and seccion2 in self.grafo:
            self.grafo.add_edge(seccion1, seccion2)
            return True
        return False

    def calcular_ruta_corta(self, inicio, destino):
        """
        Calcula la ruta más corta entre dos nodos.
        """
        try:
            return nx.shortest_path(self.grafo, source=inicio, target=destino)
        except nx.NetworkXNoPath:
            return None

    def mostrar_grafo(self):
        """
        Muestra el grafo con Matplotlib.
        """
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.grafo)  # Posición automática de los nodos
        nx.draw(self.grafo, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
        plt.title("Mapa de la Tienda")
        plt.show()


# Ventana para la gestión de Grafos
def show_grafo_menu(menu_ventana):
    grafo = GrafoTienda()
    grafo_menu = tk.Toplevel()
    grafo_menu.title("Grafo - Mapa de la Tienda")
    grafo_menu.geometry("500x600")

    def agregar_nodo():
        seccion = entry_seccion.get().strip()
        if not seccion:
            messagebox.showerror("Error", "La sección no puede estar vacía.")
            return

        if grafo.agregar_seccion(seccion):
            messagebox.showinfo("Éxito", f"Sección '{seccion}' agregada al grafo.")
        else:
            messagebox.showerror("Error", f"La sección '{seccion}' ya existe.")
        entry_seccion.delete(0, tk.END)

    def agregar_arista():
        seccion1 = entry_seccion1.get().strip()
        seccion2 = entry_seccion2.get().strip()

        if not seccion1 or not seccion2:
            messagebox.showerror("Error", "Ambas secciones deben ser especificadas.")
            return

        if grafo.agregar_conexion(seccion1, seccion2):
            messagebox.showinfo("Éxito", f"Conexión agregada entre '{seccion1}' y '{seccion2}'.")
        else:
            messagebox.showerror("Error", "Ambas secciones deben existir en el grafo.")
        entry_seccion1.delete(0, tk.END)
        entry_seccion2.delete(0, tk.END)

    def calcular_ruta():
        inicio = entry_inicio.get().strip()
        destino = entry_destino.get().strip()

        if inicio == "" or destino == "":
            messagebox.showerror("Error", "Ambas secciones deben ser especificadas.")
            return

        ruta = grafo.calcular_ruta_corta(inicio, destino)
        if ruta:
            messagebox.showinfo("Ruta más Corta", f"La ruta más corta es: {' -> '.join(ruta)}")
        else:
            messagebox.showerror("Error", f"No hay conexión entre '{inicio}' y '{destino}'.")
        entry_inicio.delete(0, tk.END)
        entry_destino.delete(0, tk.END)

    def mostrar_grafo():
        grafo.mostrar_grafo()

    def regresar_al_menu():
        grafo_menu.destroy()
        menu_ventana.deiconify()

    # Sección de control
    tk.Label(grafo_menu, text="Gestión del Mapa de la Tienda", font=("Arial", 12)).pack(pady=10)

    # Agregar nodos (secciones)
    tk.Label(grafo_menu, text="Agregar Sección:").pack()
    entry_seccion = tk.Entry(grafo_menu)
    entry_seccion.pack(pady=5)
    tk.Button(grafo_menu, text="Agregar Sección", command=agregar_nodo).pack(pady=5)

    # Agregar aristas (conexiones)
    tk.Label(grafo_menu, text="Agregar Conexión:").pack()
    tk.Label(grafo_menu, text="Sección 1:").pack()
    entry_seccion1 = tk.Entry(grafo_menu)
    entry_seccion1.pack(pady=5)
    tk.Label(grafo_menu, text="Sección 2:").pack()
    entry_seccion2 = tk.Entry(grafo_menu)
    entry_seccion2.pack(pady=5)
    tk.Button(grafo_menu, text="Agregar Conexión", command=agregar_arista).pack(pady=5)

    # Ruta más corta
    tk.Label(grafo_menu, text="Calcular Ruta Más Corta:").pack(pady=10)
    tk.Label(grafo_menu, text="Inicio:").pack()
    entry_inicio = tk.Entry(grafo_menu)
    entry_inicio.pack(pady=5)
    tk.Label(grafo_menu, text="Destino:").pack()
    entry_destino = tk.Entry(grafo_menu)
    entry_destino.pack(pady=5)
    tk.Button(grafo_menu, text="Calcular Ruta", command=calcular_ruta).pack(pady=5)

    # Mostrar grafo
    tk.Button(grafo_menu, text="Mostrar Grafo", command=mostrar_grafo).pack(pady=20)

    # Botón para regresar al menú principal
    tk.Button(grafo_menu, text="Regresar al Menú", command=regresar_al_menu).pack(pady=20)
