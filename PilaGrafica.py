import tkinter as tk
from tkinter import messagebox

class PilaGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Pila (Stack)")
        self.root.geometry("400x500")

        self.pila = []

        # Controles de entrada y botones
        frame_controles = tk.Frame(self.root)
        frame_controles.pack(pady=10)

        self.entry_valor = tk.Entry(frame_controles, width=10, font=("Arial", 12))
        self.entry_valor.grid(row=0, column=0, padx=5)

        btn_push = tk.Button(frame_controles, text="Push (Apilar)", command=self.push, bg="#4CAF50", fg="white")
        btn_push.grid(row=0, column=1, padx=5)

        btn_pop = tk.Button(frame_controles, text="Pop (Desapilar)", command=self.pop, bg="#f44336", fg="white")
        btn_pop.grid(row=0, column=2, padx=5)

        # Canvas para dibujar la pila
        self.canvas = tk.Canvas(self.root, width=300, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.dibujar_pila()

    def push(self):
        valor = self.entry_valor.get().strip()
        if not valor:
            messagebox.showwarning("Atención", "Ingresa un valor para apilar.")
            return

        if len(self.pila) >= 8:
            messagebox.showerror("Error", "La pila está llena (Límite visual alcanzado).")
            return

        self.pila.append(valor)
        self.entry_valor.delete(0, tk.END)
        self.dibujar_pila()

    def pop(self):
        if not self.pila:
            messagebox.showwarning("Atención", "La pila está vacía (Underflow).")
            return

        self.pila.pop()
        self.dibujar_pila()

    def dibujar_pila(self):
        self.canvas.delete("all")
        
        # Dibujar estructura del contenedor de la pila
        self.canvas.create_line(50, 50, 50, 350, width=3)
        self.canvas.create_line(250, 50, 250, 350, width=3)
        self.canvas.create_line(50, 350, 250, 350, width=3)

        # Dibujar elementos
        ancho_bloque = 180
        alto_bloque = 30
        x_inicio = 60
        y_base = 345

        for i, elemento in enumerate(self.pila):
            y1 = y_base - (i + 1) * alto_bloque
            y2 = y_base - i * alto_bloque
            
            # Bloque del elemento
            self.canvas.create_rectangle(x_inicio, y1, x_inicio + ancho_bloque, y2, fill="#2196F3", outline="black")
            self.canvas.create_text(x_inicio + ancho_bloque / 2, y1 + alto_bloque / 2, text=str(elemento), fill="white", font=("Arial", 11, "bold"))

            # Indicador TOP
            if i == len(self.pila) - 1:
                self.canvas.create_text(x_inicio + ancho_bloque + 25, y1 + alto_bloque / 2, text="← TOP", fill="red", font=("Arial", 10, "bold"))

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGrafica(root)
    root.mainloop()