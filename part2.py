import os, math
import TF
punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
MotPoubelle = ["comment","quoi","pourquoi","dire","porte"]

def token(sentence):
    L = []
    n = ""
    for o in sentence.split(" "):
        if all(z not in punc for z in o):
            n += o + " "
    n = n.lower()
    L = n.split(" ")
    return L


def identify(sentence , repertoire):
    listu = token(sentence)
    keep = []
    for fichier in os.listdir(repertoire):
        with open(os.path.join(repertoire, fichier), 'r') as f:
            contenu = f.read()
            mots = contenu.split()

    for word in listu:
        if word in mots and word not in keep:
            keep.append(word)
    return keep

def questtfidf(question):

    quest = ""
    for e in token(question):
        quest += e + " "
    occMots = TF.calcul_occurrences(quest)
    result = TF.calcul_score_idf("cleaned")
    L = {}
    for i in result.keys():
        if i in occMots:
            x = result[i] * occMots[i]
            L[i] = x
        else:
            result[i] = 0
    return L

def motImportant(question):
    dicquest = questtfidf(question)
    max = 0
    word = ""
    for i in dicquest:
        if i not in MotPoubelle:
            if max <= dicquest[i]:
                max = dicquest[i]
                word = i
    return word

def MotPertinentViaFichier(word):
    fichiers = []
    for fichier in os.listdir("cleaned"):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    dico = TF.calcul_matrice_tf_idf("cleaned")
    nomfichier = ""
    max = 0
    for i in range(len(fichiers)):
        if dico[word][i] > max:
            max = dico[word][i]
            nomfichier = fichiers[i]
    return nomfichier

def reponseViaFile(word):
    file = MotPertinentViaFichier(word)
    L1 = []

    file  = open("cleaned\\{}".format(file),"r",encoding="utf8")
    lines = file.readlines()
    for n, line in enumerate(lines) :
        L1.append(str(line).replace("\n", " "))
    file.close()
    reponse = ""
    for i in range(len(L1)):
        if word in L1[i]:
            reponse = L1[i]
            break
    
    reponse = reponse.replace(" l ", " l'")
    reponse = reponse.replace(" c ", " c'")
    reponse = reponse.replace(" s ", " s'")
    return reponse

def generationentry(question):
    question = question.replace("'", " ")
    question = question.replace(".", "")
    question = question.replace(",", "")
    question = question.replace(";", "")
    question = question.replace("!", "")
    question = question.replace("?", "")
    question = question.replace("-", " ")
    question = question.lower()
    question_starters = {
 "comment": "Après analyse,",
 "pourquoi": "Car,",
 "peux tu": "Oui, bien sûr!"
}
    for i in question_starters:
        if i in question:
            return question_starters[i]
            