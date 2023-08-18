#!/usr/env/bin python3

def verifier_matricule(matricule):
    if type(matricule) is str and matricule.upper() == matricule:
        if matricule.isalnum():
            longueur_matricule = len(matricule)
            if longueur_matricule >= 2 and longueur_matricule <= 6:
                l1 = matricule[0]
                l2 = matricule[1]
                if l1.isalpha() and l2.isalpha():
                    numbers = []
                    for i in range(len(matricule)):
                        lettre = matricule[i]
                        if lettre.isdigit():
                            numbers.append(lettre)

                    if len(numbers) > 0:
                        indice_premier_nombre = matricule.index(numbers[0])
                        if numbers[0] != "0" and matricule[indice_premier_nombre:].isdigit():
                            return "Valide"
                        return "Invalide"

                    return "Valide"

    return "Invalide"


matricules = ["", "Hello", "AAA222", "AAA022", "AAA202", "22222", [], "@123", "123AAAAAAA", "A2AAA2",
              "A2A2A2", "A2A2A2A", "A2A2A2A2", "A2A2A2A2A", "A2A2A2A2A2", "A2a000A2A2A2A2A", "AA", "AA1000", "AA00000"]

for i in range(len(matricules)):
    print(f"#{i + 1} {verifier_matricule(matricules[i])}")
