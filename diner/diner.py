#!/usr/bin/env python3


def heure_repas(chaine):
    if type(chaine) is str:
        divisee = chaine.split(':')

        if len(divisee) == 2:
            [heure, minutes] = divisee

            if heure.isdigit() and minutes.isdigit():
                heure = int(heure)
                minutes = int(minutes)
                message = ''

                if 7 <= heure <= 8:
                    message = "petit-déjeuner"

                elif 12 <= heure <= 13:
                    message = "déjeuner"

                elif 18 <= heure <= 19:
                    message = "diner"
                else:
                    message = "repas non définie"

                def convert():
                    valeur = heure + (minutes * 0.5) / 30
                    if valeur > 25:
                        return "heure non définie"
                    return valeur

                return [message, convert()]

    return "le paramètre n'est pas une chaine de caractère"


# tableau des tests

tests = [
    "7:00",
    "7:30",
    "8:00",
    "8:30",
    "9:00",
    "9:30",
    "9:45",
    "10:00",
    "10:30",
    "11:00",
    "11:10",
    "11:14",
    "9:07",
    "11:5656789",
    "11:14",
    "salut comment tu vas ?",
    "1s:123",
    "11:30:25",
    "salut:14"
]


for test in tests:
    print(heure_repas(test))
