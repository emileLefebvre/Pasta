from ingredients import Ingredient
from recettes import Recette
import pickle
import os

LISTE_INGREDIENTS = []
LISTE_RECETTES = []

def afficher_menu():
    print("\n-------- Menu --------\n"
          "0: Quitter\n"
          "1: Créer un ingredient\n"
          "2: Supprimer un ingrédient\n"
          "3: Modifier un ingrédient\n"
          "4: Afficher les ingrédients\n"
          "5: Créer une recette\n"
          "6: Afficher les recette\n"
          "7: Afficher les prix de revient\n"
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
                supprimer_ingredient()
            elif int(choix) == 3:
                modifier_ingredient()
            elif int(choix) == 4:
                afficher_liste_ingredients()
            elif int(choix) == 5:
                creer_recette()
            elif int(choix) == 6:
                afficher_liste_recette()
            elif int(choix) == 7:
                afficher_prix_revient()
            elif int(choix) == 8:
                charger()
            elif int(choix) == 9:
                sauvegarder()
            else:
                print("Choix pas valide :(")
            afficher_menu()
        else:
            print("Choix pas valide :(")

def afficher_liste_ingredients():

    if len(LISTE_INGREDIENTS) == 0:
        print("\nAucun ingrédient n'a été crée")
    else:
        print("\n -- Ingrédients --")
        for x in LISTE_INGREDIENTS:
            x.to_string()

def afficher_liste_recette():

    if len(LISTE_RECETTES) == 0:
        print("\nAucune recette n'a été crée")
    else:
        print("\n ----- Recettes -----")
        for x in LISTE_RECETTES:
            x.print_recette()

def sauvegarder():
    data = {"ing" : LISTE_INGREDIENTS, "recette" : LISTE_RECETTES}
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
        global LISTE_INGREDIENTS
        global LISTE_RECETTES
        LISTE_INGREDIENTS = data["ing"]
        LISTE_RECETTES = data["recette"]
        print("Chargement terminé")

def modifier_ingredient():
    nom_ing = input("Nom de l'ingredient à modifier: ")
    index = 0
    for x in range(len(LISTE_INGREDIENTS)):
        if nom_ing == LISTE_INGREDIENTS[x].get_nom():
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
                        LISTE_INGREDIENTS[index].set_prix_unite(float(prix), float(qty))
                        break
                    except ValueError:
                        print("Veuillez entrer un nombre valide")
            elif champ == "UNITE":
                while 1:
                    unite = input("L'unité de l'ingrédient (Kg, L ou unité): ")
                    if unite in ["Kg", "L", "unite"]:
                        LISTE_INGREDIENTS[index].set_unite(unite)
                        break
                    else:
                        print("Veuillez entrer une unité valide (Kg, L ou unité)")
            else:
                nom = input("Nouveau nom: ")
                LISTE_INGREDIENTS[index].set_nom(nom)
            print("-- Modification réussi --")

def supprimer_ingredient():
    nom = input("Nom de l'ingrédient à supprimer: ")
    index = 0
    for x in range (len(LISTE_INGREDIENTS)):
        if nom == LISTE_INGREDIENTS[x].get_nom():
            index = x
            break
    if index == 0:
        print("Aucun ingrédient de ce nom")
    else:
        LISTE_INGREDIENTS.pop(index)
        print("Ingredient supprimé")

def creer_recette():
    liste_ingredients = []
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
                    for x in LISTE_INGREDIENTS:
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
                    liste_ingredients.append([ing,qty])
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
        LISTE_RECETTES.append(Recette(nom,liste_ingredients,qty_total,unite_total,prix_vente))
        print("-- Création réussie --")

def afficher_prix_revient():
    print("- Prix de revient")
    for x in LISTE_RECETTES:
        x.print_prix_revient()

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
