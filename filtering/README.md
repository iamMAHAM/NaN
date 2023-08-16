# FILTERING

Créer une fonction nommée filtering qui prend en paramètre 1 tableau et qui rétourne 3 tableaux

- le premier tableau avec les entiers naturels pairs
- le second avec les entiers naturels impairs
- le troisième avec les autres types restant

## EXAMPLE

```python
tab = [1, 2, "salut", [], "{}", str(1), "test"]

result = filtering(tab)
print(result)
print(len(result))

```

la console affiche

```
[[2], [1], ["salut", [], "1", "test" ]]
3
```
