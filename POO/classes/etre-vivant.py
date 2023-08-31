#!/usr/bin/env python3


# creation d'une classe

class EtreVivant:
    nombre = 0

    def __init__(self, nom, age, taille):
        self.nom = nom
        self.age = age
        self.taille = taille
        self.nombre += 1

    def sePresenter(self):
        print(
            f"Salut je suis {self.nom} et j'ai {self.age} ans et je mesure {self.taille} cm")

    @staticmethod
    def lslsls():
        print('hello')

    @classmethod
    def afficher_tous(cls):
        print(cls.nombre)
