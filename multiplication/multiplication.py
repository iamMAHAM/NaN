#!/usr/env/bin python3

def multiplication(n, limit=10):
    if type(n) is int and type(limit) is int and limit >= 10:
        for i in range(1, limit):
            print(f"{i} x {n} = {i * n}")
        return

    print("Impossible d'effectuer l'opération")


multiplication(10)
