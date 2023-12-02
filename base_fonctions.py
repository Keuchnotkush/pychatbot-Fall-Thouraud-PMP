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
    L2 = []
    for fichier in os.listdir(repertoire):
        L2.append(fichier)
    for i in range(len(L2)):
        L2[i] = L2[i].replace(".txt","")
        L2[i] = L2[i].replace("0","")
        L2[i] = L2[i].replace("1","")
        L2[i] = L2[i].replace("2","")
        L2[i] = L2[i].replace("3","")
        L2[i] = L2[i].replace("4","")
        L2[i] = L2[i].replace("5","")
        L2[i] = L2[i].replace("6","")
        L2[i] = L2[i].replace("7","")
        L2[i] = L2[i].replace("8","")
        L2[i] = L2[i].replace("9","")
        L2[i] = L2[i].replace("Nomination_","")
    
    L3 = []
    for nom in L2:
        if nom not in L3:
            L3.append(nom)
            print(nom)

def prenomforname(repertoire):
    
    L1 = ["Valéry Giscard dEstaing","Jacques Chirac","Nicolas Sarkozy","François Mitterrand","François Hollande","Emanuelle Macron"]
    L2 = []
    for fichier in os.listdir(repertoire):
        L2.append(fichier)
    for i in range(len(L2)):
        L2[i] = L2[i].replace(".txt","")
        L2[i] = L2[i].replace("0","")
        L2[i] = L2[i].replace("1","")
        L2[i] = L2[i].replace("2","")
        L2[i] = L2[i].replace("3","")
        L2[i] = L2[i].replace("4","")
        L2[i] = L2[i].replace("5","")
        L2[i] = L2[i].replace("6","")
        L2[i] = L2[i].replace("7","")
        L2[i] = L2[i].replace("8","")
        L2[i] = L2[i].replace("9","")
        L2[i] = L2[i].replace("Nomination_","")
    
    L3 = []
    for nom in L2:
        if nom not in L3:
            L3.append(nom)
            for prenom in L1:
                if nom in prenom:
                    print(prenom)
        


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
                    

        

