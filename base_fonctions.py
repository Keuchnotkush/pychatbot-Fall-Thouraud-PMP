import os
def afficher_fichiers(repertoire):
    # Vérifier si le répertoire existe
    if not os.path.exists(repertoire):
        print("Le répertoire spécifié n'existe pas.")
        return

    # Parcourir tous les fichiers du répertoire
    for fichier in os.listdir(repertoire):
        # Vérifier si c'est un fichier
        if os.path.isfile(os.path.join(repertoire, fichier)):
            print(fichier)

def extract_names(repertoire):
    L = []
    for fichier in os.listdir(repertoire):      
        
        if "1" in fichier and fichier.removeprefix("Nomination_").removesuffix("1.txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix("1.txt"))
        elif "2" in fichier and fichier.removeprefix("Nomination_").removesuffix("2.txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix("2.txt"))
        elif "1" not in fichier and "2" not in fichier and fichier.removeprefix("Nomination_").removesuffix(".txt") not in L:
            L.append(fichier.removeprefix("Nomination_").removesuffix(".txt"))
    for e in L:
        print(e)


def transition(repertoire):
    for fichier in os.listdir(repertoire):
        with open(repertoire + "/" + fichier , "r" , encoding= 'utf8') as file:
            content = file.read()
        
        content = content.lower()

        with open(repertoire + "/" + "clean" + fichier , "w" , encoding= 'utf8') as file:
            file.write(content)

        os.rename(repertoire + "/" + "clean" + fichier , "cleaned/" + "clean" + fichier )


def propre(repertoire):
    L1 = []

    file  = open("{}.txt".format(repertoire),"r",encoding="utf8")
    lines = file.readlines()
    for n, line in enumerate(lines) :
        L1.append(str(line).replace("-", " "))
    file.close()
    for i in range(len(L1)):
        L1[i] = L1[i].replace("'", " ")
        L1[i] = L1[i].replace(".", "")
        L1[i] = L1[i].replace(",", "")
        L1[i] = L1[i].replace(";", "")
        L1[i] = L1[i].replace("!", "")
        L1[i] = L1[i].replace("?", "")
    
    f = open("{}.txt".format(repertoire),"w")
    j = 0
    for n, line in enumerate(lines) :
        f.write("{}\n".format(L1[j]))
        j += 1
    f.close() 
                    

        

