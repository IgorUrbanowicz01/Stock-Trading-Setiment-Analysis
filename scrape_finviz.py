import sys
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime
import re
import pandas as pd
from pathlib import Path


def scrape_finviz(stock):
    p = Path('./data/' + stock + '.csv')
    current_article = ''
    original_df = None
    if p.exists():
        original_df = pd.read_csv(p)
        current_article = original_df.iloc[0]['article']

    month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
                  'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    df_dict = {'article': [], 'date': []}
    url = 'https://finviz.com/quote.ashx?t=' + stock + '&p=d'
    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urlopen(req) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
        titles = soup.find(id='news-table')
        article_date = datetime.today().date()
        for child in titles.findAll('tr', attrs={'class': 'cursor-pointer has-label'}):
            time = str(child.find('td', attrs={'align': 'right'}).string)
            title = str(child.find('a', attrs={'class': 'tab-link-news'}).string)
            if title == current_article:
                break
            if '-' in time:
                mont_re = re.search('[a-zA-Z]{3}', time)
                month = month_dict[mont_re.group()]
                day_year = re.search('[0-9]{2}-[0-9]{2}', time).group()
                full_date = month + '-' + day_year
                article_date = datetime.strptime(full_date, '%m-%d-%y').date()
            df_dict['article'].append(title)
            df_dict['date'].append(article_date)

    if p.exists():
        new_df = pd.DataFrame(df_dict)
        pd.concat([original_df, new_df])
    else:
        df = pd.DataFrame.from_dict(df_dict)
        df.to_csv(p, index=False)
