from bs4 import BeautifulSoup

# Lecture des donné HTML
f = open("recette.html", "r")
html_content = f.read()
f.close()
soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
paragraphe = soup.find("p")
image = soup.find("img")


print("Titre de la page HTML : ", titre_h1.text) # type: ignore
print()
print("Paragraphe de la page HTML : ", paragraphe.text) # type: ignore
print()
print("Image de la page HTML : ", image["src"]) # type: ignore