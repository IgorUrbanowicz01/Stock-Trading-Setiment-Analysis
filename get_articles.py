import requests
import pandas as pd
import pathlib


def get_articles_gaurdian(subject):
    api = '3df11a60-2bf6-4746-a991-c3a4250909a7'
    try:
        df1 = pd.read_csv('./articles_gaurdian.csv')
        date = df1.tail(1)['date'].to_string(index=False)
    except FileNotFoundError:
        date = '2020-01-01'

    data_dict = {'title': [], 'date': []}
    url = 'https://content.guardianapis.com/search?section=technology&page-size=100&from-date=' + date + '&order-by=oldest&qApple%20and%20iphone%20&api-key=' + api
    response = requests.get(url)
    response_json = response.json()

    while response_json['response']['total'] != 1:
        for article in response_json['response']['results']:
            data_dict['title'].append(article['webTitle'])
            data_dict['date'].append(article['webPublicationDate'])
        date = data_dict['date'][-1]
        url = 'https://content.guardianapis.com/search?section=technology&page-size=100&from-date=' + date + '&order-by=oldest&q=Apple%20and%20iphone%20&api-key=' + api
        response = requests.get(url)
        response_json = response.json()

    df2 = pd.DataFrame.from_dict(data_dict)
    df2.to_csv('./articles_gaurdian.csv')


if __name__ == '__main__':
    get_articles_gaurdian('name')
