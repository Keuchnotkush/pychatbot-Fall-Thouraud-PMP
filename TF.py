import os
import math
def tf(repertoire):
    L1 = []

    file  = open("speeches\{}.txt".format(repertoire),"r",encoding="utf8")
    lines = file.readlines()
    for n, line in enumerate(lines) :
        L1.append(str(line))
    file.close()

    L2 = []
    for i in range(len(L1)):
        L3 = L1[i].split()
        for j in range(len(L3)):
            L2.append(L3[j])
    
    words = L2
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def calculate_idf(corpus_directory):
    document_frequencies = {}

    total_documents = 0

    for filename in os.listdir(corpus_directory):
        file_path = os.path.join(corpus_directory, filename)

        if os.path.isfile(file_path):
            total_documents += 1

            with open(file_path, 'r') as file:
                content = file.read()

                words = content.split()

                for word in word_set:
                    if word in document_frequencies:
                        document_frequencies[word] += 1
                    else:
                        document_frequencies[word] = 1

    idf_scores = {}
    for word, frequency in document_frequencies.items():
        idf_scores[word] = math.log(total_documents / frequency)

    return idf_scores

def calcul_occurrences(chaine):
    mots = chaine.split()
    occurrences = {}
    for mot in mots:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return occurrences


def calcul_score_idf(repertoire):
    nb_documents = 0
    mots_documents = {}
    score_idf = {}
    
    for fichier in os.listdir(repertoire):
        nb_documents += 1
        with open(os.path.join(repertoire, fichier), 'r') as f:
            contenu = f.read()
            mots = contenu.split()
            for mot in set(mots):
                if mot in mots_documents:
                    mots_documents[mot] += 1
                else:
                    mots_documents[mot] = 1
    
    for mot, nb_occurrences in mots_documents.items():
        score_idf[mot] = math.log(nb_documents / nb_occurrences)
    
    return score_idf

def calcul_matrice_tf_idf(repertoire):
    score_idf = calcul_score_idf(repertoire)
    matrice_tf_idf = []
    mots_uniques = set()
    
    for fichier in os.listdir(repertoire):
        with open(os.path.join(repertoire, fichier), 'r') as f:
            contenu = f.read()
            occurrences = calcul_occurrences(contenu)
            mots_uniques.update(occurrences.keys())
            matrice_tf_idf.append(occurrences)
    
    mots_uniques = sorted(list(mots_uniques))
    
    for i in range(len(matrice_tf_idf)):
        for mot in mots_uniques:
            tf = matrice_tf_idf[i].get(mot, 0)
            idf = score_idf.get(mot, 0)
            matrice_tf_idf[i][mot] = tf * idf
    
    return matrice_tf_idf








def mots_moins_importants(repertoire):
    fichiers = []
    motused = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for i in range(len(fichiers)):
        res = calcul_matrice_tf_idf(repertoire)
        for mot in res:
            print(mot, res[mot])
            if 0 == res[mot]:
                if mot in motused:
                    variabledechet = 0
                else: 
                    motused.append(mot)
        
    
    textoutput = "Les mots les moins important sont : {}".format(motused)
    return textoutput
    
    return mots_moins_importants







def mots_plus_importants(repertoire):
    
    return mots_plus_importants











def mots_plus_repetes_president(repertoire):
    fichiers_chirac = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt") and "Chirac" in fichier:
            fichiers_chirac.append(fichier)
    for i in range(len(fichiers_chirac)):
        endroit = fichiers_chirac[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        L1.append(contenux)   
    
    max = 0
    for i in range(len(L1)):
        res = calcul_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if max <= res[mot]:
                max = res[mot]
                motofficiel = mot
    textoutput = "Le mot '{}' est répété {} fois chez Chirac".format(motofficiel,max)
    return textoutput
    




    


    

def president_parle_de_mot(repertoire):
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        contenux = contenux.replace("nations", "nation")
        L1.append(contenux)   
    
    max = 0
    savepres = 0
    for i in range(len(L1)):
        res = calcul_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if mot == "nation":
                if max <= res[mot]:
                    max = res[mot]
                    savepres = i 
        
    
    presi = fichiers[savepres]
    presi = presi.removeprefix("Nomination_").removesuffix(".txt")
    textoutput = "Le président '{}' est celui qui a cité le plus de fois le mot 'Nation' , il l'a répété {} fois".format(presi,max)
    return textoutput

def premier_president_parle_de_mot(repertoire):
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        contenux = contenux.replace("climats", "climat")
        contenux = contenux.replace("écologies", "écologie")
        contenux = contenux.replace("écologie", "climat")
        L1.append(contenux)   
    
    max = 0
    savepres = 0
    for i in range(len(L1)):
        res = calcul_occurrences(L1[i])
        
        for mot in res:
            #print(mot, res[mot])
            if mot == "climat":
                if max <= res[mot]:
                    max = res[mot]
                    savepres = i 
        
    
    presi = fichiers[savepres]
    presi = presi.removeprefix("Nomination_").removesuffix(".txt")
    textoutput = "Le président '{}' est celui qui parle le plus du climat / écologie , il l'a répété {} fois".format(presi,max)
    return textoutput

def mots_evoques_par_tous_presidents(repertoire):
    fichiers = []
    L1 = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    for i in range(len(fichiers)):
        endroit = fichiers[i]
        with open("{}\\{}".format(repertoire,endroit), 'r') as file:
            contenu = file.read()
        contenux = contenu.replace("\n", " ")
        contenux = contenux.lower()
        L1.append(contenux)   
    
    motscheck = True
    motsdit = []
    for i in range(len(L1)):
        res = calcul_occurrences(L1[i])
        
        for mot1 in res:
            for j in range(len(L1)):
                if j != len(L1)-1:
                    res = calcul_occurrences(L1[j+1])
                    
                    for mot2 in res:
                        if mot1 != mot2:
                            motscheck = False
                        else:
                            motscheck = True
                            break
                    if motscheck == False:
                        break
                    else:
                        if mot1 in motsdit:
                            variablebouchetrou = 0
                        else:
                            motsdit.append(mot1)
            if j == len(L1):
                if motscheck == True:
                    break

            #print(mot, res[mot])
        
    
    textoutput = "Tout le sprésidents on au moins cité 1 fois ces mots : {}".format(motsdit)
    return textoutput
