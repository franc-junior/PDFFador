import tkinter as tk
import os
from tkinter import ttk
from tkinter import filedialog
from pdf2image import convert_from_path
from PIL import Image, ImageTk
from tkinter import Canvas, Scrollbar

class Separador():
    def __init__(self):
        self.root = tk.Tk()
        self.botao_selecionar = ttk.Button()
        self.campo1 = ttk.Entry()
        self.qt_folhas = ttk.Entry()
        self.qt_dividi = ttk.Entry()
        self.campo_qt_paginas = ttk.Spinbox()
        self.botao_atualizar = ttk.Button()
        self.botao_separar = ttk.Button()
        self.canvas = tk.Canvas()
        self.imagem_tk = None
        self.imagem_tk2 = None
        self.nome_pdf = ttk.Entry()
        self.num_pdf = ttk.Spinbox()
        self.scrollbar = Scrollbar()
    
    def janela1(self):
        #tela
        self.root.geometry("800x400")
        self.root.resizable(False, False)
        
        label6 = ttk.Label(text="Caminho:",font=("Helvetica", 11, "bold"))
        label6.place(x=20, y=5)
        
        #botão selecionar
        self.botao_selecionar.place(x=40, y=40)
        self.botao_selecionar.configure(text="Selecionar", command=self.busca_arquivo)
        
        #campo de texto - endereço 
        self.campo1.place(x=120, y=41)
        self.campo1.configure(width=41)
        
        linha_horizontal = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal.place(x=20, y=87, relwidth=0.45)
        
               
        #campo numero de paginas por aquivo
        label5 = ttk.Label(text="Parametros:",font=("Helvetica", 11, "bold"))
        label5.place(x=20, y=88)
        
        label1 = ttk.Label(text="Intervalo:",font=("Helvetica", 10))
        label1.place(x=40, y=120)
        self.campo_qt_paginas.place(x=100, y=121)
        self.campo_qt_paginas.configure(from_=1, to=2, increment=1, width=5)
        
        #dados do pdf x=horizontal, y=vertical
            #linha
        linha_horizontal2 = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal2.place(x=20, y=182, relwidth=0.45)
        label4 = ttk.Label(text="Dados:",font=("Helvetica", 11, "bold"))
        label4.place(x=20, y=183)
            #qt.folhas
        label2 = ttk.Label(text="Qt.Folhas:",font=("Helvetica", 10))
        label2.place(x=40, y=217)
        self.qt_folhas.place(x=110, y=219)
        self.qt_folhas.insert(0, "0")
        self.qt_folhas.configure(width=5, state=tk.DISABLED)
            #qt.dividido
        label3 = ttk.Label(text="Qt.Dvidido:",font=("Helvetica", 10))
        label3.place(x=40, y=240)
        self.qt_dividi.place(x=110, y=242)
        self.qt_dividi.insert(0, "0")
        self.qt_dividi.configure(width=5, state=tk.DISABLED)
        
        #Botões de ação
            #linha
        linha_horizontal3 = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal3.place(x=20, y=300, relwidth=0.45)
        label5 = ttk.Label(text="Ações:",font=("Helvetica", 11, "bold"))
        label5.place(x=20, y=301)
        
            #estilo dos botões
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica", 16))  # Altere o tamanho da fonte conforme necessário    
            #botão atualizar
        self.botao_atualizar.place(x=40, y=350)
        self.botao_atualizar.configure(text="ATUALIZAR",style="Custom.TButton")
            #botão separar
        self.botao_separar.place(x=200, y=350)
        self.botao_separar.configure(text="SEPARAR",style="Custom.TButton" ,command=self.busca_arquivo)

        #Area que mostra a imagem
        self.canvas.configure(width=390, height=400)
        self.canvas.place(x=390)
        self.canvas.create_rectangle(1, 1, 390, 300, fill="#FBF7B9")
               
        #Edição do nome do pdf  
            #setas que muda de pdf
        self.num_pdf.place(x=720, y=350)
        self.num_pdf.configure(from_=1, to=100, increment=1, width=3, font=("Helvetica", 16))
            #campo de texto que renomeia o pdf
        self.nome_pdf.place(x=390, y=350)
        self.nome_pdf.configure(width=25, font=("Helvetica", 16))

               
        self.root.mainloop()
        
    def busca_arquivo(self):
        file_path = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("PDF", "*.pdf")])
        self.campo1.config(state=tk.NORMAL)    # Habilita a edição temporariamente
        self.campo1.delete(0, tk.END)          # Apaga todo o texto do Entry
        self.campo1.insert(0, file_path)
        self.campo1.config(state=tk.DISABLED)  # Bloqueia a edição novamente
        
        self.abrir_pdf(file_path)
    
    def abrir_pdf(self, caminho):
        #print(r"{}\poppler-23.08.0\Library\bin".format(os.getcwd()))
        #print(type(caminho))
        #os.environ['POPPLER_PATH'] = r"D:/Estudo/GitHub/PDFFador/poppler-23.08.0/Library/bin"
        
        self.canvas.delete("all") # Limpe o Canvas, caso já haja imagens anteriores
        imagens = convert_from_path(caminho) # converte as paginas para imagem

        imagem = imagens[0]
        imagem2 = imagens[1].resize((400,570))
        
        redemensionada = imagem.resize((400,570))
        
        self.imagem_tk2 = ImageTk.PhotoImage(imagem2)
        self.imagem_tk = ImageTk.PhotoImage(redemensionada)
        
        #cria as imagens
        self.canvas.create_image(200, 0, anchor=tk.N, image=self.imagem_tk)
        self.canvas.create_image(200, 580, anchor=tk.N, image=self.imagem_tk2)
        
        #contador que indica onde a imagem vai aparecer, no lugar do 580
        #y += imagem.height() + 10
        
        #limita a rolagem
        self.canvas.config(scrollregion=(0, 0, 0, 1200), width=400, height=330)
        
        #atualiza o canvas
        self.canvas.update()
        
        #define o scroll
        self.scrollbar.configure(orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Ative a rolagem com a roda do mouse
        self.canvas.bind_all("<MouseWheel>", self.rolar)
        
        #imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
        
        # Exiba cada imagem no Canvas
        # for imagem in imagens:
        #     imagem_tk = ImageTk.PhotoImage(imagem)
        #     self.canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)
        #     self.canvas.update()
        #     print(imagem_tk)
            # Mantenha uma referência para a imagem para evitar que seja coletada pelo garbage collector
        #imagem_tk.append(imagem)
           
    def rolar(self, event):
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def para_testar(self):    
        linha_horizontal = ttk.Separator(root, orient='horizontal')
        linha_horizontal.pack(fill='x', padx=20, pady=20)

inicialize = Separador()
inicialize.janela1()