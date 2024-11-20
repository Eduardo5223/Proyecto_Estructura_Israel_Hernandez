import tkinter as tk
from tkinter import ttk, messagebox


# Nodo del Árbol
class Nodo:
    def __init__(self, valor):
        # Cada nodo contiene un valor, un puntero al hijo izquierdo y otro al hijo derecho
        self.valor = valor
        self.izq = None
        self.der = None


# Clase Árbol Binario
class ArbolBinario:
    def __init__(self):
        # Inicializa el árbol con una raíz vacía
        self.raiz = None

    def insertar(self, valor):
        # Método para insertar un valor en el árbol
        if not self.raiz:
            # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
            self.raiz = Nodo(valor)
        else:
            # Llama al método recursivo para insertar en la posición adecuada
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        # Método auxiliar recursivo para encontrar la ubicación del nuevo nodo
        if valor < nodo.valor:
            if nodo.izq:
                # Si el hijo izquierdo existe, continúa buscando
                self._insertar_rec(nodo.izq, valor)
            else:
                # Si no existe, lo crea
                nodo.izq = Nodo(valor)
        elif valor > nodo.valor:
            if nodo.der:
                # Si el hijo derecho existe, continúa buscando
                self._insertar_rec(nodo.der, valor)
            else:
                # Si no existe, lo crea
                nodo.der = Nodo(valor)

    def buscar(self, valor):
        # Método para buscar un valor en el árbol
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        # Método auxiliar recursivo para buscar el valor
        if nodo is None:
            return False  # No se encontró el valor
        if nodo.valor == valor:
            return True  # Valor encontrado
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izq, valor)  # Buscar en el subárbol izquierdo
        else:
            return self._buscar_rec(nodo.der, valor)  # Buscar en el subárbol derecho

    def eliminar(self, valor):
        # Método para eliminar un nodo con un valor específico
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo, valor):
        # Método auxiliar recursivo para eliminar un nodo
        if nodo is None:
            return None
        if valor < nodo.valor:
            # Buscar el nodo a eliminar en el subárbol izquierdo
            nodo.izq = self._eliminar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            # Buscar el nodo a eliminar en el subárbol derecho
            nodo.der = self._eliminar_rec(nodo.der, valor)
        else:
            # Nodo encontrado
            if nodo.izq is None:
                return nodo.der  # Reemplazar por el subárbol derecho
            elif nodo.der is None:
                return nodo.izq  # Reemplazar por el subárbol izquierdo
            # Nodo con dos hijos: encontrar el sucesor
            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar_rec(nodo.der, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        # Encuentra el nodo con el valor mínimo en un subárbol
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo

    def recorrer(self, orden):
        # Realiza un recorrido del árbol en el orden especificado
        resultado = []
        if orden == "Inorden":
            self._inorden(self.raiz, resultado)
        elif orden == "Preorden":
            self._preorden(self.raiz, resultado)
        elif orden == "Postorden":
            self._postorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        # Recorrido inorden: izquierda, nodo, derecha
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.der, resultado)

    def _preorden(self, nodo, resultado):
        # Recorrido preorden: nodo, izquierda, derecha
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izq, resultado)
            self._preorden(nodo.der, resultado)

    def _postorden(self, nodo, resultado):
        # Recorrido postorden: izquierda, derecha, nodo
        if nodo:
            self._postorden(nodo.izq, resultado)
            self._postorden(nodo.der, resultado)
            resultado.append(nodo.valor)


# Interfaz gráfica
def show_arbol_menu(menu_ventana):
    # Instancia de un árbol binario
    arbol = ArbolBinario()

    def actualizar_canvas():
        # Actualiza el canvas dibujando el árbol actual
        canvas.delete("all")
        if arbol.raiz:
            dibujar_arbol(arbol.raiz, 250, 50, 120)

    def dibujar_arbol(nodo, x, y, desplazamiento):
        # Dibuja el árbol binario de manera recursiva
        if nodo.izq:
            canvas.create_line(x, y, x - desplazamiento, y + 50, arrow=tk.LAST)
            dibujar_arbol(nodo.izq, x - desplazamiento, y + 50, desplazamiento // 2)
        if nodo.der:
            canvas.create_line(x, y, x + desplazamiento, y + 50, arrow=tk.LAST)
            dibujar_arbol(nodo.der, x + desplazamiento, y + 50, desplazamiento // 2)
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="brown")
        canvas.create_text(x, y, text=str(nodo.valor), fill="white")

    def insertar_nodo():
        # Inserta un nodo con el valor especificado
        try:
            valor = int(entry_valor.get())
            arbol.insertar(valor)
            messagebox.showinfo("Éxito", f"Se ha insertado el valor {valor}.")
            entry_valor.delete(0, tk.END)
            actualizar_canvas()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def buscar_nodo():
        # Busca un nodo en el árbol
        try:
            valor = int(entry_valor.get())
            encontrado = arbol.buscar(valor)
            if encontrado:
                messagebox.showinfo("Resultado", f"El valor {valor} fue encontrado.")
            else:
                messagebox.showinfo("Resultado", f"El valor {valor} no fue encontrado.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def eliminar_nodo():
        # Elimina un nodo del árbol
        try:
            valor = int(entry_valor.get())
            arbol.eliminar(valor)
            messagebox.showinfo("Éxito", f"Se ha eliminado el valor {valor}.")
            entry_valor.delete(0, tk.END)
            actualizar_canvas()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor válido.")

    def recorrer_arbol():
        # Muestra el recorrido del árbol en el orden especificado
        orden = combo_recorrido.get()
        if orden:
            resultado = arbol.recorrer(orden)
            messagebox.showinfo("Recorrido", f"{orden}: {', '.join(map(str, resultado))}")
        else:
            messagebox.showerror("Error", "Seleccione un tipo de recorrido.")

    def regresar_al_menu():
        # Cierra esta ventana y regresa al menú principal
        arbol_menu.destroy()
        menu_ventana.deiconify()

    # Crear ventana
    arbol_menu = tk.Toplevel()
    arbol_menu.title("Gestión de Árboles Binarios")
    arbol_menu.geometry("800x600")

    # Widgets
    tk.Button(arbol_menu, text="Regresar", command=regresar_al_menu).pack(pady=5)
    tk.Label(arbol_menu, text="Valor:").pack()
    entry_valor = tk.Entry(arbol_menu)
    entry_valor.pack(pady=5)
    tk.Button(arbol_menu, text="Insertar", command=insertar_nodo).pack(side=tk.LEFT, padx=10, pady=5)
    tk.Button(arbol_menu, text="Buscar", command=buscar_nodo).pack(side=tk.LEFT, padx=10, pady=5)
    tk.Button(arbol_menu, text="Eliminar", command=eliminar_nodo).pack(side=tk.LEFT, padx=10, pady=5)

    # Recorridos
    tk.Label(arbol_menu, text="Recorridos:").pack(pady=5)
    combo_recorrido = ttk.Combobox(arbol_menu, values=["Inorden", "Preorden", "Postorden"])
    combo_recorrido.pack()
    tk.Button(arbol_menu, text="Recorrer", command=recorrer_arbol).pack(pady=5)

    # Canvas para el árbol
    canvas = tk.Canvas(arbol_menu, width=500, height=300, bg="white")
    canvas.pack(pady=10)

    actualizar_canvas()
