#!/usr/bin/env python3

def snake_case(chaine):
    if type(chaine) is str:
        resultat = ''
        flag = False

        if chaine.isalpha():
            if chaine[0].isupper():
                return "La chaine n'est pas en camelcase"

            for c in chaine:
                if c.isupper():
                    flag = True

            if flag == True:
                for caractere in chaine:
                    if caractere.isupper():
                        resultat += '_' + caractere.lower()
                    else:
                        resultat += caractere
                return resultat + ' ' + chaine

    return "La chaine n'est pas en camelcase"


# tableau de test
tests = ["salutLaTeam", "salut_la_team", "salut_la_Team", "SalutLaTeam", "salutlateam", "salut la team", "salut_lateam", "salut_la_team_",
         "_salut_la_team", "salut_la_team_", "salut__la_team", "salut_la__team", "salut_la_team_", "salut_la_team_", "salut_la_team_"]


for test in tests:
    print(snake_case(test))
