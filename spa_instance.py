"""
Code de génération d'instances du problème d'affectation de projet à des étudiants (Student Project Allocation)
"""

import random,pprint,pandas,csv


def create_random_list(nb_items:int,items_names) -> list[str]:
    result_list = []
    for i in range(nb_items):
        result_list.append(items_names+str(i+1))
    return result_list


def create_projects_capacities(projects_list,max_capacity): #a = {"nom": "Alice", "âge": 25}
    projects_cap = {}
    nb_projects = len(projects_list)
    for p in projects_list:
        projects_cap[p] = random.randint(1,max_capacity)
    return projects_cap


def create_pref_dict(students_list,projects_list,min):
    pref_dict = {}
    for st in students_list:
        ch_list = []
        nb_choices = random.randint(min,len(projects_list))
        for i in range(nb_choices):
            ch = random.choice(projects_list)
            while ch in ch_list:
                ch = random.choice(projects_list)
            ch_list.append(ch)
        pref_dict[st] = ch_list
    return pref_dict


def compute_num_student_choices(students,projects_list,student_prefs):
    lst_choice = [-1]*len(projects_list) # choice in num
    for p in student_prefs: # pour tous les choix
        p_rk = projects_list.index(p) # il existe
        lst_choice[p_rk] = student_prefs.index(p)+1
    return lst_choice


def compute_num_mat_choices(students_list,projects_list,pref_dict):
    res_lst = []
    for st in students_list:
        res_lst.append(compute_num_student_choices(st,projects_list,pref_dict[st]))
    return res_lst


# sauvegarde dans un fichier csv ou excel
def save_in_file(students_list,projects_list,prefs):
    # save all lists and dict
    # autant de colonnes que de projets et mettre des nb pour le choix de chaque étudiant
    res = compute_num_mat_choices(students_list,projects_list,prefs)
    col_pref = transpose_mat(res)
    sn = ["Nom complet"]+projects_list
    df_lst = col_pref
    df_lst.insert(0, students_list)
    lst = dict(zip(sn, df_lst))
    df = pandas.DataFrame(lst)
    df.to_excel("test.xlsx") # TODO : passer le bom enparamètre
    return True


def transpose_mat(lst:list[list[int]]):
    nb_lines = len(lst)
    nb_col = len(lst[0])
    lst_res = []
    for col in range(nb_col):
        lst_res.append([lst[i][col] for i in range(nb_lines)])
    return lst_res

def save_in_file_csv(students_list, projects_list, prefs):
    res = compute_num_mat_choices(students_list, projects_list, prefs)
    col_pref = transpose_mat(res)
    sn = ["Nom complet"] + projects_list
    df_lst = col_pref
    df_lst.insert(0, students_list)
    lst = dict(zip(sn, df_lst))

    with open("inputCSV/instance0.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sn)
        writer.writeheader()
        for i in range(len(students_list)):
            writer.writerow({k: v[i] for k, v in lst.items()})

    return True
# tests
min_choices = 4 # nombre minimum de choix
sl = create_random_list(90, "Nom complet_")
pl = create_random_list(20, "project_")
#pc = create_projects_capacities(pl, 6) # nombre de place par projet
prefs = create_pref_dict(sl, pl, min_choices) # choix aléatoire
df = save_in_file_csv(sl, pl, prefs) # formmat csv
