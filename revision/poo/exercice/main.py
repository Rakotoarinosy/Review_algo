# creer class Question:
# propriete (titre:str, choix[], bonne_reponse:str)
# poser_question()

class Question:
    def __init__(self,titre,choix,bonne_reponse):
        self.titre = titre
        self.choix =choix
        self.bonne_reponse = bonne_reponse
        
    def poser_question(self):
        print("QUESTION")
        print(" " + self.titre)
        for i in range(len(self.choix)):
            print(f"    {i+1} - {self.choix[i]}")
            
        print()
        resultat_reponse_correcte = False
        reponse_int = Question.demander_reponse_numerique_utilisateur(1,len(self.choix)) # type: ignore
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower(): # type: ignore
            print("Bonne réponse")
            resultat_reponse_correcte = True
        else:
            print("Mauvaise réponse")
        print()
        return resultat_reponse_correcte
        
    def demander_reponse_numerique_utilisateur(min,max):
        reponse_str = input(f"Votre réponse entre {min} et {max} : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max: # type: ignore
                return reponse_int
            else:
                print(f"ERREUR : Vous devez rentrer un nombre entre {min} et {max}")
                return Question.demander_reponse_numerique_utilisateur(min, max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
            Question.demander_reponse_numerique_utilisateur(min,max)  # type: ignore
    

# creer class Questionnaire:
#       - questions     - (Question)
#       - lancer()

class Questionnaire:
    def __init__(self,questions):
        self.questions = questions
    
    def lancer_questionnaire(self):
        score = 0
        for question in self.questions:
            if question.poser_question():
                score += 1
        print(f"Score finale : {score} / {len(self.questions)}")
        

questions = (
                 Question("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"),"Paris"),
                 Question("Quelle est la capitale de l'Italie ?",("Rome","Venise","Pise","Florence"),"Rome")
                )

questonnaire = Questionnaire(questions)
questonnaire.lancer_questionnaire()