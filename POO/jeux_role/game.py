#!/usr/bin/env python3
import random


class Joueur:
    def __init__(self, nom, pv, pa, arme):
        self.nom = nom
        self.pv = pv
        self.pa = pa
        self.arme = arme

    def attaquer(self, cible):
        chance_attaquer = random.randint(0, 1)
        if chance_attaquer:
            print(f'{self.nom} attaque {cible.nom}')
            cible.pv -= self.pa
            if self.arme:
                print(f'{self.nom} a une arme de {self.arme.degat} dégats')
                cible.pv -= self.arme.degat
            cible.mourrir()

        else:
            print(f'{cible.nom} contre attaque {self.nom}')
            cible.attaquer(self)
            self.mourrir()

    def mourrir(self):
        if self.pv <= 0:
            print(f'Mort du joueur {self.nom}')


class Arme:
    def __init__(self, nom, degat):
        self.nom = nom
        self.degat = degat


diallo = Joueur('diallo', 15, 2, Arme('kalash', 20))
gage = Joueur('gage live coding', 15, 3, Arme('Sniper', 25))


i = 10

while i >= 10:
    diallo.attaquer(gage)
    i -= 1
