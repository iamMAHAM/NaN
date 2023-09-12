import requests
from bs4 import BeautifulSoup
import test

url = "https://www.jumia.ci/flash-sales/"


def getHTML(url):
    res = requests.get(url)
    return res.text


def parseHTML(source):
    soup = BeautifulSoup(source, 'html.parser')
    return soup


def main():
    soup = parseHTML(getHTML(url))
    atricles = soup.select('article.prd._p._fb')


# parseHTML(getHTML(url))

if __name__ == '__main__':
    main()
