from ingredients import Ingredient
import pickle

LISTE_INGREDIENTS = []

def afficher_menu():
    print("\n-------- Menu --------\n"
          "0: Quitter\n"
          "1: Créer un ingredient\n"
          "2: Afficher les ingrédients\n"
          "3: Sauvegarder\n"
          "4: Charger\n"
          "5: Modifier un ingrédients")

def menu():
    afficher_menu()
    while True:
        choix = input("Entrez votre choix: ")
        if choix.isnumeric():
            if int(choix) == 0:
                quitter()
            elif int(choix) == 1:
                creer_ingredient()
                afficher_menu()
            elif int(choix) == 2:
                afficher_liste_ingredients()
                afficher_menu()
            elif int(choix) == 3:
                sauvegarder()
                afficher_menu()
            elif int(choix) == 4:
                charger()
                afficher_menu()
            else:
                print("Choix pas valide :(")
        else:
            print("Choix pas valide :(")

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

def modifier_ingredient():
    pass

def afficher_liste_ingredients():

    if len(LISTE_INGREDIENTS) == 0:
        print("\nAucun ingrédient n'a été crée")
    else:
        print("\n -- Ingrédients --")
        for x in LISTE_INGREDIENTS:
            x.print_ing()

def sauvegarder():
    data = {"ing" : LISTE_INGREDIENTS}
    f = open("data.pickle", "r+")
    f.truncate(0)
    f.close()
    pickle.dump(data, open("data.pickle", "wb"))
    print("Enregistrement terminé")

def charger():
    data = pickle.load(open("data.pickle", "rb"))
    global LISTE_INGREDIENTS
    LISTE_INGREDIENTS = data["ing"]
    print("Chargement terminé")

def modifier_ingredient():
    ing = input("Quel est le nom de l'ingredient vous voulez modifier: ")
    for x in range(len(LISTE_INGREDIENTS)):
        if ing == LISTE_INGREDIENTS[x]:
            print("Voici l'ingredient: \nnom: ", LISTE_INGREDIENTS[x].get_nom)




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
