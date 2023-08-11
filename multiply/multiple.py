#!/usr/env/bin python3
import random


def est_multiple_de(n):
    continuer_partie = True
    while continuer_partie:
        try:
            nbr = int(input(' > : '))
            if (nbr % n == 0):
                print('CE nombre ' + str(nbr) +
                      ' est un multiple de ' + str(n))
            else:
                print('CE nombre ' + str(nbr) +
                      ' n\'est pas un multiple de ' + str(n))
        except ValueError:
            print('Erreur : veuillez entrer un nombre valide')

        except KeyboardInterrupt:
            reponse = input('voulez vous réellement quitter : ')
            if reponse == 'oui':
                continuer_partie = False
