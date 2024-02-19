import math
import tkinter as tk
import PyPDF2
import os
from tkinter import ttk, filedialog, Scrollbar
from pdf2image import convert_from_path
from PIL import ImageTk
#import pyautogui

class Separador():
    def __init__(self):
        self.root = tk.Tk()
        #button
        self.botao_selecionar = ttk.Button()
        self.botao_onde_salvar = ttk.Button()
        self.botao_atualizar = ttk.Button()
        self.botao_separar = ttk.Button()
        #entry
        self.campo1 = ttk.Entry()
        self.campo_onde_salvar = ttk.Entry()
        self.qt_folhas = ttk.Entry()
        self.qt_dividi = ttk.Entry()
        self.nome_pdf = ttk.Entry()
        #spinbox
        self.campo_qt_paginas = ttk.Spinbox()
        self.num_pdf = ttk.Spinbox()
        #outros
        self.canvas = tk.Canvas()
        self.scrollbar = Scrollbar()
        self.imagem_tk = None
        self.imagens_tks = []
        self.matriz = []
        self.nome_dos_pdfs = []
        self.caminho = None
        self.caminho_salvar = None
        self.num_pdf_anterior = [1]
    
    def janela1(self): #interface do sistema
        #tela
        self.root.geometry("800x400")
        self.root.resizable(False, False)
         
        #CAMINHO
            #Texto caminho
        label6 = ttk.Label(text="Caminho:",font=("Helvetica", 11, "bold"))
        label6.place(x=20, y=5)
            #botão selecionar
        self.botao_selecionar.place(x=40, y=40)
        self.botao_selecionar.configure(text="Selecionar", command=self.busca_arquivo)
            #campo de texto que mostra o caminho do arquivo
        self.campo1.place(x=120, y=41)
        self.campo1.configure(width=41)
            #linha horizontal
        linha_horizontal = ttk.Separator(self.root, orient='horizontal')
        linha_horizontal.place(x=20, y=87, relwidth=0.45)
               
        #PARAMETROS
            #texto parametros
        label5 = ttk.Label(text="Parametros:",font=("Helvetica", 11, "bold"))
        label5.place(x=20, y=88)
            #texto intervalo
        label1 = ttk.Label(text="Intervalo:",font=("Helvetica", 10))
        label1.place(x=40, y=120)
            #campo para definir a separação das paginas
        self.campo_qt_paginas.place(x=97, y=121)
        self.campo_qt_paginas.configure(from_=1,to=100, increment=1, width=5)
        self.campo_qt_paginas.insert(0,1)
            #botão selecionar
        self.botao_onde_salvar.place(x=160, y=119)
        self.botao_onde_salvar.configure(text="OndeSalvar", command=self.lugarSalvar)
            #campo de texto que mostra o caminho do arquivo
        self.campo_onde_salvar.place(x=240, y=120)
        self.campo_onde_salvar.configure(width=21)
        
        #DADOS do pdf x=horizontal, y=vertical
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
            #Texto ações
        label5 = ttk.Label(text="Ações:",font=("Helvetica", 11, "bold"))
        label5.place(x=20, y=301)
            #estilo dos botões
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica", 16))  # Altere o tamanho da fonte conforme necessário    
            #botão atualizar
        self.botao_atualizar.place(x=40, y=350)
        self.botao_atualizar.configure(text="ATUALIZAR",style="Custom.TButton", command=self.atualizar)
            #botão separar
        self.botao_separar.place(x=200, y=350)
        self.botao_separar.configure(text="SEPARAR",style="Custom.TButton" ,command=self.separar_pdf)

        #Area que mostra a imagem
        self.canvas.configure(width=390, height=400)
        self.canvas.place(x=390)
        self.canvas.create_rectangle(1, 1, 390, 300, fill="#FBF790")
        self.canvas.bind('<Motion>', self.zoom) ####################################
               
        #Edição do nome do pdf  
            #setas que muda de pdf
        # style_spin = ThemedStyle()
        # style_spin.configure("TSpinbox", arrowsize=10)
        self.num_pdf.place(x=720, y=350)
        self.num_pdf.configure(from_=1, to=100, style="TSpinbox" , increment=1, width=3, font=("Helvetica", 16), state="readonly", command=self.passa_pdf)
        self.num_pdf.bind("<FocusIn>", self.atera_num_anterior)

            #campo de texto que renomeia o pdf
        self.nome_pdf.place(x=390, y=350)
        self.nome_pdf.configure(width=25, font=("Helvetica", 16))
        self.nome_pdf.bind("<FocusOut>", self.salva_nome) # quando o entry perder o foco, vai executar a função
               
        self.root.mainloop()
    
    def lugarSalvar(self):
        #self.zerar_variaveis()
        file_path = filedialog.askdirectory(title="Selecione uma pasta")
        self.escreverEntry(self.campo_onde_salvar, file_path)
        self.caminho_salvar = file_path
        #self.abrir_pdf()
        
    def atera_num_anterior(self, a): #sempre que muda de numero no pdf_num o novo numero é adicionado a lista, então para pegar o numero anterior, é só pegar o penultimo numero da lista
        num_atual = int(self.num_pdf.get())  
        self.num_pdf_anterior.append(num_atual)
        self.nome_pdf.focus_set()
    
    
    def salva_nome(self,a):#salva os novos nomes dos PDFs na lista
        print(self.num_pdf_anterior)
        novo_foco = str(a.widget.focus_get())
        nome = self.nome_pdf.get()
        
        if novo_foco == ".!spinbox2":
            num_pdf_anteror = self.num_pdf_anterior[-1]-1
            
        self.nome_dos_pdfs[num_pdf_anteror] = nome
    
    
    def zoom(self, event):
        pass
        
            
    def gera_matriz_pdf(self): #gera uma matriz separando o pdf
        self.nome_dos_pdfs = []
        
        imagens = convert_from_path(self.caminho)
        
        self.escreverEntry(self.qt_folhas, len(imagens)) #escreve no entry que indica a quantidade de folhas
        self.escreverEntry(self.qt_dividi, len(imagens)/int(self.campo_qt_paginas.get()))#escreve no entry que indica a quantidade de pdfs
        self.num_pdf.configure(to=math.ceil(float(self.qt_dividi.get())))
        
        qt_dividi = math.ceil(float(self.qt_dividi.get())) #valor de PDFs divididos
        divsor = int(self.campo_qt_paginas.get()) #divisor
        self.matriz = []

        cont = 0
        for pdf in range(qt_dividi): #loop que gera a matriz com as paginas dos PDFs divididos
            linha = []
            for col in range(divsor):
                linha.append(imagens[cont])
                cont+=1
            self.matriz.append(linha)
            self.nome_dos_pdfs.append("pdf{}".format(pdf+1))
        
        
     
            
    def passa_pdf(self): # Função responsavel por navegar entre os PDFs e seus nomes
        #self.atera_num_anterior()
        nome_dos_pdfs = self.nome_dos_pdfs #lista com o nome dos pdfs
        num_pdf = int(self.num_pdf.get())-1 
        self.pdf_canva(self.matriz[num_pdf]) #coloca o pdf setado no num_pdf no canva
        
        self.nome_pdf.delete(0, tk.END)          # Apaga todo o texto do Entry
        self.nome_pdf.insert(0, nome_dos_pdfs[num_pdf])# Escreve no entry
        #self.nome_pdf.focus_set()
        self.nome_pdf.select_range(0, 'end')
        #nome_dos_pdfs[num_pdf] = self.nome_pdf.get()
        #self.nome_dos_pdfs = nome_dos_pdfs
        
        
        
        
    def pdf_canva(self, imagens): #Organiza todas as imagens do pdf no canva
        y = 0 #contador que devine o espaço entre as imagens e o tamanho do scrollregion
        for img in imagens: #loop para empilhar as imagens do pdf
            self.imagem_tk = ImageTk.PhotoImage(img.resize((380,540))) #converte para um formato que pode ser exibido no cavas e diminui o tamanho da imagem
            self.canvas.create_image(200, y, anchor=tk.N, image=self.imagem_tk) #coloca a imagem no canvas    
            self.imagens_tks.append(self.imagem_tk) #adiciona a imagem a uma lista, para que ela não se perda e continue aparecendo no canvas
            y += 550  
        self.canvas.config(scrollregion=(0, 0, 0, y), width=400, height=330) #tamanho do scrollregion
        self.canvas.update() #atualiza o canvas com as noavs imagens                  
    
    
    def atualizar(self):
        self.abrir_pdf()    
        
        
    def zerar_variaveis(self):
        self.imagem_tk = None
        self.imagens_tks = []
        self.matriz = []
        self.nome_dos_pdfs = []
        self.caminho = None
        self.num_pdf_anterior = [1]
                
             
    def abrir_pdf(self): #mostra as paginas do pdf na area canvas
        #os.environ['POPPLER_PATH'] = r"D:/Estudo/GitHub/PDFFador/poppler-23.08.0/Library/bin"  
        
        self.canvas.delete("all") # Limpe o Canvas, caso já haja imagens anteriores
        self.gera_matriz_pdf() #gera a matriz
        imagens = self.matriz[0] #primeiro pdf
        self.pdf_canva(imagens) #imprime as paginas do pdf no canvas

        #DEFINE O SCROLLBAR
        self.scrollbar.configure(orient="vertical", command=self.canvas.yview) #orientação e comando
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y) #posição
        self.canvas.configure(yscrollcommand=self.scrollbar.set) #coloca o scrollbar no canvas
        self.canvas.bind_all("<MouseWheel>", self.rolar) # Ative a rolagem com a roda do mouse

        #imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
           
          
    def separar_pdf(self): #função responsavel por separar os pdfs com suas devidas paginas
        pdf_reader = PyPDF2.PdfReader(self.caminho) #Abra o arquivo PDF original
        qt_dividi = math.ceil(float(self.qt_dividi.get()))
        divsor = int(self.campo_qt_paginas.get())
        lista_nomes = self.nome_dos_pdfs
            
        cont = 0
        for pdf_pg in range(qt_dividi): #loop da quantidade total de arquivos
            pdf_wr = PyPDF2.PdfWriter() #abre o pdf para escrita
            for pg in range(divsor): #loop das paginas do arquivo original
                pdf_wr.add_page(pdf_reader.pages[cont]) #adiciona as paginas ao pdf aberto
                cont += 1 #contador das paginas
            with open("{}/{}.pdf".format(self.caminho_salvar, lista_nomes[pdf_pg]), "wb") as output:
                pdf_wr.write(output) #salva o pdf
                print("\n{}/{}".format(self.caminho_salvar, lista_nomes[pdf_pg]), pdf_pg)
        #self.reset__init__()
            
            
        
                    
    def busca_arquivo(self): # Procura o arquivo que será editado
        self.zerar_variaveis()
        file_path = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("PDF", "*.pdf")])
        self.escreverEntry(self.campo1, file_path)
        self.caminho = file_path
        self.abrir_pdf()
    
    
    def escreverEntry(self, campo, escrita): # escreve no entry, definindo qual será o entry e o que será escrito
        campo.config(state=tk.NORMAL)    # Habilita a edição temporariamente
        campo.delete(0, tk.END)          # Apaga todo o texto do Entry
        campo.insert(0, escrita)         # Escreve no entry
        campo.config(state=tk.DISABLED)  # Bloqueia a edição novamente
        
        
    def rolar(self, event): #definição da ação de rolagem 
        self.canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
        
caminho = os.getcwd() + r"\poppler-23.08.0\Library\bin" 
print(caminho)    
os.environ['PATH'] = caminho

inicialize = Separador()
inicialize.janela1()