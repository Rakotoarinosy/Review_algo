def lire_extension(element):
    element = element.split(".")
    if len(element) > 1:
        return element[-1]
    return None

def get_extension(extention,definitions):
    for d in definitions:
        print(d[0])
        if d[0].lower() == extention.lower():
            return d[1]
    return None

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document World"),
                         ("exe", "Executable"),
                         ("txt", "Document Texte"),
                         ("jpeg", "Image JPEG")
                        )

for fichier in fichiers:
    ext = lire_extension(fichier)
    if ext:
        definition = get_extension(ext,definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(f"{fichier } ({definition})")
        
