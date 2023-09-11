#!/usr/bin/env python3


class Array:
    def __init__(self, *args):
        self.tableau = list(args)

    def __repr__(self):
        return f'Array {self.tableau}'

    def iterate(self):
        return self.tableau

    def afficher(self):
        print(self.tableau)

    def length(self):
        compteur = 0
        for _ in self.tableau:
            compteur += 1

        return compteur

    def toReversed(self):
        tableaurenverse = self.iterate()[::-1]
        return Array(*tableaurenverse)

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
                self.push(element)

        return Array(**self.tableau)

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
                self.push(element)

        return Array(*tab.iterate())

    def find(self, fonction):
        for element in self.iterate():
            if (fonction(element)):
                return element

        return None

    def findIndex(self, fonction):
        for i in range(self.length()):
            if (fonction(self.tableau[i])):
                return i

        return -1

    def findLast(self, fonction):
        tableaureverse = self.toReversed()
        for element in tableaureverse.iterate():
            if (fonction(element)):
                return element

        return None

    def findLastIndex(self, fonction):
        for i in range(self.length()):
            if fonction(self.toReversed().iterate()[i]):
                return i

        return -1

    def forEach(self, fonction):
        for element in self.iterate():
            fonction(element)

    def map(self, fonctionMap):
        mapped = [fonctionMap(element) for element in self.tableau]

        return Array(*mapped)

    @staticmethod
    def From(iterable, fonctionMap=None):
        tolist = [element for element in iterable]
        if fonctionMap:
            return Array(*tolist).map(fonctionMap)

        return Array(*tolist)

    def includes(self, element):
        return element in self.iterate()

    def indexOf(self, element):
        for i in range(len(self.iterate())):
            if self.iterate()[i] == element:
                return i

        return -1

    @staticmethod
    def isArray(element):
        return isinstance(element, Array)

    def join(self, sepateur=','):
        chaine = ''
        for element in self.iterate():
            chaine += element
            index = self.indexOf(element)

            if (index == self.length() - 1):
                continue

            chaine += sepateur

        return chaine

    def lastIndexOf(self, element):
        renverse = self.toReversed()
        index = renverse.indexOf(element)
        if (index == -1):
            return -1
        return renverse.indexOf(element) + renverse.length() - 1

    @staticmethod
    def of(*args):
        return Array.From(args)

    def pop(self):
        dernier = self.iterate()[self.length() - 1]
        self.tableau = self.tableau[0:self.length() - 1]
        return dernier

    def push(self, *args):
        for arg in args:
            self.tableau[:self.length()] = [arg]

        return self.length()


array = Array(2, 4, 9, 7, 8, 4, 7, 2)
array2 = Array(5, 5, 7)
array3 = Array("yakasport", "diallogage", "dedy")

print(array3.pop())
print(array3)
