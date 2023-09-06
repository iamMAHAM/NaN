#!/usr/bin/env python3

class Array:
    def __init__(self, *args):
        self.tableau = list(args)

    def iterate(self):
        return self.tableau

    def afficher(self):
        print(self.tableau)

    def length(self):
        compteur = 0
        for _ in self.tableau:
            compteur += 1

        return compteur

    def at(self, indice):
        if indice < 0:
            indice = self.length() + indice

        for i in range(self.length()):
            if i == indice:
                return self.tableau[indice]

        return None

    def concat(self, *args):
        for tab in args:
            if not isinstance(tab, Array):
                raise TypeError("Un element suspect détécté : ", tab)

            for element in tab.iterate():
                self.tableau[self.length():] = [element]

        return self.tableau

    def copyWithin(self, cible, debut, fin):
        pass

    def every(self, fonction):
        pass


array = Array(0, "7", 4, 7, 8)
array2 = Array(5, 5, 7)
array3 = Array("yakasport", "diallogage", "dedy")
