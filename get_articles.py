import requests
import json
import pathlib
def get_articles_gaurdian():
    api = '3df11a60-2bf6-4746-a991-c3a4250909a7'
    url = 'https://content.guardianapis.com/search?from-date=2020-01-01&order-by=relevance&page-size=100&q=Apple&api-key=' + api

    response = requests.get(url)
    response_json = response.json()
    print(response_json['root'])


if __name__ == '__main__':
    get_articles_gaurdian()

