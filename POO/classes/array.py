#!/usr/bin/env python3

class Array:
    def __init__(self, *args):
        self.tableau = list(args)

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
        if all(isinstance(t, Array) for t in args):
            self.tableau

        raise TypeError("Un element suspect détécté")


array = Array(0, "7", 4, 7, 8)
