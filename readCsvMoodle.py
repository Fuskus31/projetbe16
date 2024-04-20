import csv


def readCsvGenerateMoodle(csv_file):
    etudiants_burgers = {}
    all_burgers = {}  # Dictionnaire pour stocker tous les choix possibles de burgers

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            nom_etudiant = row["Nom complet"]
            burgers = []

            for burger, choix in row.items():
                if "Burger" in burger and choix.isdigit():
                    burgers.append((int(choix), burger))
                    if burger not in all_burgers:
                        all_burgers[burger] = -1  # Initialiser à -1

            burgers.sort(key=lambda x: x[0])
            etudiants_burgers[nom_etudiant] = [burger[1] for burger in burgers]

    with open('inputCSV/burgerVisuInutile.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nom étudiant", "Burgers choisis"])
        for nom_etudiant, choix_burgers in etudiants_burgers.items():
            writer.writerow([nom_etudiant, ', '.join(choix_burgers)])

    return etudiants_burgers, all_burgers


def lire_csv_et_generer_dictionnaires(chemin_fichier):
    # Dictionnaire pour stocker les préférences des étudiants
    dictionnaire_projets = {}
    # Dictionnaire pour stocker le nombre de places par projet
    places_par_projet = {}

    with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            nom_complet = ligne.pop('Nom complet')
            # Initialiser les places à 0 pour chaque projet lors de la première occurrence
            for projet in ligne:
                if projet not in places_par_projet:
                    places_par_projet[projet] = 0
            # Convertir les valeurs en entiers, sauf les -1 qui restent inchangés
            projets_ordonnes = {int(v): k for k, v in ligne.items() if v != '-1'}
            # Trier les projets par note (la clé) en ordre croissant et récupérer les noms des projets
            projets_ordonnes = [projets_ordonnes[k] for k in sorted(projets_ordonnes)]
            dictionnaire_projets[nom_complet] = projets_ordonnes

    return dictionnaire_projets, places_par_projet



