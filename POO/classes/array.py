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

    def flat(self, profondeur):
        def getLevel(tab):
            count = 1
            for element in tab:
                while self.some(lambda v: isinstance(v, list)):
                    pass

        array = Array()
        for element in self.iterate():
            pass

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
        self.tableau = self.tableau[:self.length() - 1]
        return dernier

    def push(self, *args):
        for arg in args:
            self.tableau[self.length():] = [arg]

        return self.length()

    def reduce(self, fonction, valeurInitiale):
        pass

    def reverse(self):
        self.tableau = self.toReversed()
        return self

    def shift(self):
        premier_element = self.tableau[0]
        self.tableau = self.tableau[1:]
        return premier_element

    def slice(self, debut=0, fin=None):
        array = Array()
        if not fin:
            fin = self.length()

        if debut >= fin:
            raise ValueError(
                'la valeur initiale ne peut être supérieur à la taille du tableau')

        for i in range(debut, fin):
            array.push(self.tableau[i])

        return array

    def some(self, fonction):
        for element in self.iterate():
            if (fonction(element)):
                return True

        return False


array = Array(2, 4, 9, 7, 8, 4, 7, 2)
array2 = Array(5, 5, 7)
array3 = Array("yakasport", "diallogage", "dedy")
array3.push('salut', 'comment', 'tu', 'vas')

print(array3.some(lambda value: value == 'tdsu'))
