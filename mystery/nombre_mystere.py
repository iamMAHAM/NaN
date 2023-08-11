
import random


def nombre_mystere():
    nombre_aleatoire = random.randint(1, 100)
    nombre_tentatives = 5
    na_pas_trouve = True
    while na_pas_trouve:
        entree = int(input('Choisir un nombre entre 1 et 100 : '))

        if (nombre_aleatoire > entree):
            nombre_tentatives = nombre_tentatives - 1
            if nombre_tentatives == 0:
                na_pas_trouve = False
            print("C'est plus il vous reste : " +
                  str(nombre_tentatives) + ' tentatives')

        elif (nombre_aleatoire < entree):
            nombre_tentatives = nombre_tentatives - 1
            if nombre_tentatives == 0:
                na_pas_trouve = False
            print("C'est moins il vous reste : " +
                  str(nombre_tentatives) + ' tentatives')

        else:
            print('Mes félicitations vous avez trouvé la bonne reponse : ', entree)
            na_pas_trouve = False
