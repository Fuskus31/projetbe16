import os
from itertools import combinations
from affectationSPA import construct_ressources_list, lancement_testaffection_bruteforce
from hongrois import allouer_sujets
from student_project_allocation import allocate_subjects_spa
from readCsvMoodle import readCsvGenerateMoodle, lire_csv_et_generer_dictionnaires
from utils import assign_random, verification_nballocation_nbsujet, assign_choice
import time


def allocation_heuristique(dictionnaire_student_project, tableau_choix_possible):
    allocation_resultat = {}
    projets_attribues = {key: 0 for key in tableau_choix_possible.keys()}  # Suivi des projets attribués

    for etudiant, preferences in dictionnaire_student_project.items():
        projet_attribue = False  # Indicateur pour savoir si un projet a été attribué à l'étudiant
        for index, projet in enumerate(preferences, start=1):  # Commencez l'indexation à 1 pour le rang
            if projets_attribues[projet] < tableau_choix_possible[projet]:
                # Attribuer le projet à l'étudiant et enregistrer le rang du choix
                allocation_resultat[etudiant] = (projet, index)  # Stockez le projet et son rang
                projets_attribues[projet] += 1
                projet_attribue = True
                break  # Passez à l'étudiant suivant une fois le projet attribué

        if not projet_attribue:
            # Si aucun projet n'a été attribué à l'étudiant (tous ses choix sont pleins)
            allocation_resultat[etudiant] = (None, None)  # L'étudiant n'obtient aucun projet

    return allocation_resultat


def start_heuristique(etudiants_projects, tableau_choix_possible):
    start_time = time.time()
    allocation = allocation_heuristique(etudiants_projects, tableau_choix_possible)
    end_time = time.time()

    cout_heuristique = 0
    compteur = 0
    # Chemin complet du sous-dossier
    chemin_sous_dossier = os.path.join(os.getcwd(), "resultatAllocation")

    # Chemin du fichier résultat dans le sous-dossier
    chemin_fichier_resultat = os.path.join(chemin_sous_dossier, "resultatHeuristique.txt")

    with open(chemin_fichier_resultat, 'w') as fichier:
        print("\nAllocations des sujets méthode heuristique :")
        for etudiant, (projet, rang) in allocation.items():
            if projet is not None:
                print(f"{etudiant} a été alloué au sujet {projet} qui correspond au choix numéro -> {rang}.")
                fichier.write(f"{etudiant} a été alloué au sujet {projet} qui correspond au choix numéro -> {rang}.\n")
                cout_heuristique += rang
                compteur = compteur + 1
            else:
                print(f"{etudiant} n'a pas été alloué à un projet car ses choix sont pleins.")
                fichier.write(f"{etudiant} n'a pas été alloué à un projet car ses choix sont pleins.\n")

        verification_nballocation_nbsujet(tableau_choix_possible, compteur)
        print(f"cout final de la méthode heuristique -> {cout_heuristique}\n")
        fichier.write(f"cout final de la méthode heuristique -> {cout_heuristique}\n")
        print("\nTous les choix possibles de projet :", tableau_choix_possible)
        fichier.write(f"\nTous les choix possibles de projet :, {tableau_choix_possible}\n")
        #print(etudiants_projects)
        fichier.write(f"{etudiants_projects}\n")
        print(f"Temps d'exécution heuristique: {end_time - start_time} secondes")


def start_brute_force(dictionnaire_student_project, tableau_choix_possible):
    clesEtudiant = list(dictionnaire_student_project.keys())
    ressources = construct_ressources_list(tableau_choix_possible)

    # cette ligne peut poser probleme ( grand nombre de combinaisons)
    cl = list(combinations(ressources, len(clesEtudiant)))
    start_time = time.time()
    lancement_testaffection_bruteforce(cl, dictionnaire_student_project, clesEtudiant)
    end_time = time.time()
    print(f"Temps d'exécution bruteforce: {end_time - start_time} secondes")

    #print("\nTous les choix possibles de projet :", tableau_choix_possible)
    print(dictionnaire_student_project)


