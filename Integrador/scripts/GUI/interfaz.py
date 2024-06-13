import tkinter as tk
from tkinter import *

class Interfaz:
    def _init_ (self,root):
        self.root = root
        self.root.title("GESTOR DE FINANZAS")
        self.root.geometry("850x600")
        #self.ventana.attributes("-alpha",0.99)
    
    def frames_root(self): 
        self.barra_superior = tk.Frame(self.root, background= "#1f2329",height=50)
        self.barra_superior.pack(side= TOP, fill = "both")

        self.cuerpo = tk.Frame(self.root, background="#f1faff",width =150)
        self.cuerpo.pack(side= RIGHT, fill = "both", expand=True)

        self.menu_lateral = tk.Frame(self.root, background="#2a3138",width= 1500)
        self.menu_lateral.pack(side=LEFT, fill ="both", expand=False)
        
    def etiquetas(self): #etiqueta de título
        label_titulo = tk.Label(self.barra_superior, text="GESTOR DE FINANZAS PERSONALES")
        label_titulo.config(foreground="#fff",font=("Helvetica",18),background="#1f2329",pady=20,width=40)
        label_titulo.pack()

    def botones(self): #botones del menú lateral
        self.button_subpage_login = tk.Button(self.menu_lateral, text="Mi perfil",command=self.open_subpage_login)
        self.button_subpage_inc_exp = tk.Button(self.menu_lateral,text="Ingresos y gastos",command=self.open_subpage_inc_exp)
        self.button_subpage_budget = tk.Button(self.menu_lateral, text="Presupuestos",command=self.open_subpage_budget)
        self.button_subpage_investments = tk.Button(self.menu_lateral,text="Inversiones",command=self.open_subpage_investments)
        self.button_export_logs = tk.Button(self.menu_lateral,text="Registros",command=self.open_export_logs)
