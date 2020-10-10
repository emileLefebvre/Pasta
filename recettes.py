class Recette:
    def __init__(self, nom, liste_ingredients, qty, unite):
        self.nom = nom
        self.prix = 0
        self.qty = qty
        self.unite = unite
        self.length_ing = 5 #a cause du total de la derniere range
        self.length_qty = len(str(self.qty))
        self.length_unite = len(unite)
        self.liste_ingredients = []
        #liste ingredient est une liste de liste avec le nom en [0] et la quantite en [1] et l'unite en [2] et le prix en [3].
        for i in liste_ingredients:
            self.liste_ingredients.append([i[0].get_nom(), str(i[1]), i[0].get_unite(), round(i[0].get_prix_unite()*float(i[1]),2)])
        for i in self.liste_ingredients:
            if len(i[0]) > self.length_ing:
                self.length_ing = len(i[0])
            if len(str(i[1])) > self.length_qty:
                self.length_qty = len(str(i[1]))
            if len(i[2]) > self.length_unite:
                self.length_unite = len(i[2])
            self.prix += i[3]
        self.length_prix = len("{:.2f}".format(self.prix))

    def get_cout_total(self):
        cout = 0
        for x in self.liste_ingredients:
            cout += x[3]
        return cout

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def print_recette(self):
        contour = "*" * (self.length_ing + self.length_prix + self.length_unite +self.length_qty + 12)
        print("- {}".format(self.get_nom()))
        print(contour)
        for i in self.liste_ingredients:
            print("* "+" "*(self.length_ing-len(i[0])),i[0],end=" | ",sep="")
            print(" "*(self.length_qty - len(i[1])), i[1], end=" ", sep="")
            print(" " * (self.length_unite - len(i[2])), i[2], end=" | ", sep="")
            print(" "*(self.length_prix - len("{:.2f}".format(i[3]))), "{:.2f}$".format(i[3]), end=" *\n", sep="")
        print("* "+"-" * (self.length_ing + self.length_prix + self.length_unite +self.length_qty + 8)+" *")
        print("* "+" "*(self.length_ing-5),"Total", end=" | ", sep="")
        print(" "*(self.length_qty-len(str(self.qty))),self.qty,end=" ",sep="")
        print(" "*(self.length_unite-len(self.unite)),self.unite,end=" | ", sep="")
        print("{:.2f}$".format(self.prix), end=" *\n", sep="")
        print(contour+"\n")



