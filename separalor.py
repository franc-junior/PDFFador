import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle

class Separador():
    def __init__(self):
        self.root = tk.Tk()
        self.botao_selecionar = ttk.Button()
        self.campo1 = ttk.Entry()
        self.qt_folhas = ttk.Entry()
        self.qt_dividi = ttk.Entry()
        
        self.campo_qt_paginas = ttk.Spinbox()
    
    def janela1(self):
        #tela
        self.root.geometry("600x400")
        
        #botão selecionar
        self.botao_selecionar.place(x=20, y=30)
        self.botao_selecionar.configure(text="Selecionar", command=self.busca_arquivo)
        
        #campo de texto - endereço 
        self.campo1.place(x=100, y=31)
        self.campo1.configure(width=50)
        
        linha_horizontal = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal.place(x=20, y=67, relwidth=0.65)
        
               
        #campo numero de paginas por aquivo
        label5 = ttk.Label(text="Parametros:",font=("Helvetica", 11, "bold"))
        label5.place(x=20, y=68)
        
        label1 = ttk.Label(text="Intervalo:",font=("Helvetica", 10))
        label1.place(x=40, y=100)
        self.campo_qt_paginas.place(x=100, y=101)
        self.campo_qt_paginas.configure(from_=1, to=2, increment=1, width=5)
        
        
        
        #dados do pdf x=horizontal, y=vertical
        linha_horizontal2 = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal2.place(x=20, y=132, relwidth=0.65)
        label4 = ttk.Label(text="Dados:",font=("Helvetica", 11, "bold"))
        label4.place(x=20, y=133)
        
        label2 = ttk.Label(text="Qt.Folhas:",font=("Helvetica", 10))
        label2.place(x=40, y=167)
        
        self.qt_folhas.place(x=110, y=169)
        self.qt_folhas.insert(0, "0")
        self.qt_folhas.configure(width=5, state=tk.DISABLED)
        
        label3 = ttk.Label(text="Qt.Dvidid:",font=("Helvetica", 10))
        label3.place(x=40, y=190)
        self.qt_dividi.place(x=110, y=192)
        self.qt_dividi.insert(0, "0")
        self.qt_dividi.configure(width=5, state=tk.DISABLED)
        
        self.root.mainloop()
        
    def busca_arquivo(self):
        file_path = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("PDF", "*.pdf")])
        self.campo1.config(state=tk.NORMAL)    # Habilita a edição temporariamente
        self.campo1.delete(0, tk.END)          # Apaga todo o texto do Entry
        self.campo1.insert(0, file_path)
        self.campo1.config(state=tk.DISABLED)  # Bloqueia a edição novamente
        
        
    def para_testar(self):
        pass     
        linha_horizontal = ttk.Separator(root, orient='horizontal')
        linha_horizontal.pack(fill='x', padx=20, pady=20)

inicialize = Separador()
inicialize.janela1()