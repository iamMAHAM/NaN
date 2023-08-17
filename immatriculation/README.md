# IMMATRICULATION

Dans le Massachusetts, il est possible de demander une plaque d'immatriculation de fantaisie pour sa voiture,
avec les lettres et les chiffres de son choix au lieu de lettres et de chiffres aléatoires. Parmi les exigences, cependant, il y a :

- les plaques d'immatriculation de fantaisie doivent commencer par au moins deux lettres.
- les plaques d'immatriculation de fantaisie peuvent contenir un maximum de 6 caractères (lettres ou chiffres) et un minimum de 2 caractères.
- Les chiffres ne peuvent pas être utilisés au milieu d'une plaque ; ils doivent être placés à la fin. Par exemple, AAA222 serait une plaque ... de vanité acceptable ; AAA22A ne le serait pas. Le premier chiffre utilisé ne peut être un '0'.

- Aucun point, espace ou signe de ponctuation n'est autorisé.

Implémentez une fonction verifier_matricule qui prend en paramètre 1 matricule et qui retourne 'Valide' si elle répond à toutes
les exigences ou 'Invalide' si ce n'est pas le cas.

## EXEMPLE

```python
resultat = verifier_matricule("AAA22A")
resultat2 = verifier_matricule("AAA222")
print(resultat)
print(resultat2)
```

la console affiche

```
Valide
Invalide
```
