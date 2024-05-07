
'''NB_QUESTION = 4
def questionnaire():
    for i in range(0,NB_QUESTION):
        print(f"Question {i+1}: Quelle est la capapitale de la France?")
        a = "Marseille"
        b = "Nice"
        c = "Paris"
        d = "Nantes"
        print(f" (a) {a}\n", f"(b) {b}\n",f"(c) {c}\n", f"(d) {d}\n")
        reponse = input("Quelle est la bonne réponse: ")
        print()
        if reponse == "c":
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")

questionnaire()'''

def poser_question(question, r1, r2, r3, r4, choix_reponse):
    global score
    print("QUESTION")
    print(" " + question)
    print(" (a)", r1)
    print(" (b)", r2)
    print(" (c)", r3)
    print(" (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    
    if reponse == choix_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise répnse")
        
    print()

score = 0
poser_question("Quelle est la capapitale de la France","Marseille","Nice","Paris","Nantes","c")
poser_question("Quelle est la capapitale de l'Italie","Rome","Venise","Pise","Florence","a")

print("Score final :", score, "/ 2")