import base_fonctions, TF
repertoire = "speeches"
# fonctions.afficher_fichiers(repertoire)
print("== Menu Principale ==|\n")
print("Que souhaitez vous faire ? (Saisir le nombre entre parenthèse)") 
print("- Pour clean le speeches (0)")
print("- Voir le TF (1)")
print("- Voir l'IDF (2)")
print("- Voir le TF-IDF (3)")
print("- Afficher la liste des mots les moins importants dans le corpus de documents (4)")
print("- Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé (5)")
print("- Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac (6)")
print("- Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois (7)")
print("- Indiquer le premier président à parler du climat et/ou de l’écologie (8)")
print("- Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués (9)")
print("- Pour afficher la liste des noms et prénoms des présidents (10)")
print("- Pour extraire les noms des présidents à partir des noms des fichiers texte fournis (11)")
print("généralement il faut écrire 'cleaned' pour les répértoires *")

ask = int(input("Saisie : "))
while ask > 11 or ask < 0:
    ask = int(input("Saisie : "))

if ask == 0:
    x = str(input("Saisir le nom du répértoire à copier : "))
    y = str(input("Saisir le nom du répértoire à coller : "))
    base_fonctions.transition(x,y)
    base_fonctions.propre(y)
    print("Les speeches sont nétoyés !")
elif ask == 1:
    x = str(input("Saisir le nom du fichier (avec le .txt) "))
    print(TF.tf("speeches",x))
elif ask == 2:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.calcul_score_idf(x))
elif ask == 3:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.calcul_matrice_tf_idf(x))
elif ask == 4:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.mots_moins_importants(x))
elif ask == 5:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.mots_plus_importants(x))
elif ask == 6:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.mots_plus_repetes_president(x))
elif ask == 7:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.president_parle_de_mot(x))
elif ask == 8:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.premier_president_parle_de_mot(x))
elif ask == 9:
    x = str(input("Saisir le nom du répértoire "))
    print(TF.mots_evoques_par_tous_presidents(x))
elif ask == 10:
    x = str(input("Saisir le nom du répértoire "))
    base_fonctions.prenomforname(x)
elif ask == 11:
    x = str(input("Saisir le nom du répértoire "))
    base_fonctions.extract_names(x)
    
else:
    print("erreur, veuillez relancer le programme..")