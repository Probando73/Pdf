from PyPDF2 import PdfReader
import pdfplumber

"""
pdf_file = open('resumen.pdf', 'rb')  # Apertura del archvo

lector_pdf = PdfReader(pdf_file)  # Lectura del Pdf

hojas = lector_pdf._get_page(2)  # Asigno el numero de la hoja

print(hojas.extract_text())  # Extraigo el texto
"""

import pdfplumber


def extraer_texto_pdf(archivo_pdf):
    texto = ""
    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto


# Ruta del archivo PDF
ruta_pdf = 'resumen.pdf'

# Extraer texto del PDF
try:
    texto_extraido = extraer_texto_pdf(ruta_pdf)
    print(texto_extraido)
except Exception as e:
    print(f"Error al extraer texto del PDF: {e}")
