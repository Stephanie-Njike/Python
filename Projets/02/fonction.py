
def augmente_moi(a, *param):
    return a + param[0] + param[1] + param[2]

augmente_moi(1, 4, 5, 8)

def dico_in_param(**params):
    return params

print(dico_in_param(nom="Stephanie", prenom="olive"))
