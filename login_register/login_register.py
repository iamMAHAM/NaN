#!/usr/bin/env python3

bd = []


def recup_infos():
    nom = input('entrer votre nom : ')
    prenoms = input('entrer votre prenoms : ')
    age = int(input('entrer votre age : '))
    email = input('entrer votre email : ')
    motdepasse = input('entrer votre mot de passe : ')

    return {
        "nom": nom,
        "prenoms": prenoms,
        "age": age,
        "email": email,
        "motdepasse": motdepasse,
    }


def inscription(dico):
    if any(dico['email'] == utilisateur['email'] for utilisateur in bd):
        raise ValueError("L'utilisateur existe déjà")

    bd.append(dico)


def connexion():
    email = input('entrer votre email : ')
    motdepasse = input('entrer votre mot de passe : ')

    if any(email == utilisateur['email'] and motdepasse == utilisateur['motdepasse'] for utilisateur in bd):
        print('BIENVENUE')

    else:
        print('INDENTIFIANT INVALIDE')
