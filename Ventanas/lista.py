import tkinter as tk
from tkinter import messagebox


class NodoDoble:
    def __init__(self, promocion, descuento):
        self.promocion = promocion
        self.descuento = descuento
        self.anterior = None
        self.siguiente = None


class ListaDoblementeLigada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, promocion, descuento):
        nuevo_nodo = NodoDoble(promocion, descuento)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def buscar(self, promocion):
        actual = self.cabeza
        while actual is not None:
            if actual.promocion == promocion:
                return actual
            actual = actual.siguiente
        return None

    def eliminar(self, promocion):
        actual = self.cabeza
        while actual is not None:
            if actual.promocion == promocion:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def obtener_promociones(self):
        promociones = []
        actual = self.cabeza
        while actual is not None:
            promociones.append((actual.promocion, actual.descuento))
            actual = actual.siguiente
        return promociones


# Crear una lista doblemente ligada
lista_promociones = ListaDoblementeLigada()

# Ventana de Lista Doblemente Ligada
def show_lista_doble_menu(menu_ventana):
    lista_menu = tk.Toplevel()
    lista_menu.title("Lista Doblemente Ligada - Promociones")
    lista_menu.geometry("500x700")

    def agregar_promocion():
        promocion = entry_promocion.get().strip()
        try:
            descuento = float(entry_descuento.get())
        except ValueError:
            messagebox.showerror("Error", "El descuento debe ser un número válido.")
            return

        if not promocion:
            messagebox.showerror("Error", "El nombre de la promoción no puede estar vacío.")
        else:
            lista_promociones.agregar(promocion, descuento)
            messagebox.showinfo("Éxito", f"Promoción '{promocion}' con descuento {descuento}% agregada.")
            entry_promocion.delete(0, tk.END)
            entry_descuento.delete(0, tk.END)
            mostrar_promociones()

    def buscar_promocion():
        promocion = entry_buscar_promocion.get().strip()
        if not promocion:
            messagebox.showerror("Error", "Por favor ingrese el nombre de la promoción a buscar.")
            return

        nodo = lista_promociones.buscar(promocion)
        if nodo:
            messagebox.showinfo("Resultado", f"Promoción encontrada: {nodo.promocion}, Descuento: {nodo.descuento}%")
        else:
            messagebox.showinfo("Resultado", "Promoción no encontrada.")

    def eliminar_promocion():
        promocion = entry_eliminar_promocion.get().strip()
        if not promocion:
            messagebox.showerror("Error", "Por favor ingrese el nombre de la promoción a eliminar.")
            return

        eliminado = lista_promociones.eliminar(promocion)
        if eliminado:
            messagebox.showinfo("Éxito", f"Promoción '{promocion}' eliminada.")
            mostrar_promociones()
        else:
            messagebox.showinfo("Error", "Promoción no encontrada.")

    def mostrar_promociones():
        promociones = lista_promociones.obtener_promociones()
        if not promociones:
            lbl_promociones.config(text="No hay promociones activas.")
        else:
            promociones_texto = "\n".join([f"{promocion} - {descuento}%" for promocion, descuento in promociones])
            lbl_promociones.config(text=f"Promociones Activas:\n{promociones_texto}")

    def regresar_al_menu():
        lista_menu.destroy()
        menu_ventana.deiconify()

    # Sección para agregar promociones
    tk.Label(lista_menu, text="Agregar Promoción", font=("Arial", 12)).pack(pady=5)
    tk.Label(lista_menu, text="Promoción:").pack()
    entry_promocion = tk.Entry(lista_menu)
    entry_promocion.pack(pady=5)
    tk.Label(lista_menu, text="Descuento (%):").pack()
    entry_descuento = tk.Entry(lista_menu)
    entry_descuento.pack(pady=5)
    tk.Button(lista_menu, text="Agregar", command=agregar_promocion).pack(pady=10)

    # Sección para buscar promociones
    tk.Label(lista_menu, text="Buscar Promoción", font=("Arial", 12)).pack(pady=10)
    tk.Label(lista_menu, text="Nombre de la Promoción:").pack()
    entry_buscar_promocion = tk.Entry(lista_menu)
    entry_buscar_promocion.pack(pady=5)
    tk.Button(lista_menu, text="Buscar", command=buscar_promocion).pack(pady=10)

    # Sección para eliminar promociones
    tk.Label(lista_menu, text="Eliminar Promoción", font=("Arial", 12)).pack(pady=10)
    tk.Label(lista_menu, text="Nombre de la Promoción:").pack()
    entry_eliminar_promocion = tk.Entry(lista_menu)
    entry_eliminar_promocion.pack(pady=5)
    tk.Button(lista_menu, text="Eliminar", command=eliminar_promocion).pack(pady=10)

    # Sección para mostrar promociones
    lbl_promociones = tk.Label(lista_menu, text="No hay promociones activas.", font=("Arial", 10), justify="left")
    lbl_promociones.pack(pady=20)

    # Botón para regresar al menú principal
    tk.Button(lista_menu, text="Regresar al Menú", command=regresar_al_menu).pack(pady=20)
