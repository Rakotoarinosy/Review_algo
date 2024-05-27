# EXTRAIRE LE TEXTE DES FICHIERS PDF
from PyPDF2 import PdfWriter,PdfReader

f = open("recap.pdf", "rb")
reader = PdfReader(f)

page0 = reader.pages[0]
texte = page0.extract_text()

print(texte)

f.close()