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
    for fichier in os.listdir(drepertoire):
        if fichier.endswith(".txt"):
            fichiers.append(fichier)
    
    for i in fichiers:
        source_file = '{}/{}'.format(drepertoire,i)
        destination_file = '{}/{}'.format(frepertoire,i)

        with open(source_file, 'r') as f_source:
            with open(destination_file, 'w') as f_dest:
                for line in f_source:
                    f_dest.write(line)

        


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
                    

        

