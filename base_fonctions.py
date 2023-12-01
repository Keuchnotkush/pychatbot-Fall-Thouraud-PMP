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


def transition(drepertoire,frepertoire):
    
    fichiers = []
    L1 = []
    for fichier in os.listdir(drepertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for i in range(len(fichiers)):

        file  = open("{}\\{}".format(drepertoire,fichiers[i]),"r",encoding="utf8")
        lines = file.readlines()
        for n, line in enumerate(lines) :
            L1.append(str(line).replace("\n", " "))
        file.close()

        try:
            # Tentative d'ouverture du fichier en mode écriture
            with open("{}\\{}".format(frepertoire,fichiers[i]), 'w') as file:
                pass
            print("Le fichier {} a été créé avec succès.".format(fichiers[i]))
        except FileExistsError:
            print("Le fichier existe déjà.")
        f = open("{}\\{}".format(frepertoire,fichiers[i]),"w")
        for n, line in enumerate(lines) :
            f.write("{}\n".format(L1[n]))
        f.close() 
        


def propre(repertoire):
    fichiers = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for j in range(len(fichiers)):
    
        L1 = []

        file  = open("{}\\{}".format(repertoire,fichiers[j]),"r",encoding="utf8")
        lines = file.readlines()
        for n, line in enumerate(lines) :
            L1.append(str(line).replace("\n", " "))
        file.close()
        for i in range(len(L1)):
            L1[i] = L1[i].replace("'", " ")
            L1[i] = L1[i].replace(".", "")
            L1[i] = L1[i].replace(",", "")
            L1[i] = L1[i].replace(";", "")
            L1[i] = L1[i].replace("!", "")
            L1[i] = L1[i].replace("?", "")
            L1[i] = L1[i].replace("-", " ")
            L1[i] = L1[i].lower()
        
        f = open("{}\\{}".format(repertoire,fichiers[j]),"w")
        for n, line in enumerate(lines) :
            f.write("{}\n".format(L1[n]))

        f.close() 
                    

        

