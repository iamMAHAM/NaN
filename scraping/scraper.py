import requests
from bs4 import BeautifulSoup
import json

url = "https://www.jumia.ci/flash-sales/"


def getHTML(url):
    res = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    })
    return res.text


def parseHTML(source):
    soup = BeautifulSoup(source, 'html.parser')
    return soup


def main():
    articles = []
    soup = parseHTML(getHTML(url))
    divs = soup.select('article.prd._p._fb')

    for div in divs:
        href = div.select_one('a').attrs['href']
        titre = div.select_one('h3.name').text
        price = div.select_one('div.prc').text
        image = div.select_one('img').attrs['data-src']

        lien = f'https://jumia.ci{href}'

        soupDetail = parseHTML(getHTML(lien))

        description = soupDetail.select_one('markup.-mhm.-pvl')
        print(description)

        articles.append({"titre": titre, "price": price, "image": image})

    print(articles)

    with open('data.json', 'w') as file:
        file.write(json.dumps(articles, indent=2))


# parseHTML(getHTML(url))


if __name__ == '__main__':
    main()
