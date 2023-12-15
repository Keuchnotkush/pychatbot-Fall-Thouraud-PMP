import os, TF, math

punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''

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
    ListeMots = token(question)
    
    quest = question.replace("'", " ")
    quest = quest.replace(".", "")
    quest = quest.replace(",", "")
    quest = quest.replace(";", "")
    quest = quest.replace("!", "")
    quest = quest.replace("?", "")
    quest = quest.replace("-", " ")
    quest = quest.lower()
    occMots = TF.calcul_occurrences(quest)

    matrice_tf_idf = []
    mots_uniques = set()
    nbfichier = 0
    for fichier in os.listdir("cleaned"):
        nbfichier += 1
        with open(os.path.join("cleaned", fichier), 'r',encoding="utf8") as f:
            contenu = f.read()
            occurrences = TF.calcul_occurrences(contenu)
            mots_uniques.update(occurrences.keys())
            matrice_tf_idf.append(occurrences)
    
    mots_uniques = sorted(list(mots_uniques))
    
    L2 = []
    for fichier in os.listdir("cleaned"):
        L2.append(fichier)
    result = {}
    for i in range(len(mots_uniques)):
        L20 = []
        for j in range(len(L2)):
            
            idfscore = TF.calcul_score_idf("cleaned")
            tfscore = TF.tf(str("cleaned"),str(L2[j]))
            
            if mots_uniques[i] in tfscore:
                L20.append(idfscore[mots_uniques[i]] * tfscore[mots_uniques[i]])
        
        result[mots_uniques[i]] = L20
    #return result

    L2 = {}
    for i in range(len(occMots)):
        if occMots[i] in result:
            print()