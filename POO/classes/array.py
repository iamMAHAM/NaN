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
        for element in self.iterate():
            if not fonction(element):
                return False

        return True

    def fill(self, valeur, debut=0, fin=None):

        if not fin:
            fin = self.length()

        if (not isinstance(debut, int) or not isinstance(fin, int)):
            raise TypeError('Le début ou la fin doit être un entier')
        for i in range(self.length()):
            if debut <= i < fin:
                self.tableau[i] = valeur

        return self.tableau

    def filter(self, fonction):
        tab = Array()

        for element in self.iterate():
            if (fonction(element)):
                tab.tableau[tab.length():] = [element]

        return tab.iterate()


array = Array(9, 2, 4, 7, 8)
array2 = Array(5, 5, 7)
array3 = Array("yakasport", "diallogage", "dedy")

print(array.filter(lambda x: x > 2))
