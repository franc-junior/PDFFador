# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def exibir_parte_da_imagem():
#     # Carregue a imagem original
#     imagem_original = Image.open("botao.png")

#     # Defina as coordenadas da área que você deseja exibir (recortar)
#     x1, y1, x2, y2 = 100, 100, 300, 300  # Por exemplo, coordenadas para recortar uma área retangular

#     # Recorte a parte desejada da imagem
#     imagem_recortada = imagem_original.crop((x1, y1, x2, y2))

#     # Converta a imagem recortada para ImageTk.PhotoImage
#     imagem_tk = ImageTk.PhotoImage(imagem_recortada)

#     # Exiba a imagem recortada em um Canvas
#     canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)
#     canvas.image = imagem_tk  # Mantenha uma referência para a imagem
#     canvas.config(scrollregion=canvas.bbox("all"))  # Atualize a região de rolagem do Canvas

# root = tk.Tk()
# root.geometry("400x400")

# frame = ttk.Frame(root)
# frame.pack(fill=tk.BOTH, expand=True)

# # Crie um Canvas com uma barra de rolagem vertical
# canvas = tk.Canvas(frame)
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# canvas.configure(yscrollcommand=scrollbar.set)

# exibir_parte_da_imagem_button = ttk.Button(root, text="Exibir Parte da Imagem", command=exibir_parte_da_imagem)
# exibir_parte_da_imagem_button.pack()

# root.mainloop()

import tkinter as tk
from tkinter import Scrollbar, Canvas

def rolar(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

root = tk.Tk()
root.geometry("400x300")

canvas = Canvas(root)
canvas.pack(fill="both", expand=True)

scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Adicione algum conteúdo ao Canvas
for i in range(50):
    canvas.create_text(20, i * 20, text=f"Item {i + 1}")

# Ative a rolagem com a roda do mouse
canvas.bind_all("<MouseWheel>", rolar)

root.mainloop()