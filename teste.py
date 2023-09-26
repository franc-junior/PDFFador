import PyPDF2

# Abra o arquivo PDF original
with open(r"D:\Estudo\2folhas.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Crie dois objetos PdfWriter para os dois PDFs resultantes
    pdf_writer1 = PyPDF2.PdfWriter()
    pdf_writer2 = PyPDF2.PdfWriter()

    # Adicione as páginas desejadas aos respectivos PDFs
    for page_number, page in enumerate(pdf_reader.pages):
        if page_number < 1:
            pdf_writer1.add_page(page)
        else:
            pdf_writer2.add_page(page)

    # Salve os dois PDFs resultantes
    with open("parte1.pdf", "wb") as output_file1:
        pdf_writer1.write(output_file1)

    with open("parte2.pdf", "wb") as output_file2:
        pdf_writer2.write(output_file2)

##############################################

import math

numero_ponto_flutuante = 3.7  # Substitua isso pelo seu número de ponto flutuante
numero_inteiro_arredondado = math.ceil(numero_ponto_flutuante)

print(numero_inteiro_arredondado)