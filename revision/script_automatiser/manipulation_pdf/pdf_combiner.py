# PyPDF2
# COMBINER

# lire des PDF extraire le texte
# Ecrire des PDF
# - Combiner
# - Rotation, superposer
# - Ne peut pas : rajouter du texte ou des images
import os
from PyPDF2 import PdfWriter,PdfReader

base_path = "/home/fehizoro/Bureau/Review_algo/revision/script_automatiser/manipulation_pdf"

contenu_sortie = PdfWriter()

pdf_presentation = os.path.join(base_path,"presentation.pdf")
pdf_recap = os.path.join(base_path,"recap.pdf")

fichier_pdf_presentation = open(pdf_presentation, 'rb')
fichier_pdf_recap = open(pdf_recap, 'rb')

reader_presentation = PdfReader(fichier_pdf_presentation)
reader_recap = PdfReader(fichier_pdf_recap)

print("Nombre de pages du fichier récap : " + str(len(reader_recap.pages)))

# Ajouter les pages du fichier de présentation
for page in reader_presentation.pages:
    contenu_sortie.add_page(page)

# Ajouter les pages du fichier de récap
for page in reader_recap.pages:
    contenu_sortie.add_page(page)


fichier_sortie = open("fichier_sortie.pdf", "wb")
contenu_sortie.write(fichier_sortie)

fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()