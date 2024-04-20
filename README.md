# kev-projet-16
J'ai modifié le nom des burgers pour un affichage plus lisible et pour l'instant je m'occupe d'obtenir les données utiles pour les algorithmes

### 25 mars : 
>le main.py genere des dictionnaires avec la clé : Nom étudiant --> qui donne son tableau de vote par ordre de préférence ( générer en csv pour une lecture plus facile pour vérifier ).
>dans les votes le chiffre `-1` signifie que l'étudiant n'a pas fait de choix 


### 26 mars : 
>J'ai ajouté le 26 mars la possibilité d'avoir un dictionnaire qui contient tous les projets ,avec leur nombre de places initiales. ( les places initiales sont générés par une fonction très simple dans le utils.py) qui prend >un chiffre entre 3 et 8 par exemple.

 Nous avons également le dictionnaire dictionnaire[str,list]. Avec le nom de tous les étudiants avec le tableau contenant les projets qu'ils ont choisis dans l'ordre du projet favori au moins voulu.
![image](https://github.com/Fuskus31/kev-N-16/assets/70700226/e09e4bb6-e81a-4800-a171-a01d4bdbd22f)

### 10 avril: bruteforce
>j'ai ajouté le 10 avril la fonction def startBruteForce(dictionnaire_student_project,tableau_choix_possible) pour lancer les fonctions forceBrut donner par vincent DUGAT, nous avons remarquer que les fichiers qui ont plus de >6 étudiants et 8 projets (2minimum - 4 places max) commencent à prendre un temps important à l'execution 23s.. ![image](https://github.com/Fuskus31/kev-N-16/assets/70700226/17527e62-6c83-4cce-a7bf-8d20a7513649)

nous avons ajouté la possibilité de choisir le cout maximum voulu dans la fonction lancement_testaffection_bruteforce() et le nombre d'essais maximum, on remarque que cl = list(combinations(ressources, len(clesEtudiant))) fait bugger l'ordinateur en raison de la taille énorme de l'espace de combinaisons générées, cela nous empêche d'utiliser cet algorithme sur des données trop importantes.

### 15 avril hongrois
j'ai ajouté l'option qui permet de choisir l'algorithme hongrois, le code des fonctions pour utiliser la méthode hongroise est dans le fichier hongrois.py, on peut visualiser la matrice et les allocations dans 2 fichier .txt 
resultatHongrois.txt et matrice_cout_hongrois.txt si le vote est -1 ( pas de choix du votant ) la matrice complète avec le nombre d'étudiant +1 ( s'il y a 39 étudiants ce sera 40 pour  les -1). car à l'initialisation on met la plus grande valeur possible pour chaque valeur de la matrice et quand les étudiants ne font pas de choix (-1) l'algorithme ne change pas la valeur.

### 17 avril heuristique
>ne garantissent pas la solution optimale !
 Dans notre contexte l'approche heuristique  tente d'attribuer à chaque étudiant un projet parmi ses préférences, en respectant les contraintes de capacité des projets, et en laissant certains étudiants sans projet 
 si nécessaire. Cette méthode maximise la satisfaction globale des étudiants 

### 19 avril algo SPA basique
Ajout d'une fonction basique pour le problème d'allocation des projets étudiant afin d'avoir plus de choix pour résoudre un problème.
Cette méthode utilise la méthode de répartition équitable des sujets, où chaque sujet est attribué à un étudiant à la fois, en respectant les contraintes de capacité du sujet et les préférences des étudiants.