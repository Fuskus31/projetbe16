def allocate_subjects_spa(students, subjects):
    # Convertir les préférences en ensembles pour une recherche plus rapide
    preferences = {subject: set() for subject in subjects}
    for student, prefs in students.items():
        for pref in prefs:
            if pref in preferences:
                preferences[pref].add(student)

    # Initialiser les sujets avec un nombre de places disponibles
    subjects_available = subjects.copy()

    # Dictionnaire pour suivre les sujets attribués à chaque étudiant
    subjects_assigned = {}

    # Tant qu'il reste des sujets non attribués et des étudiants non attribués
    while subjects_available:
        # Choisir un sujet disponible
        subject = next(iter(subjects_available))

        # Vérifier si le sujet a encore des places disponibles
        if subjects_available[subject] == 0:
            del subjects_available[subject]
            continue

        # Obtenir les étudiants qui préfèrent ce sujet
        students_preferring_subject = preferences[subject]

        # Parcourir les étudiants qui préfèrent ce sujet
        for student in students_preferring_subject:
            # Vérifier si l'étudiant est déjà attribué à un sujet
            if student not in subjects_assigned:
                # Si l'étudiant n'est pas encore attribué, lui attribuer le sujet
                subjects_assigned[student] = subject
                subjects_available[subject] -= 1

                # Vérifier si tous les étudiants ont un sujet
                if len(subjects_assigned) == len(students):
                    return subjects_assigned  # Sortir de la boucle si tous les étudiants ont un sujet attribué
                break
            else:
                # Si l'étudiant est déjà attribué, comparer les préférences
                current_subject = subjects_assigned[student]
                if subject in students[student] and subjects[subject] < subjects[current_subject]:
                    # L'étudiant préfère ce nouveau sujet à celui qui lui est actuellement attribué et il reste des places disponibles
                    subjects_available[current_subject] += 1
                    subjects_assigned[student] = subject
                    subjects_available[subject] -= 1
                    break

    return subjects_assigned

