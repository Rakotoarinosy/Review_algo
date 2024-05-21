# creer class Question:
# propriete (titre:str, reponse:[], bonne_reponse:str)
# poser_question()

# creer class Questionnaire:
#       - questions     - (Question)
#       - lancer()

def demander_reponse_numerique_utilisateur(min,max):
    reponse_str = input(f"Votre réponse entre {min} et {max} : ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        
        print(f"ERREUR : Vous devez rentrer un nombre entre {min} et {max}")
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    demander_reponse_numerique_utilisateur(min,max) 

        
def poser_question(question):
    print(" " + question[0])
    choix = question[1]
    for i in range(len(choix)):
        print(f"    {i+1} - {choix[i]}")
        
    print()
    resultat_reponse_correcte = False
    reponse_int = demander_reponse_numerique_utilisateur(1,len(choix))
    if choix[reponse_int-1].lower() == question[2].lower(): # type: ignore
        print("Bonne réponse")
        resultat_reponse_correcte = True
    else:
        print("Mauvaise réponse")
    print()
    return resultat_reponse_correcte


def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print(f"Score finale : {score} / {len(questionnaire)}")

question1 = ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris")
question2 = ("Quelle est la capitale de l'Italie ?",("Rome","Venise","Pise","Florence"),"Rome")

questionnaire = (
                 ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris"),
                 ("Quelle est la capitale de l'Italie ?",("Rome","Venise","Pise","Florence"),"Rome")
                )

lancer_questionnaire(questionnaire)