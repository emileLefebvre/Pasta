from utils import *

def creer_ingredient():
    print("\n-- Création d'un nouvel ingredient --")
    nom = input("Nom de l'ingrédient: ")
    existe = False

    for x in range(len(LISTE_INGREDIENTS)):
        if nom == LISTE_INGREDIENTS[x].get_nom():
            existe = True
    if existe:
        print("Il existe déjà un ingrédient portant ce nom... tentative annulée")
    else:
        while 1:
            prix = input("Prix: ")
            try:
                float(prix)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide")
        while 1:
            qty = input("Quantité pour le prix: ")
            try:
                float(qty)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide")
        while 1:
            unite = input("L'unité de l'ingrédient (Kg, L ou unité): ")
            if unite in ["Kg", "L", "unite"]:
                break
            else:
                print("Veuillez entrer une unité valide (Kg, L ou unité)")

        LISTE_INGREDIENTS.append(Ingredient(nom,float(prix),float(qty),unite))
        print("-- Création réussie --")