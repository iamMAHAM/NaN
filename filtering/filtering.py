tab = [1, 2, "salut", [], str(
    1), "test", {"school": 'NaN'}, 7, 6, 9, 11, 13, 15, -1, -1000]


def filtering(tableau):
    pair, impair, autres, results = [], [], [], []
    if (type(tableau) is list):
        for element in tableau:
            if (type(element) is int and element > 0 and element % 2 == 0):
                pair.append(element)
            elif type(element) is int and element > 0 and element % 2 == 1:
                impair.append(element)
            else:
                autres.append(element)

        results.append(pair)
        results.append(impair)
        results.append(autres)

        return results

    return -1


salut = filtering(tab)
erreur = filtering(2)
print(salut)
print(erreur)
