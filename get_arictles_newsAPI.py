
import requests
def get_arictles_newsAPI():
    api = '8b0df4dbbee64db9b907bab9ba071e34'

    url = "https://bing-news-search1.p.rapidapi.com/news/search"

    querystring = {"count": "100", "sortBy": "Date", "q": "Apple OR Iphone ", "textFormat": "Raw", "offset": "100",
                   "safeSearch": "Off"}

    headers = {
        "x-rapidapi-key": api,
        "x-rapidapi-host": "bing-news-search1.p.rapidapi.com",
        "X-BingApis-SDK": "true"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

if __name__ == '__main__':
    get_arictles_newsAPI()