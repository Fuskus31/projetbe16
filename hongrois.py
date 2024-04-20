import numpy as np
from scipy.optimize import linear_sum_assignment

from utils import ecrire_matrice_hongroistxt


def calculer_cout_etudiants(etudiants_dictionnaire, tableau_choix_possible, nombre_places_total):
    n = len(etudiants_dictionnaire)
    m = nombre_places_total  # Nombre total de places disponibles pour tous les sujets combinés
    cout = np.full((n, m), fill_value=n + 1)  # Initialise la matrice de coût avec une valeur élevée

    index_courant_sujet = 0
    for sujet, nb_places in tableau_choix_possible.items():
        for i, choix in enumerate(etudiants_dictionnaire.values()):
            try:
                rang_choix = choix.index(sujet) + 1
                for j in range(nb_places):  # Répéter le coût pour le nombre de places disponibles
                    cout[i, index_courant_sujet + j] = rang_choix
            except ValueError:
                pass  # Le coût reste élevé si le sujet n'est pas dans les préférences de l'étudiant
        index_courant_sujet += nb_places

    ecrire_matrice_hongroistxt(cout)
    print("Matrice des Couts :\n", cout)  # affiche la matrice des couts pour l'algorithme hongrois
    return cout


def allouer_sujets(etudiants_dictionnaire, tableau_choix_possible):
    burgers = {sujet: tableau_choix_possible[sujet] for choix in etudiants_dictionnaire.values() for sujet in
               choix}
    nombre_places_total = sum(tableau_choix_possible.values())

    cout = calculer_cout_etudiants(etudiants_dictionnaire, tableau_choix_possible, nombre_places_total)
    etudiants = list(etudiants_dictionnaire.keys())

    row_ind, col_ind = linear_sum_assignment(cout)  # Appliquer l'algorithme hongrois

    allocations = {}
    for i, choix in enumerate(col_ind):
        etudiant = etudiants[row_ind[i]]
        # Trouver le sujet correspondant à cet index de choix
        total_places_jusqu_a_present = 0
        for sujet, nb_places in tableau_choix_possible.items():
            if total_places_jusqu_a_present <= choix < total_places_jusqu_a_present + nb_places:
                # Calculer le rang de préférence basé sur l'index original dans les choix de l'étudiant
                rang_choix = etudiants_dictionnaire[etudiant].index(sujet) + 1
                allocations[etudiant] = (sujet, rang_choix)
                break
            total_places_jusqu_a_present += nb_places

    return allocations
