#!/usr/bin/env python3

def countWords(text):
    return len(text.split())


def reverse(text):
    return text[::-1]


def removeSpace(text):
    return "".join(text.split())


def searchPosition(text, mot):
    return text.find(mot)


def replaceWords(text, mot, replace):
    return text.replace(mot, replace)


def isPalindrome(word):
    return word == word[::-1]


def toUppercase(word):
    return word.upper()


def splitWordToArrat(sentence):
    return [word for word in list(filter(lambda x: x.isalpha(), sentence.split()))]


def extractDomainFromEmail(email):
    return email.split('@')[1]


def deleteHTMLBalise(string):
    pass


def generateString(length):
    from random import randint
    from string import ascii_letters

    result = ''
    for _ in range(length):
        result += ascii_letters[randint(0, len(ascii_letters))]

    return result


# print(splitWordToArrat("salut comment tu vas ?"))
# print(extractDomainFromEmail('jean@gmail.com'))
print(generateString(10))
