class Recette:
    def __init__(self, nom, liste_ingredients):
        self.nom = nom
        self.liste_ingredients = []
        #liste ingredient est une liste de liste avec le nom en [0] et la quantite en [1] et le cout en [2].
        for i in liste_ingredients:
            self.liste_ingredients.append([i[0].get_nom(), str(i[1])+" "+i[0].get_unite(), i[0].get_prix_unite()*float(i[1])])
    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def print_recette(self):
        print("- {}".format(self.get_nom()))
        for i in self.liste_ingredients:
            print(i[0],i[1],"{:.2f}$".format(i[2]),end="\n")








