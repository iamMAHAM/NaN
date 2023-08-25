#!/usr/bin/env python3

def min(nombres):
    if type(nombres) is list and len(nombres) > 0:
        if all(isinstance(i, (int, float)) for i in nombres):
            minimum = nombres[0]

            for nombre in nombres:
                if nombre < minimum:
                    minimum = nombre
            return minimum

    return -1


def max(nombres):
    if type(nombres) is list and len(nombres) > 0:
        if all(isinstance(i, (int, float)) for i in nombres):
            minimum = nombres[0]

            for nombre in nombres:
                if nombre > minimum:
                    minimum = nombre
            return minimum

    return -1


def min_max(nombres):
    return (min(nombres), max(nombres))


# 30 tests
tests = [
    ['a', 'b', 'c'],
    [1, 2, 3],
    [1.0, 2.0, 3.0],
    [1, 2.0, 3],
    [1, 3, "9"],
    [-5, 0, 2, 5, 3, -1]
]

for test in tests:
    print(min_max(test))
