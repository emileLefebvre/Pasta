class Recette:
    def __init__(self, nom, liste_ingredients, qty, unite, prix_vente):
        #liste_ingredients = [[Ing1,qty1],[Ing2,qty2],...[Ingn,qtyn]]
        self.nom = nom
        self.len_nom_ing = len("Total")
        #[0] -> Ing, [1] -> qty, [2] -> cout de l'Ing
        self.liste_ingredients = []
        self.qty = qty
        self.len_qty = len("{:.3f}".format(self.qty))
        self.unite = unite
        self.len_unite = len(self.unite)
        self.prix_vente = prix_vente
        self.len_prix_vente = len("{:.2f}".format(self.prix_vente))

        for x in liste_ingredients:
            if self.len_nom_ing < len(x[0].get_nom()):
                self.len_nom_ing = len(x[0].get_nom())
            if self.len_unite < len(x[0].get_unite()):
                self.len_unite = len(x[0].get_unite())
            if self.len_qty < len(str(x[1])):
                self.len_qty = len(str(x[1]))

            a = x
            a.append(x[1]*x[0].get_prix_unite())
            self.liste_ingredients.append(a)

    def get_cout_total(self):
        cout = 0
        for x in self.liste_ingredients:
            cout += x[2]
        return round(cout, 2)

    def get_cout_revient(self):
        prix_unitaire = self.get_cout_total() /  self.qty
        diff = self.prix_vente - prix_unitaire
        pour = 100*(self.prix_vente - prix_unitaire)/self.prix_vente

        return [prix_unitaire, diff, pour]

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def to_string(self):
        s= "\n"
        str_cout_total = "{:.2f}".format(self.get_cout_total())
        str_qty_total = "{:.3f}".format(self.qty)
        contour = "*"*(self.len_qty + self.len_unite + self.len_nom_ing + len(str_cout_total) +12)
        s += "- {}\n".format(self.get_nom())
        s += contour + "\n"
        for x in self.liste_ingredients:
            str_nom = str(x[0].get_nom())
            str_qty = "{:.3f}".format(x[1])
            str_unite = x[0].get_unite()
            str_cout = "{:.2f}".format(x[2])
            s += "* " + " "*(self.len_nom_ing-len(str_nom)) + str_nom + " | "
            s += " "*(self.len_qty-len(str_qty)) + str_qty + " "
            s += " "*(self.len_unite-len(str_unite)) + str_unite + " | "
            s += " "*(len(str_cout_total)-len(str_cout)) + str_cout + "$ *\n"
        s += "* " + "-"*(self.len_qty + self.len_unite + self.len_nom_ing + len(str_cout_total) + 8) + " *\n"
        s += "* " + " "*(self.len_nom_ing-5) + "Total" + " | "
        s += " " * (self.len_qty - len(str_qty_total)) + str_qty_total + " "
        s += " "*(self.len_unite-len(self.unite)) + self.unite + " | "
        s += str_cout_total + "$ *\n"
        s += contour
        return s





