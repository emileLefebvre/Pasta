class Ingredient:
    def __init__(self, nom, prix, qty, unite):
        self.nom = nom
        self.prix_unite = round(float(prix / qty), 2)
        self.unite = unite

    def get_nom(self):
        return self.nom

    def get_prix_unite(self ):
        return self.prix_unite

    def get_unite(self):
        return self.unite

    def set_nom(self, nom):
        self.nom = nom

    def set_prix_unite(self, prix, qty):
        self.prix_unite = prix / qty

    def set_unite(self, unite):
        self.unite = unite

    def to_string(self):
        print(self.get_nom(), ": ", "{:.2f}".format(self.get_prix_unite()), "/", self.get_unite(), sep="", end="\n")




