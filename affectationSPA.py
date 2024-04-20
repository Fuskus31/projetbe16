"""
Algorithme brute force pour un problème d'affectation basé sur des préférences
Les préférences vont de 1 (préféré) à N (moins préféré)
Pour calculer le coût global d'une affectation on considère chaque note comme un coût
et on cherche l'affectation de coût minimal.
Vincent Dugat mars 2024
"""
from itertools import permutations,combinations # brute force bête et méchant

coeff = 10 # pénalité
#personnes = ['Luffy','Zorro','Sanji','Robin','Chopper'] # liste sujet
#subjects_list ={'ch1':2,'ch2':1,'ch3':2,'ch4':1,'ch5':1,'ch6':3,'ch7':1}
#ressources = ['ch1','ch1','ch2','ch3','ch3','ch4','ch5','ch6','ch6','ch6','ch7'] # liste projets
# les capacités sont simulées par la répétition d'une ressource

# preferences
#preferences1 = {'Luffy':['ch1','ch2','ch5','ch4','ch3'],
				#'Zorro':['ch1','ch3','ch2','ch5','ch4'],
				#'Sanji':['ch2','ch4','ch1','ch3','ch5'],
				#'Robin':['ch2','ch1','ch5','ch3','ch4'],
				#'Chopper':['ch2','ch3','ch1','ch4','ch5']}
#preferences2 = {'Luffy':['ch1','ch2','ch5','ch6','ch3'],
				#'Zorro':['ch1','ch3','ch5','ch4'],
				#'Sanji':['ch2','ch4','ch1','ch3','ch5'],
				#'Robin':['ch2','ch7','ch3','ch6','ch1','ch4','ch5'],
				#'Chopper':['ch2','ch3','ch1','ch6']}
#preferences = preferences2

def construct_ressources_list(subjects_list):
	res_list =[]
	aux_lst = [(k,v) for k,v in subjects_list.items()]
	for (k,v) in aux_lst:
		res_list = res_list+([k]*v)
	return res_list

def cout(preferences,permut,personnes)->int:
#Calcule le coût d'une affectation (matching)
	som = 0
	for i in range(len(permut)):
		item = permut[i]
		pers = personnes[i]
		try:
			som += preferences[pers].index(item)
		except:
			som += coeff
	return som

def analyse_permutations(combiRessources,preferences,personnes):
	pl = list(permutations(combiRessources)) # calcul des permutations d'une combinaison

	mincout = 2**16 # init du min au max sur 16 bits
	minPerm = [] # indice du min
	# on fait le min à la main
	for i in range(len(pl)):# pour toutes les permutations
		perm = list(pl[i]) # je veux une liste
		c = cout(preferences,perm,personnes)
		if c<mincout:
			mincout = c
			minPerm = perm
	return (mincout,minPerm) # la meilleure


'''def lancement_testAffectationSpa():
	cl = list(combinations(ressources,len(personnes))) # si plus de projets que de sujets
	minPermGlobal = []
	minCoutGlobal = 2**16
	for combi in cl:
		# toutes les permutations possibles de ressources pour cette combination
		(coutLocal,perm) = analyse_permutations(combi,preferences)
		if coutLocal<minCoutGlobal:
			minCoutGlobal = coutLocal
			minPermGlobal = perm

	print(construct_ressources_list(subjects_list)==ressources)
	print("Première affectation solution :",minPermGlobal,"Cout = ",minCoutGlobal)'''


def lancement_testaffection_bruteforce(cl, preferencemain, personnes, max_essais=30000):
    i = 0
    minPermGlobal = []
    minCoutGlobal = 2 ** 16
    for combi in cl:
        if i >= max_essais:
            print("Nombre maximum d'essais atteint")
            break
        print(i)
        i = i+1
        # toutes les permutations possibles de ressources pour cette combination
        (coutLocal, perm) = analyse_permutations(combi, preferencemain, personnes)
        if coutLocal < minCoutGlobal:
            minCoutGlobal = coutLocal
            minPermGlobal = perm
        if minCoutGlobal <= 15:  # on s'arrête si le cout est inférieur ou égal à 5
            print("ok")
            break

    print("Première affectation solution :", minPermGlobal, "Cout = ", minCoutGlobal)