'''
# Exemple d'utilisation avec les données fournies
students = {'DUGAT Vincent': ['Burger b1', 'Burger b2', 'Burger b3', 'Burger b5', 'Burger b6', 'Burger b7', 'Burger b8', 'Burger b10', 'Burger b4', 'Burger b9'], 'VALLAT Ugo': ['Burger b1', 'Burger b10', 'Burger b2', 'Burger b8', 'Burger b6', 'Burger b7', 'Burger b9', 'Burger b4', 'Burger b3'], 'GREZIT Gabriel': ['Burger b1', 'Burger b2', 'Burger b3', 'Burger b9', 'Burger b10', 'Burger b8', 'Burger b6', 'Burger b7', 'Burger b5', 'Burger b4'], 'LANSALOT Eva': ['Burger b7', 'Burger b3', 'Burger b5', 'Burger b2', 'Burger b4', 'Burger b8', 'Burger b10', 'Burger b9', 'Burger b1', 'Burger b6'], 'MOUNIE Robin': ['Burger b10', 'Burger b9', 'Burger b8', 'Burger b7', 'Burger b6', 'Burger b5', 'Burger b4', 'Burger b3', 'Burger b2', 'Burger b1'], 'VIGOUROUX Loan': ['Burger b7', 'Burger b2', 'Burger b1', 'Burger b8', 'Burger b5', 'Burger b3', 'Burger b10', 'Burger b4', 'Burger b6', 'Burger b9'], 'CHERRAF Maxime': ['Burger b1', 'Burger b2', 'Burger b3', 'Burger b4', 'Burger b5', 'Burger b6', 'Burger b7', 'Burger b8', 'Burger b9', 'Burger b10'], 'DINI ALI Thaoumani': ['Burger b3', 'Burger b5', 'Burger b10', 'Burger b9', 'Burger b1', 'Burger b7', 'Burger b8', 'Burger b2', 'Burger b4', 'Burger b6'], 'YABAR Fabio': ['Burger b2', 'Burger b6', 'Burger b4', 'Burger b9', 'Burger b5', 'Burger b10', 'Burger b1', 'Burger b3', 'Burger b7', 'Burger b8'], 'GIRY Nicolas': ['Burger b3', 'Burger b1', 'Burger b2', 'Burger b10', 'Burger b8', 'Burger b6', 'Burger b7', 'Burger b4', 'Burger b5'], 'MIGNOTTE Julie': ['Burger b8', 'Burger b6', 'Burger b4', 'Burger b1', 'Burger b2', 'Burger b3', 'Burger b5', 'Burger b7', 'Burger b9', 'Burger b10'], 'MARTIN Benoit': ['Burger b7', 'Burger b3', 'Burger b2', 'Burger b5', 'Burger b8', 'Burger b9', 'Burger b10', 'Burger b4', 'Burger b6', 'Burger b1'], 'NDOYE Assane': ['Burger b1', 'Burger b9', 'Burger b10', 'Burger b8', 'Burger b5', 'Burger b3', 'Burger b2', 'Burger b7', 'Burger b6', 'Burger b4'], 'PINTI Anthony': ['Burger b6', 'Burger b10', 'Burger b2', 'Burger b1', 'Burger b8', 'Burger b5', 'Burger b9', 'Burger b3', 'Burger b7', 'Burger b4'], 'LUDWIG Corentin': ['Burger b10', 'Burger b2', 'Burger b3', 'Burger b5', 'Burger b7', 'Burger b8', 'Burger b9', 'Burger b1', 'Burger b6', 'Burger b4'], 'LAFORGE Mateo': ['Burger b1', 'Burger b2', 'Burger b5', 'Burger b8', 'Burger b6', 'Burger b7', 'Burger b9', 'Burger b10', 'Burger b4', 'Burger b3'], 'PIGANI Emanuele': ['Burger b10', 'Burger b1', 'Burger b7', 'Burger b6', 'Burger b3', 'Burger b5', 'Burger b2', 'Burger b8', 'Burger b9', 'Burger b4'], 'REGRAGUI MARTINS Marco': ['Burger b7', 'Burger b8', 'Burger b6', 'Burger b5', 'Burger b3', 'Burger b10', 'Burger b1', 'Burger b2', 'Burger b4', 'Burger b9'], 'RUMIN Raphael': ['Burger b2', 'Burger b6', 'Burger b9', 'Burger b10', 'Burger b3', 'Burger b7', 'Burger b5', 'Burger b4', 'Burger b8', 'Burger b1'], 'AIT MESSAOUD Tinhinane': ['Burger b8', 'Burger b4', 'Burger b1', 'Burger b10', 'Burger b9', 'Burger b7', 'Burger b5', 'Burger b6', 'Burger b3', 'Burger b2'], 'GINESTE Jarod': ['Burger b5', 'Burger b2', 'Burger b8', 'Burger b9', 'Burger b1', 'Burger b3', 'Burger b10', 'Burger b7', 'Burger b6', 'Burger b4'], 'SENGES Noa': ['Burger b8', 'Burger b7', 'Burger b2', 'Burger b1', 'Burger b10', 'Burger b9', 'Burger b6', 'Burger b5', 'Burger b4', 'Burger b3'], 'SANCHEZ Emilien': ['Burger b4', 'Burger b9', 'Burger b3', 'Burger b2', 'Burger b5', 'Burger b1', 'Burger b6', 'Burger b8', 'Burger b7'], 'MOUSSAOUI Salim': ['Burger b6', 'Burger b7', 'Burger b10', 'Burger b3', 'Burger b5', 'Burger b8', 'Burger b4', 'Burger b9', 'Burger b2', 'Burger b1'], 'RICHARD Jeremy': ['Burger b2', 'Burger b10', 'Burger b7', 'Burger b8', 'Burger b1', 'Burger b5', 'Burger b6', 'Burger b9', 'Burger b3', 'Burger b4'], 'CALMELS Oceane': ['Burger b2', 'Burger b7', 'Burger b8', 'Burger b4', 'Burger b10', 'Burger b9', 'Burger b6', 'Burger b3', 'Burger b5', 'Burger b1'], 'LAMALMI Daoud': ['Burger b8', 'Burger b7', 'Burger b10', 'Burger b5', 'Burger b9', 'Burger b6', 'Burger b4', 'Burger b1', 'Burger b2', 'Burger b3'], 'ZOUBAI Nabil': ['Burger b1', 'Burger b6', 'Burger b4', 'Burger b8', 'Burger b5', 'Burger b7', 'Burger b10', 'Burger b2', 'Burger b3'], 'KOUZMITCH Quentin': ['Burger b9', 'Burger b5', 'Burger b1', 'Burger b2', 'Burger b3', 'Burger b7', 'Burger b8', 'Burger b10', 'Burger b6', 'Burger b4'], 'DIALLO Mariama': ['Burger b1', 'Burger b3', 'Burger b8', 'Burger b4', 'Burger b2', 'Burger b6', 'Burger b7', 'Burger b5', 'Burger b9'], 'HANDWERK Hippolyte': ['Burger b5', 'Burger b1', 'Burger b2', 'Burger b8', 'Burger b7', 'Burger b10', 'Burger b6', 'Burger b3', 'Burger b4', 'Burger b9'], 'IVANOVA Alina': ['Burger b6', 'Burger b10', 'Burger b9', 'Burger b4', 'Burger b1', 'Burger b5', 'Burger b2', 'Burger b3', 'Burger b8', 'Burger b7'], 'JOSEPH Remy': ['Burger b1', 'Burger b2', 'Burger b3', 'Burger b7', 'Burger b5', 'Burger b9', 'Burger b8', 'Burger b4', 'Burger b10', 'Burger b6'], 'RADIONOVA Veronika': ['Burger b6', 'Burger b8', 'Burger b7', 'Burger b10', 'Burger b1', 'Burger b5', 'Burger b2', 'Burger b4', 'Burger b3', 'Burger b9'], 'JOSEPH Wilkens Marc Johnley': ['Burger b1', 'Burger b3', 'Burger b4', 'Burger b10', 'Burger b9', 'Burger b2', 'Burger b8', 'Burger b5', 'Burger b7', 'Burger b6'], 'ROSET Nathan': ['Burger b7', 'Burger b8', 'Burger b3', 'Burger b4', 'Burger b5', 'Burger b6', 'Burger b2', 'Burger b9', 'Burger b1', 'Burger b10'], 'AUTEFAGE-PINIES Ninon': ['Burger b7', 'Burger b3', 'Burger b1', 'Burger b8', 'Burger b6', 'Burger b5', 'Burger b10', 'Burger b4', 'Burger b2'], 'ZERKANI Yanis': ['Burger b7', 'Burger b8', 'Burger b5', 'Burger b6', 'Burger b10', 'Burger b3', 'Burger b4', 'Burger b9', 'Burger b1', 'Burger b2'], 'GIREAUD Noemie': ['Burger b1', 'Burger b10', 'Burger b4', 'Burger b7', 'Burger b2', 'Burger b5', 'Burger b3', 'Burger b6', 'Burger b9', 'Burger b8']}
subjects = {'Burger b1': 4, 'Burger b2': 5, 'Burger b3': 4, 'Burger b4': 5, 'Burger b5': 4, 'Burger b6': 3, 'Burger b7': 3, 'Burger b8': 4, 'Burger b9': 4, 'Burger b10': 3}


students = {
    'Nom complet_1': ['project_2', 'project_7', 'project_4', 'project_1', 'project_3', 'project_8'],
    'Nom complet_2': ['project_1', 'project_3', 'project_5', 'project_6', 'project_8'],
    'Nom complet_3': ['project_1', 'project_3', 'project_7', 'project_8', 'project_2', 'project_4', 'project_5'],
    'Nom complet_4': ['project_2', 'project_3', 'project_7', 'project_8'],
    'Nom complet_5': ['project_1', 'project_3', 'project_2', 'project_6', 'project_5', 'project_4']}
subjects = {'project_1': 1, 'project_2': 2, 'project_3': 2, 'project_4': 3, 'project_5': 3, 'project_6': 2, 'project_7': 2, 'project_8': 2}


allocations = allocate_subjects_spa(students, subjects)
print(allocations)
print("Attribution des sujets aux étudiants:")
for student, subject in allocations.items():
    print(f"{student} -> {subject}")'''