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