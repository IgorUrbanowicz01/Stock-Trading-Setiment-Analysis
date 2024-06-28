import scrapy
from pathlib import Path


def NYTspider(scr):
    name = 'nyt'

    def start_requests(self):
        urls=['https://www.nytimes.com/search?dropmab=false&endDate=2024-06-28&query=Apple%20&sort=best&startDate=2024-06-21']
        for url in urls:
            yield scrapy.Request(url=url, callback=parse)

    def parse(self, response):
        yield response.xpath('/body/div[2]/div[2]/main/div/div[2]/div[2]/ol/li[1]/div/div/div/a/h4/text()').get