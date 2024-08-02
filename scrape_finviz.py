import sys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def scrape_finviz(name):
    url = 'https://finviz.com/quote.ashx?t=AAPL&p=d'
    req = Request(
        url=url

    )
    with urlopen(url) as response:
        print(response.read())

if __name__ == '__main__':
    scrape_finviz('milk')