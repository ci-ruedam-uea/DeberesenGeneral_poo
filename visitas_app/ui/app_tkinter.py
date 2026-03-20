import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Registro de Visitantes")
        self.root.geometry("500x400")

        # ===== FORMULARIO =====
        tk.Label(root, text="Cédula").pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        tk.Label(root, text="Nombre").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Motivo").pack()
        self.entry_motivo = tk.Entry(root)
        self.entry_motivo.pack()

        # ===== BOTONES =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=2, padx=5)

        # ===== TABLA =====
        self.tree = ttk.Treeview(root, columns=("cedula", "nombre", "motivo"), show="headings")
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")
        self.tree.pack(fill="both", expand=True)

        self.actualizar_tabla()

    # ===== FUNCIONES =====
    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)
        if self.servicio.registrar(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        cedula = self.tree.item(seleccionado)["values"][0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Visitante eliminado")
            self.actualizar_tabla()

    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for v in self.servicio.obtener_todos():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))