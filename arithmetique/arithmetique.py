#!/usr/env/bin python3

def evaluer(chaine):
    if type(chaine) is str:
        gauche = ''
        operateur = ''
        droite = ''
        for i in range(len(chaine)):
            caractere = chaine[i]
            if caractere == ' ':
                gauche = chaine[:i]
                operateur = chaine[i + 1]
                droite = chaine[i + 3:]
                break

        if gauche.isdigit() and droite.isdigit():
            gauche = int(gauche)
            droite = int(droite)

            if operateur == '+':
                return f"{(gauche + droite):.1f}"

            if operateur == '-':
                return f"{(gauche - droite):.1f}"

            if operateur == '*':
                return f"{(gauche * droite):.1f}"

            if operateur == '/':
                if droite == 0:
                    return "impossible de diviser par 0"
                return f"{(gauche / droite):.1f}"

    return "expression invalide"


def evaluer_simple(chaine):
    if type(chaine) is str:
        chaine_divisee = chaine.split(' ')
        if len(chaine_divisee) == 3:
            gauche = chaine_divisee[0]
            operateur = chaine_divisee[1]
            droite = chaine_divisee[2]
            if gauche.isdigit() and droite.isdigit():
                gauche = int(gauche)
                droite = int(droite)

                if operateur == '+':
                    return f"{(gauche + droite):.1f}"

                if operateur == '-':
                    return f"{(gauche - droite):.1f}"

                if operateur == '*':
                    return f"{(gauche * droite):.1f}"

                if operateur == '/':
                    if droite == 0:
                        return "impossible de diviser par 0"
                    return f"{(gauche / droite):.1f}"


def evaluer_hyper_facile(chaine):
    if type(chaine) is str:
        return eval(chaine)


# des tests pour la fonction evaluer
tests = ["1 + 1", "2 + 3", "2 - 6", "5 / 0"]

for test in tests:
    print(f"{test} = {evaluer(test)}")
