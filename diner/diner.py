#!/usr/bin/env python3


def heure_repas(chaine):
    if type(chaine) is str:
        divisee = chaine.split(':')

        if len(divisee) == 2:
            [heure, minutes] = divisee
