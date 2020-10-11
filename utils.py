from ingredients import Ingredient
from recettes import Recette
import pickle
import os

#initialisation des variables globales
DICT_INGREDIENTS = {}
DICT_RECETTES = {}

#Partie sur les ingredients
def creer_ingredient():
    global DICT_INGREDIENTS
    print("\n-- Création d'un nouvel ingredient --")
    nom = input("Nom de l'ingrédient: ")

    if nom in DICT_INGREDIENTS:
        print("Il existe déjà un ingredient de ce nom. Création annulée.")
    else:
        prix = demander_float("Prix: ",2)
        qty = demander_float("Quantité: ",3)
        unite = demander_unite("L'unité de l'ingredient. Kg, L ou Unite: ")


        DICT_INGREDIENTS[nom] = Ingredient(nom, prix, qty, unite)
        DICT_INGREDIENTS = dict(sort_dict_by_key(DICT_INGREDIENTS))
        print("-- Création réussie --")

def sort_dict_by_key(d):

    sorted_keys = sorted(d.keys(), key=lambda x:x.lower())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict.update({key: d[key]})

    return dict(sorted_dict)

def ingredients_to_string():
    s = ""
    if DICT_INGREDIENTS != {}:
        s += "\n-- Ingredients\n"
        for x in DICT_INGREDIENTS.values():
            s += x.to_string() + "\n"
    else:
        s += "\nAucun ingredient n'a encore été crée"

    return s

def creer_recette():
    print("\n-- Création d'une nouvelle recette --")
    nom = input("Nom de la recette: ")
    ing = []

    if nom in DICT_RECETTES:
        print("Il existe déjà une recette de ce nom. Création annulée.")
    else:
        i = 0
        while True:
            #ing = [[Ingredient, (float)qty]] liste de liste des [ing, qty]
            i = + 1
            ing.append(demander_ingredient(i))
            while True:
                s = input("Un autre ingrédient à rajouter? (Oui/Non): ")
                if s == "Non" or s == "Oui":
                    break
                else:
                    print("Input invalide")
            if s == "Non":
                break

        qty = demander_float("Quantité totale de la recette: ", 3)
        unite = demander_unite("L'unité de la recette: ")
        prix_vente = demander_float("Quel est le prix de vente: ", 2)

        DICT_RECETTES[nom] = Recette(nom, ing, qty, unite, prix_vente)
        print("-- Création réussie --")

def recette_to_string():
    s = ""
    if DICT_RECETTES != {}:
        s += "\n-- Recettes --\n"
        for x in DICT_RECETTES.values():
            s += x.to_string() + "\n"
    else:
        s += "\nAucune recette n'a encore été crée"
    return s

#Partie exclusivement utils
def afficher_menu():
    print("\n-------- Menu --------\n"
          "0: Quitter\n"
          "1: Créer un ingredient\n"
          "2: Créer une recette\n"
          "4: Afficher les ingrédients\n"
          "5: Afficher les recettes\n"
          "6: Afficher les couts de revient\n"
          "8: Charger\n"
          "9: Sauvegarder")

def menu():
    afficher_menu()
    while True:
        choix = input("Entrez votre choix: ")
        if choix.isnumeric():
            if int(choix) == 0:
                quitter()
            elif int(choix) == 1:
                creer_ingredient()
            elif int(choix) == 2:
                creer_recette()
            elif int(choix) == 4:
                afficher_ingredients()
            elif int(choix) == 5:
                afficher_recettes()
            elif int(choix) == 6:
                afficher_cout_revient()
            elif int(choix) == 8:
                charger()
            elif int(choix) == 9:
                sauvegarder()
            else:
                print("Choix pas valide :(")
            afficher_menu()
        else:
            print("Choix pas valide :(")

def demander_float(message, n):
    while True:
        f = input(message)
        try:
            float(f)
            break
        except ValueError:
            print("Nombre invalide (, à la place du .)??")
    return round(float(f), n)

def demander_unite(message):
    while True:
        u = input(message)
        if u not in ["Kg", "L", "Unite"]:
            print("Unité non valide. Choix valide: Kg, L ou Unite")
        else:
            break
    return u

def demander_ingredient(i):
    while True:
        nom = input("Nom de l'ingredient #{}: ".format(i))
        if nom in DICT_INGREDIENTS:
            ing = DICT_INGREDIENTS[nom]
            qty = demander_float("Quelle quantité ({}): "
                                 .format(ing.get_unite()),3)
            break
        else:
            print("Aucun ingrédient de ce nom")
    return [ing, qty]

def afficher_ingredients():
    print(ingredients_to_string())

def afficher_recettes():
    print(recette_to_string())

def afficher_cout_revient():
    len_nom = 0
    len_prix_unit = 0
    len_prix_vente = 0
    len_diff = 0
    return 0

