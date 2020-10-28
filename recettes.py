class Recette:
    def __init__(self, nom, liste_ingredients, qty, unite, prix_vente):
        #liste_ingredients = [[Ing1,qty1],[Ing2,qty2],...[Ingn,qtyn]]
        self.nom = nom
        #self.len_nom_ing = len("Total")
        #[0] -> Ing, [1] -> qty, [2] -> cout de l'Ing
        self.liste_ingredients = liste_ingredients
        self.qty = qty
        self.unite = unite
        self.prix_vente = prix_vente

    def get_cout_total(self):
        cout = 0
        for x in self.liste_ingredients:
            cout += x[1]*x[0].get_prix_unite()
        return round(cout, 2)

    def get_cout_revient(self):
        prix_unitaire = self.get_prix_unite()
        diff = self.prix_vente - prix_unitaire
        pour = 100*(self.prix_vente - prix_unitaire)/self.prix_vente

        return [prix_unitaire, diff, pour]

    def get_prix_vente(self):
        return self.prix_vente

    def set_prix_vente(self, n_prix):
        self.prix_vente = n_prix

    def get_nom(self):
        return self.nom

    def get_liste_ingredients(self):
        return self.liste_ingredients

    def set_liste_ingredients(self, l):
        self.liste_ingredients = l

    def set_nom(self, nom):
        self.nom = nom

    def get_unite(self):
        return self.unite

    def get_prix_unite(self):
        return round(self.get_cout_total() /  self.qty,2)

    def ing_to_string(self):
        return "{}: {:.2f}/{}".format(self.get_nom(), self.get_cout_total() /  self.qty, self.unite)

    def to_string(self):
        len_nom = 0
        len_unite = len(self.get_unite())
        len_qty = len("{:.3f}".format(self.qty))
        len_cout = 0

        for x in self.liste_ingredients:
             if len_nom < len(x[0].get_nom()):
                 len_nom = len(x[0].get_nom())
             if len_unite < len(x[0].get_unite()):
                 len_unite = len(x[0].get_unite())
             if len_qty < len("{:.3f}".format(x[1])):
                 len_qty = len("{:.3f}".format(x[1]))
             if len_cout < len(str(x[1]*x[0].get_prix_unite())):
                len_cout = len(str(x[1]*x[0].get_prix_unite()))

        s= "\n"
        str_cout_total = "{:.2f}".format(self.get_cout_total())
        str_qty_total = "{:.3f}".format(self.qty)
        contour = "*"*(len_qty + len_unite + len_nom + len(str_cout_total) +12)
        s += "- {}\n".format(self.get_nom())
        s += contour + "\n"
        for x in self.liste_ingredients:
            str_nom = str(x[0].get_nom())
            str_qty = "{:.3f}".format(x[1])
            str_unite = x[0].get_unite()
            str_cout = "{:.2f}".format(x[1]*x[0].get_prix_unite())
            s += "* " + " "*(len_nom-len(str_nom)) + str_nom + " | "
            s += " "*(len_qty-len(str_qty)) + str_qty + " "
            s += " "*(len_unite-len(str_unite)) + str_unite + " | "
            s += " "*(len(str_cout_total)-len(str_cout)) + str_cout + "$ *\n"
        s += "* " + "-"*(len_qty + len_unite + len_nom + len(str_cout_total) + 8) + " *\n"
        s += "* " + " "*(len_nom-5) + "Total" + " | "
        s += " " * (len_qty - len(str_qty_total)) + str_qty_total + " "
        s += " "*(len_unite-len(self.unite)) + self.unite + " | "
        s += str_cout_total + "$ *\n"
        s += contour

        return s





