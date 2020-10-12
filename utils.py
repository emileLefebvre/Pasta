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
    print("\n-- Creation d'un nouvel ingredient --")
    nom = input("Nom de l'ingredient: ")

    if nom in DICT_INGREDIENTS:
        print("Il existe deja un ingredient de ce nom. Creation annulee.")
    else:
        prix = demander_float("Prix: ",2)
        qty = demander_float("Quantite: ",3)
        unite = demander_unite("L'unite de l'ingredient. Kg, L ou Unite: ")


        DICT_INGREDIENTS[nom] = Ingredient(nom, prix, qty, unite)
        DICT_INGREDIENTS = dict(sort_dict_by_key(DICT_INGREDIENTS))
        print("-- Creation reussie --")

def sort_dict_by_key(d):

    sorted_keys = sorted(d.keys(), key=lambda x:x.lower())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict.update({key: d[key]})

    return dict(sorted_dict)

def ingredients_to_string():
    s = ""
    if not (DICT_INGREDIENTS == {} and DICT_RECETTES == {}):
        if DICT_INGREDIENTS != {}:
            s += "\n-- Ingredients de base --\n"
            for x in DICT_INGREDIENTS.values():
                s += x.to_string() + "\n"
        if DICT_RECETTES != {}:
            s += "\n-- Ingredients (recette) --\n"
            for x in DICT_RECETTES.values():
                s += x.ing_to_string() + "\n"
    else:
        s += "\nAucun ingredient n'a encore ete cree\n"
    return s

def creer_recette():
    print("\n-- Creation d'une nouvelle recette --")
    nom = input("Nom de la recette: ")
    ing = []

    if nom in DICT_RECETTES:
        print("Il existe deja une recette de ce nom. Creation annulee.")
    else:
        i = 0
        while True:
            #ing = [[Ingredient, (float)qty]] liste de liste des [ing, qty]
            i += 1
            ing.append(demander_ingredient(i))
            while True:
                s = input("Un autre ingredient a rajouter? (Oui/Non): ")
                if s == "Non" or s == "Oui":
                    break
                else:
                    print("Input invalide")
            if s == "Non":
                break

        qty = demander_float("Quantite totale de la recette: ", 3)
        unite = demander_unite("L'unite de la recette: ")
        prix_vente = demander_float("Quel est le prix de vente (0 si on vend pas): ", 2)

        DICT_RECETTES[nom] = Recette(nom, ing, qty, unite, prix_vente)
        print("-- Creation reussie --")

def recette_to_string():
    s = ""
    if DICT_RECETTES != {}:
        s += "\n-- Recettes --\n"
        for x in DICT_RECETTES.values():
            s += x.to_string() + "\n"
    else:
        s += "\nAucune recette n'a encore ete cree\n"
    return s

#Partie exclusivement utils
def afficher_menu():
    print("\n-------- Menu --------\n"
          "0: Quitter\n"
          "1: Creer un ingredient\n"
          "2: Creer une recette\n"
          "4: Afficher les ingredients\n"
          "5: Afficher les recettes\n"
          "6: Afficher les couts de revient\n"
          "7: Imprimer\n"
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
            elif int(choix) == 7:
                imprimer()
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
            print("Nombre invalide (, a la place du .)??")
    return round(float(f), n)

def demander_unite(message):
    while True:
        u = input(message)
        if u not in ["Kg", "L", "Unite"]:
            print("Unite non valide. Choix valide: Kg, L ou Unite")
        else:
            break
    return u

def demander_ingredient(i):
    while True:
        nom = input("Nom de l'ingredient #{}: ".format(i))
        if nom in DICT_INGREDIENTS:
            ing = DICT_INGREDIENTS[nom]
            qty = demander_float("Quelle quantite ({}): "
                                 .format(ing.get_unite()),3)
            break
        elif nom in DICT_RECETTES:
            ing = DICT_RECETTES[nom]
            qty = demander_float("Quelle quantite ({}): "
                                 .format(ing.get_unite()), 3)
            break
        else:
            print("Aucun ingredient de ce nom")

    return [ing, qty]

def afficher_ingredients():
    print(ingredients_to_string())

def afficher_recettes():
    print(recette_to_string())

def afficher_cout_revient():
    print(cout_revient_to_string())

def cout_revient_to_string():
    len_nom = 8
    if DICT_RECETTES == {}:
        s = "\nAucune recette n'a encore ete cree\n"
    else:
        s = "\n-- Cout de revient --\n"
        for x in DICT_RECETTES:
            if len(x) > len_nom:
                len_nom = len(x)
        contour = "*"*(len_nom+62)+"\n"
        s += contour + "* " + " "*(len_nom-8) + "Recettes | "
        s += "Prix unitaire | Prix de vente |   Difference  |    %    *\n"
        s += "* "+"-"*len_nom + " | ------------- | ------------- | ------------- | ------- *\n"
        for x in DICT_RECETTES.values():
            if x.get_prix_vente() != 0:
                l = x.get_cout_revient()
                s += "* " + " "*(len_nom - len(x.get_nom())) + x.get_nom() + " | {:.2f} / ".format(l[0])
                s += " "*(5-len(x.unite)) + "{} | {:.2f} / ".format(x.unite, x.prix_vente)
                s += " "*(5-len(x.unite)) + "{} | {:.2f} / ".format(x.unite, l[1])
                s += " "*(5-len(x.unite)) + "{} | {:.2f}  *\n".format(x.unite, l[2])
        s += contour
    return s

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
    print("Enregistrement termine")

def charger():
    if os.path.getsize("data.pickle") == 0:
        print("Chargement impossible... fichier vide")
    else:
        data = pickle.load(open("data.pickle", "rb"))
        global DICT_INGREDIENTS
        global DICT_RECETTES
        DICT_INGREDIENTS = data["ing"]
        DICT_RECETTES = data["recette"]
        print("Chargement termine")

def imprimer():
    print("-- Debut de l'ecriture --")
    file = open("Sortie.txt", "w")
    file.truncate(0)
    file.write(ingredients_to_string())
    file.write("-"*50+"\n")
    file.write(recette_to_string())
    file.write("-" * 50 +"\n")
    file.write(cout_revient_to_string())
    file.write("-" * 50 +"\n")
    file.close()
    print("-- Fin de l'ecriture --")

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