def sauvegarder():
    global DICT_INGREDIENTS
    global DICT_RECETTES

    DICT_INGREDIENTS = dict(sort_dict_by_key(DICT_INGREDIENTS))
    DICT_RECETTES = dict(sort_dict_by_key(DICT_RECETTES))

    data = {"ing" : DICT_INGREDIENTS, "recette" : DICT_RECETTES}
    f = open("data.pickle", "r+")
    f.truncate(0)
    f.close()
    pickle.dump(data, open("data.pickle", "wb"))
    print("Enregistrement terminé")

def charger():
    if os.path.getsize("data.pickle") == 0:
        print("Chargement impossible... fichier vide")
    else:
        data = pickle.load(open("data.pickle", "rb"))
        global DICT_INGREDIENTS
        global DICT_RECETTES
        DICT_INGREDIENTS = data["ing"]
        DICT_RECETTES = data["recette"]
        print("Chargement terminé")

"""
def modifier_ingredient():
    nom_ing = input("Nom de l'ingredient à modifier: ")
    index = 0
    for x in range(len(DICT_INGREDIENTS)):
        if nom_ing == DICT_INGREDIENTS[x].get_nom():
            index = x
            break
    if index == 0:
       print("Cet ingrédient n'existe pas :(")
    else:
        choix = ["NOM","PRIX","UNITE"]
        champ = input("Quel champ voulez-vous modifier? (Nom, prix ou unite): ").upper()
        if champ in choix:
            if champ == "PRIX":
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
                        DICT_INGREDIENTS[index].set_prix_unite(float(prix), float(qty))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre valide")
            elif champ == "UNITE":
                while 1:
                    unite = input("L'unité de l'ingrédient (Kg, L ou unité): ")
                    if unite in ["Kg", "L", "unite"]:
                        DICT_INGREDIENTS[index].set_unite(unite)
                        break
                    else:
                        print("Veuillez entrer une unité valide (Kg, L ou unité)")
            else:
                nom = input("Nouveau nom: ")
                DICT_INGREDIENTS[index].set_nom(nom)
            print("-- Modification réussi --")

def supprimer_ingredient():
    nom = input("Nom de l'ingrédient à supprimer: ")
    index = 0
    for x in range (len(DICT_INGREDIENTS)):
        if nom == DICT_INGREDIENTS[x].get_nom():
            index = x
            break
    if index == 0:
        print("Aucun ingrédient de ce nom")
    else:
        DICT_INGREDIENTS.pop(index)
        print("Ingredient supprimé")

def creer_recette():
    #DICT_INGREDIENTS = []
    print("\n-- Création d'une nouvelle recette --")
    while 1:
        nom = input("Nom de la recette: ")
        existe = False

        for i in LISTE_RECETTES:
            if nom == i.get_nom():
                existe = True
        if existe:
            print("Il existe déjà une recette portant ce nom... tentative annulée")
            break
        else:
            i = 0
            while 1:
                i += 1
                while 1:
                    ing = 0
                    input_ing = input("Nom de l'ingredient "+str(i)+": ")
                    for x in DICT_INGREDIENTS:
                        if input_ing == x.get_nom():
                            ing = x
                    if ing == 0:
                        print("Aucun ingredient de ce nom...")
                    else:
                        break
                while 1:
                    qty = input("Combien de {} ? : ".format(ing.get_unite()))
                    try:
                        float(qty)
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre valide")
                while 1:
                    #DICT_INGREDIENTS.append([ing,qty])
                    choix = input("Un autre ingredient à rajouter? (Oui/Non)")
                    if choix == "Non" or "Oui":
                        break
                    else:
                        print("Input: "+ choix+ " invalide...")
                if choix == "Non":
                    break
        break

    if not existe:
        while 1:
            qty_total = input("Quelle est la qantité finale de la recette: ")
            try:
                float(qty_total)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide")
        while 1:
            unite_total = input("L'unite finale de la recette: ")
            if unite_total in ["Kg", "L", "unite"]:
                break
            else:
                print("Veuillez entrer une unité valide (Kg, L ou unité)")
        while 1:
            prix_vente = input("Quel est le prix de vente: ")
            try:
                float(prix_vente)
                break
            except ValueError:
                print("Veuillez entrer un nombre valide")
        LISTE_RECETTES.append(Recette(nom,DICT_INGREDIENTS,qty_total,unite_total,prix_vente))
        print("-- Création réussie --")

def afficher_prix_revient():
    print("- Prix de revient")
    for x in LISTE_RECETTES:
        x.print_prix_revient()
"""

def quitter():
    while True:
        choix = input("Voulez vous sauvegarder avant de quitter? (Oui/Non): ")
        if choix == "Oui":
            sauvegarder()
            print("Terminated")
            exit()
        elif choix == "Non":
            print("Terminated")
            exit()
        else:
            print("Input non valide")