def start_hongrois(dictionnaire_student_project, tableau_choix_possible):
    start_time = time.time()
    allocations = allouer_sujets(dictionnaire_student_project, tableau_choix_possible)
    end_time = time.time()

    print("\nAllocations des sujets méthode hongroise :")
    # Chemin complet du sous-dossier
    chemin_sous_dossier = os.path.join(os.getcwd(), "resultatAllocation")

    # Chemin du fichier résultat dans le sous-dossier
    chemin_fichier_resultat = os.path.join(chemin_sous_dossier, "resultatHongrois.txt")

    compteur = 0
    coutFinal = 0
    with open(chemin_fichier_resultat, 'w') as fichier:
        for etudiant, (sujet, choix) in allocations.items():
            print(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.")
            coutFinal = coutFinal + choix
            # Écrire chaque ligne dans le fichier
            fichier.write(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.\n")
            compteur = compteur + 1
        print(f"cout final de la méthode hongrois -> {coutFinal}\n")
        fichier.write(f"cout final de la méthode hongrois -> {coutFinal}\n")
        verification_nballocation_nbsujet(tableau_choix_possible, compteur)
        print("\nTous les choix possibles de projet :", tableau_choix_possible)
        fichier.write(f"Tous les choix possibles de projet  \n{tableau_choix_possible}\n")
        #print(dictionnaire_student_project)
        fichier.write(f"dictionnaire_student_project  {dictionnaire_student_project}\n")
        print(f"Temps d'exécution hongrois: {end_time - start_time} secondes\n")


def start_spa(dictionnaire_student_project, tableau_choix_possible):
    start_time = time.time()
    allocations = allocate_subjects_spa(dictionnaire_student_project, tableau_choix_possible)
    end_time = time.time()

    print("\nAllocations des sujets méthode allocation des projets étudiants :")
    # Chemin complet du sous-dossier
    chemin_sous_dossier = os.path.join(os.getcwd(), "resultatAllocation")

    # Chemin du fichier résultat dans le sous-dossier
    chemin_fichier_resultat = os.path.join(chemin_sous_dossier, "resultatSPA.txt")

    compteur = 0
    coutFinal = 0
    with open(chemin_fichier_resultat, 'w') as fichier:
        for etudiant, (sujet, choix) in allocations.items():
            print(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.")
            coutFinal = coutFinal + choix
            # Écrire chaque ligne dans le fichier
            fichier.write(f"{etudiant} a été alloué au sujet {sujet} qui correspond au choix numéro -> {choix}.\n")
            compteur = compteur + 1
        print(f"cout final de la méthode allocation des projets étudiants -> {coutFinal}\n")
        fichier.write(f"cout final de la méthode allocation des projets étudiants -> {coutFinal}\n")
        verification_nballocation_nbsujet(tableau_choix_possible, compteur)
        print("\nTous les choix possibles de projet :", tableau_choix_possible)
        fichier.write(f"Tous les choix possibles de projet  {tableau_choix_possible}\n")
        #print(dictionnaire_student_project)
        fichier.write(f"dictionnaire_student_project  {dictionnaire_student_project}\n")
        print("Temps d'exécution allocation des projets étudiants : ", end_time - start_time, " secondes\n")


''' ------------------------------------ '''


def main_test_developpeur(choix, algorithme,aleatoire_place,nbminplace,nbmaxplace):
    if choix == 1:
        # On utilise 2 dictionnaires pour les choix des étudiants et les places disponibles par projets.
        etudiants_burgers_dictionnaire, tableau_choix_possible = readCsvGenerateMoodle(
            'inputCSV/Election_du_Burger_Supr_me.csv')
        # {'DUGAT Vincent': ['Burger b1', 'Burger b2', 'Burger b3', 'Burger b5', 'Burger b6', 'Burger b7', 'Burger b8', 'Burger b10', 'Burger b4', 'Burger b9'],
        if aleatoire_place == 1:
            assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre min et max places
        else:
            assign_choice(tableau_choix_possible)
        # print("Tous les choix possibles de burgers :", tableau_choix_possible)
        # print(etudiants_burgers_dictionnaire)
        if algorithme == "fb":
            start_brute_force(etudiants_burgers_dictionnaire, tableau_choix_possible)
        elif algorithme == "hong":
            start_hongrois(etudiants_burgers_dictionnaire, tableau_choix_possible)
        elif algorithme == "spa":
            start_spa(etudiants_burgers_dictionnaire, tableau_choix_possible)
        else:
            start_heuristique(etudiants_burgers_dictionnaire, tableau_choix_possible)

    elif choix == 2:
        etudiants_projects, tableau_choix_possible = lire_csv_et_generer_dictionnaires('instance0.csv')
        if aleatoire_place == 1:
            assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre min et max places
        else:
            assign_choice(tableau_choix_possible)
        if algorithme == "fb":
            start_brute_force(etudiants_projects, tableau_choix_possible)
        elif algorithme == "hong":
            start_hongrois(etudiants_projects, tableau_choix_possible)
        elif algorithme == "spa":
            start_spa(etudiants_projects, tableau_choix_possible)
        else:
            start_heuristique(etudiants_projects, tableau_choix_possible)


''' ------------------------------------ '''
# Main du projet


def start_all(etudiants_dictionnaire,tableau_choix_possible):
    #start_brute_force(etudiants_dictionnaire, tableau_choix_possible)
    start_hongrois(etudiants_dictionnaire, tableau_choix_possible)
    #start_spa(etudiants_dictionnaire, tableau_choix_possible)
    start_heuristique(etudiants_dictionnaire, tableau_choix_possible)


def main(developpeur_or_client, choix, algorithme,aleatoire_place,nbminplace,nbmaxplace):
    print("\n" * 10)

    # Affiche l'heure actuelle
    print(time.strftime("%H:%M:%S"))

    if developpeur_or_client == 0:
        main_test_developpeur(choix, algorithme,aleatoire_place,nbminplace,nbmaxplace)
    else:
        if choix == 1:
            filename = 'inputCSV/Election_du_Burger_Supr_me.csv'
            etudiants_dictionnaire, tableau_choix_possible = readCsvGenerateMoodle(filename)
            if aleatoire_place == 1:
                assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre 4 et 10 places par projet
            else:
                assign_choice(tableau_choix_possible)
            start_all(etudiants_dictionnaire,tableau_choix_possible)
        elif choix == 2:
            filename = 'inputCSV/instance0.csv'
            etudiants_dictionnaire, tableau_choix_possible = lire_csv_et_generer_dictionnaires(filename)
            if aleatoire_place == 1:
                assign_random(tableau_choix_possible, nbminplace, nbmaxplace)  # entre 4 et 10 places par projet
            else:
                assign_choice(tableau_choix_possible)
            start_all(etudiants_dictionnaire, tableau_choix_possible)


# Vous pouvez test 2 fichiers celui du moodle ou de l'instanceGenerer (lancer le fichier spa_instance) pour générer
if __name__ == '__main__':
    # Par projet il faut définir une place entre 5 et 7 par exemple ( aléatoire )
    aleatoire_place = 1 # 0 = choisir à la main les places et 1 choisir les places entre nbmin et nbmaxplace aléatoire
    nbminplace = 3 #mettre 3 et 4 recommander
    nbmaxplace = 4
    developpeur_or_client = 1  # 0 si pour afficher cas par cas pour le développeur dans la console sinon 1 pour client
    choix = 1  # 1 = fichier moodle 2 = instanceGénérer
    algorithme = "osef"  # "fb" ou "hong" ou "spa" ou heuristique ( ou "osef" pas d'importance si on lance tous les algos)
    main(developpeur_or_client, choix, algorithme,aleatoire_place,nbminplace,nbmaxplace)
